def input_alas_dan_tinggi ():
  alas = float(input('Masukkan alas: '))
  tinggi = float((input('Masukkan tinggi: ')))

  return alas, tinggi

def hitung_luas (alas, tinggi):
  return 0.5 * alas * tinggi

"""kalau fungsional, kita sendiri yang mengelola
hasil kembaliannya"""
print(hitung_luas(5, 10))
alas, tinggi = input_alas_dan_tinggi()
print(hitung_luas(alas, tinggi))
