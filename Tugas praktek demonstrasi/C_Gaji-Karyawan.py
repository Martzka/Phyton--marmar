nama = input("Masukkan nama karyawan: ")
golongan = input("Masukkan golongan (A/B/C/D): ").upper()
jam_kerja = int(input("Masukkan jam kerja dalam seminggu: "))

if golongan == "A":
    upah_per_jam = 5000
elif golongan == "B":
    upah_per_jam = 7000
elif golongan == "C":
    upah_per_jam = 8000
elif golongan == "D":
    upah_per_jam = 10000
else:
    print("Golongan tidak valid!")
    exit()

if jam_kerja > 48:
    lembur = (jam_kerja - 48) * 4000
else:
    lembur = 0
gaji = (jam_kerja * upah_per_jam) + lembur

print("\n--- Rincian Gaji ---")
print(f"Nama Karyawan: {nama}")
print(f"Golongan: {golongan}")
print(f"Gaji Mingguan: Rp {gaji:,}")