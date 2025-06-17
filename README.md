# secure-pseudonymizer
A lightweight Python demo for pseudonymizing sensitive Korean names.
It replaces sensitive personal names with generated pseudonyms while maintaining reversible mappings secured by encryption.

### Features
- Pseudonymization of predefined sensitive names (e.g., 길동, 철수, 영희, 민수).
- Uses AES encryption (via cryptography library) to securely store and reversibly map original names to pseudonyms.
- Each session manages an independent mapping, maintaining a separate pseudonymization state per session.
- Automatically removes old mappings if not mentioned for a configurable number of interactions.
- Simple command-line interface for testing pseudonymization and depseudonymization.

### Create and activate virtual environment
```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

### Installation
```bash
pip install -r requirements.txt
```

### Usage
Run the test script to try pseudonymization interactively:
```bash
python main.py
```
Enter text containing sensitive names to see them replaced by pseudonyms and restored back.
