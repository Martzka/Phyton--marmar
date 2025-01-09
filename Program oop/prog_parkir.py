# class Parkir:
#     def __init__(self, jenis_kendaraan, lama_parkir, is_member):
#         self.jenis_kendaraan = jenis_kendaraan
#         self.lama_parkir = lama_parkir
#         self.is_member = is_member
        
#     def Hitung_biaya(self):
#         biaya = 0
#         if self.jenis_kendaraan.lower () == "mobil":
#             biaya += 5000
#             self.lama_parkir -= 1
            

def hitung_biaya_parkir(jenis_kendaraan, lama_parkir, is_member):
    # Tarif parkir
    if jenis_kendaraan.lower() == "mobil":
        tarif_jam_pertama = 5000
        tarif_jam_berikutnya = 3000
    elif jenis_kendaraan.lower() == "motor":
        tarif_jam_pertama = 3000
        tarif_jam_berikutnya = 2000
    else:
        return "Jenis kendaraan tidak valid."

    # Menghitung biaya parkir
    if lama_parkir <= 1:
        total_biaya = tarif_jam_pertama
    else:
        total_biaya = tarif_jam_pertama + (lama_parkir - 1) * tarif_jam_berikutnya

    # Diskon untuk member
    if is_member:
        total_biaya *= 0.9

    return total_biaya


# Input dari pengguna
jenis_kendaraan = input("Masukkan jenis kendaraan (motor/mobil): ")
lama_parkir = int(input("Masukkan lama parkir (dalam jam): "))
password = input("Masukkan password untuk member (kosongkan jika bukan member): ")

# Menentukan status member
is_member = password == "member123"  # Ganti "member123" dengan password yang diinginkan

# Menghitung dan menampilkan hasil
biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir, is_member)
if isinstance(biaya, str):
    print(biaya)  # Menampilkan pesan error jika jenis kendaraan tidak valid
else:
    print(f"Biaya parkir untuk {jenis_kendaraan} selama {lama_parkir} jam adalah: Rp {int(biaya)}")
