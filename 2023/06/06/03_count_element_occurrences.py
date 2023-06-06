import os


def count_element_occurrences(tuple_data, element):
    return tuple_data.count(element)


tuple_data = tuple(
    input("Masukkan data tuple (pisahkan dengan koma tanpa spasi): ").split(",")
)
element = input("Masukkan elemen yang ingin dihitung kemunculannya: ")

occurrence_count = count_element_occurrences(tuple_data, element)
print("Jumlah kemunculan elemen", element, "dalam tuple:", occurrence_count)

# meminta user untuk mengulang program atau tidak
while True:
    ulangi = input("\nUlangi program? (y/t): ")
    if ulangi in ("y", "t"):
        if ulangi == "y":
            # hapus layar
            os.system("cls" if os.name == "nt" else "clear")
            # jalankan ulang program
            os.system("python " + __file__)
        else:
            print("Program selesai.")
            break
    else:
        print("Input tidak valid.")
