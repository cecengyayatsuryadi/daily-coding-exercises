# Program Python yang meminta pengguna untuk memasukkan dua bilangan bulat dan kemudian menampilkan hasil penjumlahan, pengurangan, perkalian, dan pembagian dari kedua bilangan tersebut.


# metode input() digunakan untuk menerima input dari pengguna
def main():
    while True:
        input_1 = input("Bilangan bulat 1: \n")
        input_2 = input("Bilangan bulat 2: \n")
        try:
            input_1 = int(input_1)
            input_2 = int(input_2)
            if input_1 == 0 or input_2 == 0:
                raise ValueError
            break
        except ValueError:
            print(
                "Bilangan bulat harus berupa angka dan tidak boleh 0. Silakan masukkan kembali."
            )

    # meminta operator matematika dari pengguna
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    # meminta operator matematika dari pengguna
    while True:
        operator = input("Masukkan operator matematika (+, -, *, /): \n")
        if operator in operators:
            hasil = operators[operator](input_1, input_2)
            break
        else:
            print("Operator matematika tidak valid. Silakan masukkan kembali.")

    # menampilkan hasil
    print("Hasil: ", hasil)


if __name__ == "__main__":
    main()

# catatan: lambda adalah fungsi tanpa nama yang dapat mengambil argumen dan mengembalikan nilai. Dalam contoh ini, lambda digunakan untuk mengimplementasikan fungsi penjumlahan, pengurangan, perkalian, dan pembagian.
