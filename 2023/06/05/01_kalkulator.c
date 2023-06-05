// Program C yang meminta pengguna untuk memasukkan dua bilangan bulat dan kemudian menampilkan hasil penjumlahan, pengurangan, perkalian, dan pembagian dari kedua bilangan tersebut.

#include <stdio.h>

// validasi input
int validasiInput(int input)
{
    while (input == 0)
    {
        printf("Input tidak boleh 0, silahkan masukkan kembali: ");
        scanf("%d", &input);
    }
    return input;
}

// opertor matematika
int tambah(int a, int b)
{
    return a + b;
}

int kurang(int a, int b)
{
    return a - b;
}

int kali(int a, int b)
{
    return a * b;
}

float bagi(int a, int b)
{
    return (float)a / b;
}

// meminta operator dari pengguna
char operator()
{
    char op;
    printf("Masukkan operator (+, -, *, /): ");
    scanf(" %c", &op);
    return op;
}

// menampilkan hasil
void hasil(int a, int b, char op)
{
    switch (op)
    {
    case '+':
        printf("%d + %d = %d\n", a, b, tambah(a, b));
        break;
    case '-':
        printf("%d - %d = %d\n", a, b, kurang(a, b));
        break;
    case '*':
        printf("%d * %d = %d\n", a, b, kali(a, b));
        break;
    case '/':
        printf("%d / %d = %.2f\n", a, b, bagi(a, b));
        break;
    default:
        printf("Operator tidak dikenali\n");
        break;
    }
}

int main()
{
    int a, b;
    char op;

    // meminta input dari pengguna
    printf("Masukkan bilangan pertama: ");
    scanf("%d", &a);

    // meminta operator dari pengguna
    op = operator();

    // meminta input dari pengguna
    printf("Masukkan bilangan kedua: ");
    scanf("%d", &b);

    // validasi input
    a = validasiInput(a);
    b = validasiInput(b);

    // menampilkan hasil
    hasil(a, b, op);

    // memberi opsi untuk mengulang program atau tidak
    char ulang;
    printf("Apakah anda ingin mengulang program? (y/n): ");
    scanf(" %c", &ulang);

    if (ulang == 'y' || ulang == 'Y')
    {
        main();
    }
    else
    {
        printf("Terima kasih telah menggunakan program ini\n");
    }

    return 0;
}