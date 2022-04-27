# Casting Jenis Data

**Casting** ialah mengubah satu jenis data ke jenis data yang berbeza
|Built in Functions|Kegunaan|
|------------------------|--------------------------------|
| ```bool(string|int|float)` ``| tukarkan jenis data lain kepada jenis **boolean** |
| ```float(string|boolean|int)``` | tukarkan jenis data lain kepada jenis **float** |
| ```int(string|boolean|float)```| tukarkan jenis data lain kepada jenis **int** |
| ```string(float|boolean|int)``` | tukarkan jenis data lain kepada jenis **string** |

## Tambahan
+ `bool(0)` menghasilkan **FALSE**
+ `int(9.9)` menghasilkan **9** (dibulatkan ke nilai bawah)
+ `bool("")` string kosong menghasilakn **FALSE**
+ `int("ayam")` hasilakan ERROR kerana hanya boleh tukarkan nombor sahaja