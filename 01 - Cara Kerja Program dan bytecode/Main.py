import time
start_time= time.time()
# ini komen single line
"""ini
komen 
multi line"""

# memaparkan teks ke layar 
print("Mhaziqrk")
# output
# Mhaziqrk


print(time.time()- start_time,"saat")

# Python boleh dicompile ke bytecode
# cara compilenya --> python3 -m py_compile [Nama Fail]
# Contoh :  python3 -m py_compile Main.py
# python yang dicompile akan lebih cepat dijalankan
# bytecode python berada dalam folder __pycache__
# output masa dicompile vs tidak dicompile:
# 5.078315734863281e-05 saat  || 5.078315734863281e-05 saat