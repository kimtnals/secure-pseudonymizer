import uuid
from src.pseudonymizer import CryptoManager, Session

class Client:
    def __init__(self):
        self.crypto_manager = CryptoManager()
        self.sessions = {}
        self.current_session_id = None

    def create_new_session(self):
        session_id = str(uuid.uuid4())
        session = Session(session_id, self.crypto_manager)
        self.sessions[session_id] = session
        self.current_session_id = session_id
        print(f"\n[New Session Created] Session ID: {session_id}\n")
        self.run_session(session)

    def list_sessions(self):
        if not self.sessions:
            print("\n[!] No sessions available.\n")
            return

        print("\n[Session List]")
        print(f"{'Session ID':<40}")
        print("-" * 40)
        for sid in self.sessions.keys():
            mark = " (current)" if sid == self.current_session_id else ""
            print(f"{sid}{mark}")
        print("-" * 40 + "\n")

    def select_session(self):
        if not self.sessions:
            print("\n[!] No sessions available.\n")
            return

        self.list_sessions()
        selected_id = input("Enter Session ID to select: ").strip()
        if selected_id in self.sessions:
            self.current_session_id = selected_id
            print(f"\n[Session Selected] Current Session ID: {self.current_session_id}\n")
            session = self.sessions[self.current_session_id]
            self.run_session(session)
        else:
            print("\n[!] Invalid Session ID.\n")

    def run_session(self, session: Session):
        print("=== Pseudonymization Session Mode ===")
        print("Type 'quit' to return to main menu.\n")
        while True:
            text = input("Enter text: ")
            if text.strip().lower() == "quit":
                print("Returning to main menu.\n")
                break

            pseudo_text = session.pseudonymize(text)
            print("\n[Pseudonymized Text]")
            print(pseudo_text)

            restored_text = session.depseudonymize(pseudo_text)
            print("\n[Restored Text]")
            print(restored_text)

            print("\n[Current Mapping Counts]")
            print(f"{'Original Name':<15} | {'Count':<5}")
            print("-" * 25)
            for info in session.mapping.values():
                original = session.crypto_manager.decrypt(info["token"])
                print(f"{original:<15} | {info['count']:<5}")
            print("-" * 25 + "\n")
