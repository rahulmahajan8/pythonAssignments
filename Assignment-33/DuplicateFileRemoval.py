import hashlib

def CalculateChecksum(path, blocksize=1024):
    hobj = hashlib.md5()

    with open(path, "rb") as f:
        buffer = f.read(blocksize)

        while len(buffer) > 0:
            hobj.update(buffer)
            buffer = f.read(blocksize)

    return hobj.hexdigest()