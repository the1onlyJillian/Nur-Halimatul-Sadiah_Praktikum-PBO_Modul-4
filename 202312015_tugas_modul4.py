from abc import ABC, abstractmethod

# 1. ABSTRACTION
class Pengguna(ABC):
    def __init__(self, nama): self.nama = nama
    @abstractmethod
    def akses(self): pass

# 4. CUSTOM EXCEPTION
class PoinTidakValidError(Exception): pass

# 2. SPECIAL METHODS
class Member(Pengguna):
    def __init__(self, nama, poin=0):
        super().__init__(nama)
        if poin < 0: raise PoinTidakValidError(f"Poin negatif: {poin}")
        self.poin = poin
    
    def akses(self): return "Akses Member tersedia"
    
    def __str__(self): return f"Member: {self.nama} – Poin: {self.poin}"
    def __add__(self, other): return self.poin + (other.poin if isinstance(other, Member) else other)
    def __len__(self): return len(self.nama)

# PROGRAM UTAMA (3 & 5)
if __name__ == "__main__":
    # Buat 2 Member
    m1 = Member("Andi", 100)
    m2 = Member("Budi", 150)
    
    # 5a. Info Member
    print("Info Member:")
    print(m1)  # __str__
    print(m2)
    print(f"Akses: {m1.akses()}")
    
    # 5b. Jumlah poin
    print(f"\nTotal poin: {m1 + m2}")  # __add__
    
    # 5c. Panjang nama
    print(f"\nPanjang nama:")
    print(f"Andi: {len(m1)} karakter")  # __len__
    print(f"Budi: {len(m2)} karakter")
    
    # 3 & 4. Exception Handling & Custom Exception
    print("\nUji Exception:")
    try:
        poin_input = input("Masukkan poin: ").strip()
        if not poin_input: raise ValueError("Input kosong!")  # 3
        poin = int(poin_input)  # 3 (ValueError jika bukan angka)
        if poin < 0: raise PoinTidakValidError("Poin < 0")  # 4 & 5d
        m3 = Member("Test", poin)
        print(f"Berhasil: {m3}")
    except ValueError as e: print(f"Error: {e}")
    except PoinTidakValidError as e: print(f"Error: {e}")