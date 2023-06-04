"""
Buat program Python yang meminta pengguna untuk memasukkan sebuah string dan kemudian menampilkan jumlah karakter dalam string tersebut.
"""


# validasi input
def validasi_input(input_string):
    """
    Function ini digunakan untuk memvalidasi input dari pengguna.
    """
    while True:
        user_input = input(input_string)
        if len(user_input) == 0:
            print("Input tidak boleh kosong. Silakan masukkan kembali.")
        else:
            return user_input


# menghitung jumlah karakter dalam string
def hitung_karakter(string):
    """
    Function ini digunakan untuk menghitung jumlah karakter dalam string.
    """
    return len(string)


def main():
    # meminta input dari pengguna
    input_1 = validasi_input("Masukkan sebuah string: \n")

    # menghitung jumlah karakter dalam string
    jumlah_karakter = hitung_karakter(input_1)

    # menampilkan hasil
    print(f"Jumlah karakter dalam string {input_1} adalah {jumlah_karakter}")


if __name__ == "__main__":
    main()
