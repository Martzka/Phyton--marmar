def gaji_karyawan(golongan, jam_kerja):
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
        return None

    if jam_kerja > 48:
        lembur = (jam_kerja - 48) * 4000
    else:
        lembur = 0
    gaji = (jam_kerja * upah_per_jam) + lembur
    return gaji

def input_karyawan():
    nama = input("Nama karyawan: ")
    golongan = input("Golongan (A/B/C/D): ").upper()
    try:
        jam_kerja = int(input("Jam kerja dalam seminggu: "))
    except ValueError:
        print("Input jam kerja tidak valid!")
        return None, None, None
    return nama, golongan, jam_kerja

def main():
    print("--- RINCIAN GAJI KARYAWAN ---")
    karyawan_data = []
    jumlah_karyawan = int(input("Berapa banyak karyawan yang mau Anda hitung gajinya? "))
    
    for i in range(jumlah_karyawan):
        print(f"Data karyawan {i+1}:")
        nama, golongan, jam_kerja = input_karyawan()
        if nama is None or golongan is None or jam_kerja is None:
            continue
        karyawan_data.append((nama, golongan, jam_kerja))

    for nama, golongan, jam_kerja in karyawan_data:
        gaji = gaji_karyawan(golongan, jam_kerja)
        if gaji is not None:
            print(f"--- GAJI KARYAWAN ---")
            print(f"Nama Karyawan: {nama}")
            print(f"---------------------")
            print(f"Golongan: {golongan}")
            print(f"---------------------")
            print(f"Jam Kerja: {jam_kerja} jam")
            print(f"---------------------")
            print(f"Gaji Mingguan: Rp {gaji:,}")

main()
