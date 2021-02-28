# Courser Prereq Scheduling
> Program to perform ordering on list of course and its prerequisites with Topological Sorting algorithm

Tugas Kecil 2 IF2211 Strategi Algoritma
Semester II tahun 2020/2021

## Algorithm
Algoritma decrease and conquer merupakan salah satu metode penyelesaian permasalahan secara komputasional. Algoritma ini bekerja dengan cara mereduksi persoalan menjadi sub-persoalan yang lebih kecil, kemudian memproses satu sub-persoalan itu saja.

Algoritma decrease and conquer memiliki tiga varian, salah satunya decrease by constant, artinya setiap iterasi, ukuran instance akan berkurang secara konstan. Salah satu contohnya adalah metode topological sort yang dalam kasus ini setiap iterasinya simpul berkurang satu buah, yaitu simpul berderajat masuk 0. Berikut adalah algoritma topological sort pada program ini.

1.	Representasikan daftar mata kuliah sebagai simpul pada graf berarah, dengan arah keluar menyatakan mata kuliah tersebut memiliki prasyarat yaitu simpul mata kuliah tujuan sisi berarah tersebut.
2.	Identifikasi simpul pada graf yang memiliki derajat masuk = 0, dalam kasus mata kuliah, artinya mata kuliah tersebut tidak memiliki prasyarat.
3.	Kemudian, hapus simpul tersebut pada graf dan sisi yang keluar dari simpul tersebut. Dalam kasus ini, misalkan simpul mata kuliah A berderajat masuk 0, maka simpul A akan dihapus dari graf dan seluruh mata kuliah yang tadinya memiliki prasyarat A sekarang tidak memiliki prasyarat A. Dengan demikian ukuran graph berkurang satu.
4.	Masukkan simpul yang terhapus pada container yang berisi daftar semester beserta mata kuliah tiap semester. Jika sudah ada simpul yang mengisi pada semester terkait, maka mata kuliah dapat ditempatkan pada satu semester yang sama.
5.	Ulangi langkah 2-4 untuk menemukan urutan mata kuliah per semesternya hingga graf kosong.

## System requirements
Make sure you have python installed in your device. Download python **[here](https://www.python.org/downloads/)**.

## How to use
1. Add or customize input text file in test folder 
2. Open src folder in terminal
3. Run main.py
```
    $ python 13519186.py
```

## Author
Alif Bhadrika Parikesit
13519186 / K-04