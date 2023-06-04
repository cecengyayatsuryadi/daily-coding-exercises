"""
Buat program Python yang mengimplementasikan struktur data stack dan kemudian melakukan beberapa operasi pada stack tersebut, seperti push, pop, dan is_empty.
"""


def main():
    stack = []
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Is Empty")
        print("4. Exit")
        choice = input("Masukkan pilihan: \n")
        if choice == "1":
            item = input("Masukkan item: \n")
            stack.append(item)
            print(f"Item {item} berhasil ditambahkan ke dalam stack.")
        elif choice == "2":
            if len(stack) == 0:
                print("Stack kosong.")
            else:
                item = stack.pop()
                print(f"Item {item} berhasil dihapus dari stack.")
        elif choice == "3":
            if len(stack) == 0:
                print("Stack kosong.")
            else:
                print("Stack tidak kosong.")
        elif choice == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan kembali.")


if __name__ == "__main__":
    main()

# catatan: stack adalah struktur data yang mengikuti prinsip LIFO (Last In First Out). Artinya, item yang terakhir dimasukkan ke dalam stack akan menjadi item pertama yang dihapus dari stack.
