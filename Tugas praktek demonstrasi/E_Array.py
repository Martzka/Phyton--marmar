def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)

def main():
    
    try:
        jumlah = int(input("Masukkan nilai yang ingin dirata - ratakan: "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    if jumlah <= 0:
        print("Jumlah nilai harus lebih besar dari 0!")
        return

    nilai = []
    for i in range(jumlah):
        try:
            angka = float(input(f"Masukkan nilai ke-{i + 1}: "))
            nilai.append(angka)
        except ValueError:
            print("Input harus berupa angka!")
            return

    rata_rata = hitung_rata_rata(nilai)

    print("\nNilai yang Anda masukkan:")
    for i, n in enumerate(nilai, start=1):
        print(f"Nilai ke-{i}: {n}")
    print(f"\nRata-rata nilai: {rata_rata:.2f}")

if __name__ == "__main__":
    main()
