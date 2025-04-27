import sys
import hashlib

hash_f = hashlib.sha256()

a = sys.argv[1]
with open(a, 'rb') as f:
    for chunk in iter(lambda: f.read(4096), b""):
            hash_f.update(chunk)
            
print(hash_f.hexdigest())