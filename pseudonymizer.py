from faker import Faker
from cryptography.fernet import Fernet
import hashlib
from typing import TypedDict, Dict, Optional, Iterable


fake = Faker("ko-KR")
sensitive_names = ["길동", "철수", "영희", "민수"]

class MappingInfo(TypedDict):
    token: str
    pseudo: str
    count: int


class CryptoManager:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, origin):
        return self.cipher.encrypt(origin.encode()).decode()

    def decrypt(self, token):
        return self.cipher.decrypt(token.encode()).decode()
    
    def hash(self, origin):
        return hashlib.sha256(origin.encode()).hexdigest()


class Session:
    def __init__(
        self, 
        session_id: str, 
        crypto_manager: CryptoManager, 
        max_mention_gap: int = 5
    ):
        self.session_id = session_id
        self.crypto_manager = crypto_manager
        self.max_mention_gap = max_mention_gap
        self.mapping: Dict[str, MappingInfo] = {} 
        

    def update_mention_counter(self, origins: Optional[Iterable[str]] = None):
        to_delete = []

        if origins is None:
            for hash_key, info in self.mapping.items():
                info['count'] += 1
                if info['count'] >= self.max_mention_gap:
                    to_delete.append(hash_key)
        else:  
            origin_hashes = {self.crypto_manager.hash(name) for name in origins}
            for hash_key, info in self.mapping.items():
                if hash_key in origin_hashes:
                    info['count'] = 0
                else:
                    info['count'] += 1
                    if info['count'] > self.max_mention_gap:
                        to_delete.append(hash_key)

        for key in to_delete:
            origin = self.crypto_manager.decrypt(self.mapping[key]['token'])
            print(f"Removing mapping: {self.mapping[key]['pseudo']} (original: {origin})")
            del self.mapping[key]

        return to_delete
    
    def pseudonymize(self, text: str) -> str:
        found_names = set()

        for name in sensitive_names:
            if name in text:
                found_names.add(name)
                origin_hash = self.crypto_manager.hash(name)

                if origin_hash in self.mapping:
                    pseudo = self.mapping[origin_hash]["pseudo"]
                    self.mapping[origin_hash]["count"] = 0
                else:
                    pseudo = fake.name()
                    self.mapping[origin_hash] = {
                        "token": self.crypto_manager.encrypt(name),
                        "pseudo": pseudo,
                        "count": 0
                    }
                text = text.replace(name, pseudo)

        if found_names:
            self.update_mention_counter(found_names)
        else:
            self.update_mention_counter(None)
            
        return text

    def depseudonymize(self, text: str) -> str:
        for info in self.mapping.values():
            original = self.crypto_manager.decrypt(info["token"])
            pseudo = info["pseudo"]
            text = text.replace(pseudo, original)
        return text




