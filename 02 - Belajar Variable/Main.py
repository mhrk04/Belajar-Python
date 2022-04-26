# Variable adalah tempat menyimpan data

# assignment nilai | terus masukkan data ke dalam variable
# tidak perlu deklarasi seperti --> int [namaVariable];
a = 10
x = 5
lebar = 100.200

print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai lebar = ", lebar)
# output:
"""
Nilai a =  10
Nilai x =  5
Nilai lebar =  100.2
"""
# penamaan variable boleh menggunakan beberapa cara
nialai_y = 10 # guna underscore
tahun1 = 11 #nombor dibelakang | tidak boleh didahului nombor
nialK = 10.50 #rapat semua dan Huruf besar disetiap perkataan baharu

# pemanggilan kedua
print("Nilai a = ", a)
a = 10000
print("Nilai a = ", a) #nilai a akan berubah mengikut nilai variable terkini |'python dibaca dari atas ke bawah'
# output:
"""
Nilai a =  10
Nilai a =  10000
"""
# assignment indirect
b = a
print("Nialai b =", b)

"""
Output:
Nialai b = 10000
"""