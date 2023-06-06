"""
Buatlah program Python untuk menggabungkan dua tuple menjadi satu tuple.
"""


# fungsi untuk menggabungkan dua tuple menjadi satu tuple
def merge_tuples(tup1, tup2):
    return tup1 + tup2


# list tuple
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)

# memanggil fungsi merge_tuples
merged_tuple = merge_tuples(tup1, tup2)

# menampilkan hasil
print("Merged tuple:", merged_tuple)


if __name__ == "__main__":
    pass

# output
# Merged tuple: (1, 2, 3, 4, 5, 6)


"""
Catatan:
- Tuple bersifat immutable, artinya tidak dapat diubah setelah dibuat.
- Oleh karena itu, tidak ada fungsi untuk menggabungkan dua tuple menjadi satu tuple.
- Namun, kita dapat membuat fungsi untuk menggabungkan dua tuple menjadi satu tuple.
- Fungsi tersebut akan mengembalikan tuple baru yang merupakan gabungan dari kedua tuple.
"""
