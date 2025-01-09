def sapa(): #sapaan
    print("Selamat datang di program kalkulator sederhana!")

def tambah(a, b):   #Tambah
    return a + b
def kurang(a, b):   #Pengurangan
    return a - b
def kali(a, b):     #Perkalian
    return a * b
def bagi(a, b):     #Pembagian
    if b != 0:
        return a / b
    else:
        return "Kesalahan: Tidak bisa membagi dengan nol!"


def main():
    sapa()
    
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    print("\nPilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        hasil = tambah(angka1, angka2)
        operasi = "penjumlahan"
    elif pilihan == "2":
        hasil = kurang(angka1, angka2)
        operasi = "pengurangan"
    elif pilihan == "3":
        hasil = kali(angka1, angka2)
        operasi = "perkalian"
    elif pilihan == "4":
        hasil = bagi(angka1, angka2)
        operasi = "pembagian"
    else:
        print("Pilihan tidak valid!")
        return

    print(f"\nHasil {operasi} dari {angka1} dan {angka2} adalah: {hasil}")

if __name__ == "__main__":
    main()