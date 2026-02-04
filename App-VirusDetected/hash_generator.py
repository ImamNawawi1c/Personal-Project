import hashlib

with open("virus_disini.txt","rb") as f:
    print(hashlib.md5(f.read()).hexdigest())