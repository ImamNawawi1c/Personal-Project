import hashlib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SIGNATURE_FILE = os.path.join(BASE_DIR, "signatures.txt")

def get_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def load_signatures():
    with open(SIGNATURE_FILE) as f:
        return f.read().splitlines()

def scan_file(file_path):
    if not os.path.isfile(file_path):
        return "File Not Found"

    file_hash = get_md5(file_path)
    signatures = load_signatures()

    if file_hash in signatures:
        return "⚠️Virus Terdeteksi"
    return "File Aman ✅"

