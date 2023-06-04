"""
Buat program Python yang meminta pengguna untuk memasukkan sebuah bilangan bulat dan kemudian menampilkan apakah bilangan tersebut genap atau ganjil.
"""


# metode input() digunakan untuk menerima input dari pengguna
def main():
    while True:
        input_1 = input("Masukkan sebuah bilangan bulat: \n")
        try:
            input_1 = int(input_1)
            break
        except ValueError:
            print("Bilangan bulat harus berupa angka. Silakan masukkan kembali.")

    if input_1 % 2 == 0:
        print(f"Bilangan {input_1} adalah bilangan genap.")
    else:
        print(f"Bilangan {input_1} adalah bilangan ganjil.")


# memanggil function utama
if __name__ == "__main__":
    main()
