"""
Buat program Python yang meminta pengguna untuk memasukkan sebuah string dan kemudian menampilkan string tersebut dalam urutan terbalik.
"""


def main():
    while True:
        input_1 = input("Masukkan sebuah string: \n")
        if input_1.isalpha():
            break
        else:
            print("String harus berupa huruf. Silakan masukkan kembali.")

    print(f"String terbalik: {input_1[::-1]}")


if __name__ == "__main__":
    main()

# catatan: [::-1] digunakan untuk membalikkan string.
# .isalpha() digunakan untuk mengecek apakah string hanya berisi huruf.
