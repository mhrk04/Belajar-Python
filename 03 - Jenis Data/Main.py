# Jenis data
# a = 10 , ialah variable yang punyai nilai 10

# Jenis data : angka (integer)
Integer = 10
print("Data :", Integer)
print("- berjenis", type(Integer))
# Jenis data : (float) nombor perpuluhan
data_float = 3.142
print("Data :", data_float)
print("- berjenis", type(data_float))

# Jenis data : string (teks biasa)
data_string = "saya suka nasi ayam"
print("Data :", data_string)
print("- berjenis", type(data_string))

# Jenis data : boolean (TRUE/FALSE)
data_boolean = False
print("Data :", data_boolean)
print("- berjenis", type(data_boolean))


# Jenis data khusus

# bilangan Complex
data_complex = complex(5,6)
print("Data :", data_complex)
print("- berjenis", type(data_complex))

# Jenis data yang diimport dari bahasa C
from ctypes import c_double,c_long

data_c_double = c_double(10.23654789)
print("Data :", data_c_double)
print("- berjenis", type(data_c_double))
