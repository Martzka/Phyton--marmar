import math
class Lingkaran:
    def __init__(self,r):
        self.r = r
        
    def hitung_luas(self):
        return math.pi * self.r**2

# lingkaran1 = Lingkaran(10)
# lingkaran2 = Lingkaran(14)
r = float(input("Masukkan jari jari lingkaran ="))
Lingkaran = Lingkaran(r)
print("luas lingkaran = ", Lingkaran.hitung_luas())

# print('Luas lingkaran1:', Lingkaran.hitung_luas())
# print('Luas lingkaran2:', Lingkaran.hitung_luas())
