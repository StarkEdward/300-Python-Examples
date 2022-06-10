# 013. How to Extract extension from filename
import os.path

for path in ["text.txt", "filename", "/user/system.text.txt", "/", ""]:
    print('"%s" : ' % path, os.path.splitext(path))
