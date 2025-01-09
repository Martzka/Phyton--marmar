def sapa():
    print("Welcome to program kalkulator")

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Kesalahan: Tidak bisa membagi dengan nol!"

def main():
    sapa()  
    results = [] 
    
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

    results.append((operasi, angka1, angka2, hasil))
    print(f"Hasil operasi adalah: {hasil}")
    print("---------------------------")
    print("--- Hasil Semua Operasi ---")
    for result in results:
        print(f"{result[0].capitalize()} antara {result[1]} dan {result[2]}: {result[3]}")
        
if __name__ == "__main__":
    main()
