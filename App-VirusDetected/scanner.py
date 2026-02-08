import hashlib # mengubah isi data jadi hash/sidik jari digital
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #ini mengambil alamat dimana folder scanner berada
SIGNATURE_FILE = os.path.join(BASE_DIR, "signatures.txt") #gabungkan folder di atas dengan signatures.txt/
# yg bertujuan supaya program selalu tahu dimana dtabase lokasi virus tersimpan

def get_md5(file_path): #filepath itu untuk menginput alamat file
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f: # rb(read binary, wajib untuk membuka file apapun) dan as f itu file nya disimpan di variabel f
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
    signatures = load_signatures() # jadi file signatures.txt itu sebagai database virus

    if file_hash in signatures:
        result = "Virus Terdeteksi"
    else:
        result = "File Aman "
    log_result(file_path,result)
    return result

def log_result(file_path,result):
    with open("log.txt","a") as log:
        log.write(f"{file_path} -> {result}\n")
