#casting --> mengubah satu jenis data ke jenis data yang berbeza
# ubah integer kepada pelbagai jenis data
print("=================INTEGER======================")
data_int= 10
print("Data =",data_int,", Jenis = ", type(data_int))
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai == 0
print("Data =",data_float,", Jenis = ", type(data_float))
print("Data =",data_str,", Jenis = ", type(data_str))
print("Data =",data_bool,", Jenis = ", type(data_bool))


# Float ---> jenis lain
print("=================FLOAT======================")
data_float= 9.9
print("Data =",data_float,", Jenis = ", type(data_float))
data_int = int(data_float) #akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai == 0
print("Data =",data_int,", Jenis = ", type(data_int))
print("Data =",data_str,", Jenis = ", type(data_str))
print("Data =",data_bool,", Jenis = ", type(data_bool))


# Boolean ---> jenis lain
print("=================BOOLEAN======================")
data_bool=True 
print("Data =",data_bool,", Jenis = ", type(data_bool))
data_int = int(data_bool) #akan dibulatkan kebawah
data_str = str(data_bool)
data_float = float(data_bool) # akan false jika nilai == 0
print("Data =",data_int,", Jenis = ", type(data_int))
print("Data =",data_str,", Jenis = ", type(data_str))
print("Data =",data_float,", Jenis = ", type(data_float))

# STRING ---> jenis lain
print("=================STRING======================")
data_str="100"
print("Data =",data_str,", Jenis = ", type(data_str))
data_int = int(data_str) # mesti nombor bru boleh ditukar ke int/float
data_bool = bool(data_str)# string kosong baru false
data_float = float(data_str) # 
print("Data =",data_int,", Jenis = ", type(data_int))
print("Data =",data_bool,", Jenis = ", type(data_bool))
print("Data =",data_float,", Jenis = ", type(data_float))