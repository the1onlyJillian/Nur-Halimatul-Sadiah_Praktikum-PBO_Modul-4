class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
    
    def __str__(self):
        return f"Nama: {self.nama}, nilai: {self.nilai}"
    
    def __gt__(self, other):
        return self.nilai > other.nilai
    
    def __add__(self, other):
        return self.nilai + other.nilai
    
    def __mul__(self, faktor):
        return self.nilai * faktor
    
    #Method __len__ untuk mengembalikan panjang nama
    def __len__(self):
        return len(self.nama)
    
    #Method __eq__ untuk menyatakan dua mahasiswa sama jika nilainya sama
    def __eq__(self, other):
        return self.nilai == other.nilai

# Control penggunaan
a = Mahasiswa("Pouster", 80)
b = Mahasiswa("Ahmad", 90)

print(a)
print(b)

if b > a:
    print(f"{b.nama} memiliki nilai lebih tinggi")

print("Total nilai:", a + b)
print("Nilai Ahmad x 2 =", b * 2)

#Membuat 2 objek tambahan
c = Mahasiswa("Budi", 85)
d = Mahasiswa("Citra", 80)  # Nilai sama dengan Pouster

print("\n=== Implementasi ===")
print()

#Representasi string (print(obj))
print("1. Representasi string:")
print(f"Mahasiswa c: {c}")
print(f"Mahasiswa d: {d}")
print()

#Menggunakan __len__ untuk mendapatkan panjang nama
print("2. Panjang nama mahasiswa:")
print(f"Panjang nama '{a.nama}': {len(a)} karakter")
print(f"Panjang nama '{b.nama}': {len(b)} karakter")
print(f"Panjang nama '{c.nama}': {len(c)} karakter")
print(f"Panjang nama '{d.nama}': {len(d)} karakter")
print()

#Perbandingan kesetaraan nilai menggunakan ==
print("3. Perbandingan kesetaraan nilai:")
print(f"Apakah {a.nama} (nilai: {a.nilai}) sama dengan {d.nama} (nilai: {d.nilai})? {a == d}")
print(f"Apakah {a.nama} (nilai: {a.nilai}) sama dengan {b.nama} (nilai: {b.nilai})? {a == b}")
print(f"Apakah {c.nama} (nilai: {c.nilai}) sama dengan {b.nama} (nilai: {b.nilai})? {c == b}")
print()

#Operasi matematika seperti m1 + m2 dan m1 * 2
print("4. Operasi matematika:")
print(f"Total nilai {a.nama} + {c.nama}: {a + c}")
print(f"Total nilai {b.nama} + {d.nama}: {b + d}")
print(f"Nilai {c.nama} x 3: {c * 3}")
print()

#Mengurutkan list mahasiswa berdasarkan nilai menggunakan sorted dengan key
print("5. Mengurutkan mahasiswa berdasarkan nilai (terendah ke tertinggi):")
list_mahasiswa = [a, b, c, d]
mahasiswa_terurut = sorted(list_mahasiswa, key=lambda x: x.nilai)

for i, mhs in enumerate(mahasiswa_terurut, 1):
    print(f"{i}. {mhs.nama}: {mhs.nilai}")