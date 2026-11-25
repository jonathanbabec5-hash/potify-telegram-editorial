from pathlib import Path
from hashlib import sha256
import sys
import unicodedata

def fingerprint(text):
    normalized = ' '.join(unicodedata.normalize('NFC', text).split())
    if not normalized:
        raise ValueError('Empty draft')
    return sha256(normalized.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    print(fingerprint(Path(sys.argv[1]).read_text(encoding='utf-8')))
