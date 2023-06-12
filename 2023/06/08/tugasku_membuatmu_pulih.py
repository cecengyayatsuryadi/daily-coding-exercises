def main():
    # Inisialisasi variabel
    diriku = None
    dia = None

    # Input pilihan dari user
    pilihan = input("Pilih aku atau dia: (aku/dia)\n")

    # Evaluasi kondisi
    if pilihan == "aku":
        diriku = True
        print("Kamu memilih aku.")
        print("Jika kamu memilih aku, aku akan senang.")
    elif pilihan == "dia":
        dia = True
        print("Kamu memilih dia.")
        print("Jika kamu memilih dia, aku tidak masalah.")
    else:
        print("Kamu belum memilih siapa-siapa.")

    # Tampilkan pesan cinta
    if diriku:
        print("Akan kujaga kamu seumur hidupku")
    if dia:
        print("Tugasku membuatmu pulih.")


if __name__ == "__main__":
    main()
