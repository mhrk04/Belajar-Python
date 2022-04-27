# amik input dari user
# input() mengambil data string
data = input("masukkan data : ")
print("Data :",data,"Jenis :",type(data))

#kalau nak amik data integer

nombor = int(input("Masukkan nombor :"))
nombor = float(input("Masukkan nombor :"))

print("data = ",nombor,", type =",type(nombor))


# input boolean

biner = bool(int(input("Masukkan nilai boolean")))
print("data =",biner,"type = ",type(biner))