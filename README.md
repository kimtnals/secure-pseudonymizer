# secure-pseudonymizer
A lightweight Python demo for pseudonymizing sensitive Korean names.
It replaces sensitive personal names with generated pseudonyms while maintaining reversible mappings secured by encryption.

### Features
- Pseudonymization of predefined sensitive names (e.g., 길동, 철수, 영희, 민수).
- Uses AES encryption (via cryptography library) to securely store and reversibly map original names to pseudonyms.
- Automatically removes old mappings if not mentioned for a configurable number of interactions.
- Simple command-line interface for testing pseudonymization and depseudonymization.

### Installation
```bash
pip install -r requirements.txt
```

### Usage
Run the test script to try pseudonymization interactively:
```bash
python test_pseudonymizer.py
```
Enter text containing sensitive names to see them replaced by pseudonyms and restored back.
