def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)):
        return True
    else:
        return False

def input_tahun():
    tahun = input("Masukkan tahun: ")
    if not tahun.isdigit():
        print("Input tidak valid")
        return None
    return int(tahun)

def main():
    print("Welcome di perhitungan tahun kabisat :)")
    tahun_array = []
    jumlah_tahun = int(input("Berapa banyak tahun yang mau di cek ? "))
    
    for i in range(jumlah_tahun):
        tahun = input_tahun()
        if tahun is not None:
            tahun_array.append(tahun)
    
    for tahun in tahun_array:
        if tahun_kabisat(tahun):
            print(f"{tahun} tahun kabisat.")
        else:
            print(f"{tahun} bukan tahun kabisat.")
            
main()
