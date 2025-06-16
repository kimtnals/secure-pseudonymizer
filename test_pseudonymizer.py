import uuid
from pseudonymizer import CryptoManager, Session

crypto_manager = CryptoManager()
session = Session(str(uuid.uuid4()), crypto_manager)

def test_pseudonymization():
    print("=== Pseudonymization Test ===")
    while True:
        text = input("Enter text (empty line to exit): ")
        if not text.strip():
            print("Exiting test.")
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


if __name__ == "__main__":
    test_pseudonymization()
