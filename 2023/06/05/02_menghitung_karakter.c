// Buat program C yang meminta pengguna untuk memasukkan sebuah string dan kemudian menampilkan jumlah karakter dalam string tersebut.

#include <stdio.h>

// menghitung karakter
int hitungKarakter(char *str)
{
    int i = 0;
    while (str[i] != '\0')
    {
        i++;
    }
    return i;
}

// program utama
int main()
{
    // deklarasi variabel
    char str[100];

    // input
    printf("Masukkan sebuah string: ");
    scanf("%s", str);

    // hitung jumlah karakter
    int jumlahKarakter = hitungKarakter(str);

    // output
    printf("Jumlah karakter: %d\n", jumlahKarakter);

    // opsi mengulang atau keluar
    char opsi;
    printf("Ulangi? (y/n) ");
    scanf(" %c", &opsi);
    if (opsi == 'y' || opsi == 'Y')
    {
        main();
    }
    else
    {
        printf("Terima kasih.\n");
        return 0;
    }

    return 0;
}

// catatan: untuk menghitung jumlah karakter dalam sebuah string, kita dapat menggunakan fungsi strlen() yang terdapat dalam library string.h. Namun, untuk memahami konsep perulangan, kita akan membuat fungsi sendiri untuk menghitung jumlah karakter dalam sebuah string.