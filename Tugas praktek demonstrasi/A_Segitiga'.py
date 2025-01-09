import math
def sapaan():
    print("Perhitungan Luas Segitiga")

def hitung_luas(alas, tinggi):
    return (alas * tinggi) / 2

def input_data():
    alas = input("Panjang segitiga: ")
    tinggi = input("Tinggi segitiga: ")
    if alas.isalpha() or tinggi.isalpha():
        print("Input tidak valid")
        return None, None
    return float(alas), float(tinggi)

def main():
    segitiga_data = [] 
    for i in range(2):
        print(f"Segitiga {i+1}:")
        alas, tinggi = input_data()
        if alas is None or tinggi is None:
            return
        
        segitiga_data.append((alas, tinggi))

    for i, (alas, tinggi) in enumerate(segitiga_data):
        luas = hitung_luas(alas, tinggi)
        print(f"Luas segitiga {i+1} = {luas:.2f}")


main()
