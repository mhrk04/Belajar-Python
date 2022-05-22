# Latihan Perhitungan Sederhana

Mengaplikasikan apa yang dipelajari dari topik-topik yang lepas. Aku akan membuat aplikasi python yang mengkonversi nilai Mbps ke MBps. Mbps **tidak sama** dengan MBps.


| Unit | Formula |
| ----------- | ----------- |
| Mbps --> MBps | Mbps * 0.125000 |

## Code

``` python
print ("Program penukaran Mbps ke MBps")

print("Tidak Perlu Menulis unit di hujung nilai")

MbpsIN = float(input("Sila Masukkan nilai yang yang hendak di konversi : "))

toMBps = MbpsIN * 0.125000

print("Nilai",MbpsIN,"Mbps dalam MBps ialah",toMBps,"MBps")
```

## Output

```
Program penukaran Mbps ke MBps
Tidak Perlu Menulis unit di hujung nilai
Sila Masukkan nilai yang yang hendak di konversi : 50
Nilai 50.0 Mbps dalam MBps ialah 6.25 MBps
```