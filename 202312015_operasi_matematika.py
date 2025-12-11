def operasi():
    print("=== Operasi Matematika Dasar ===")
    print("Pilih operasi:")
    print("1. Pembagian")
    print("2. Perkalian")
    
    pilihan = input("Masukkan pilihan (1/2): ").strip()
    
    #Validasi input pilihan tidak boleh kosong
    if pilihan == "":
        print("Error: Pilihan operasi tidak boleh kosong!")
        return
    
    x = input("Masukkan angka pertama: ").strip()
    y = input("Masukkan angka kedua: ").strip()
    
    try:
        #Validasi input tidak boleh kosong dengan pesan khusus
        if x == "":
            raise ValueError("Error: Angka pertama tidak boleh kosong!")
        if y == "":
            raise ValueError("Error: Angka kedua tidak boleh kosong!")
        
        a = float(x)
        b = float(y)
        
        #Validasi bilangan harus positif dengan pesan error yang sesuai
        if a < 0:
            raise ValueError("Error: Angka pertama tidak boleh negatif! Hanya angka positif yang diperbolehkan.")
        if b < 0:
            raise ValueError("Error: Angka kedua tidak boleh negatif! Hanya angka positif yang diperbolehkan.")
        
        if pilihan == "1":
            # PEMBAGIAN
            hasil = a / b  # dapat menyebabkan ZeroDivisionError
            operasi_str = "pembagian"
        elif pilihan == "2":
            # PERKALIAN
            hasil = a * b
            operasi_str = "perkalian"
        else:
            raise ValueError("Error: Pilihan operasi tidak valid. Gunakan 1 atau 2.")
        
    except ValueError as e:
        print(e)
    
    except ZeroDivisionError:
        print("Error: Penyebut tidak boleh nol pada operasi pembagian!")
    
    except Exception as e:
        print("Terjadi kesalahan:", e)
    
    else:
        #Hanya berjalan jika tidak ada exception
        print(f"Hasil {operasi_str} {a} dengan {b} adalah: {hasil}")
    
    finally:
        #Selalu berjalan
        print("Selesai memproses input.")
        print("-" * 50)


if __name__ == "__main__":
    #Uji program untuk berbagai skenario
    
    print("\n" + "="*60)
    print("UJI PROGRAM BERBAGAI SKENARIO")
    print("="*60 + "\n")
    
    # Simulasi input untuk berbagai skenario
    skenario = [
        # Skenario 1: Pilih pembagian input kedua angka valid (contoh: 10 dan 2)
        {"nama": "Pembagian angka valid (10/2)", "input": ["1", "10", "2"]},
        
        # Skenario 2: Pilih pembagian penyebut = 0 (contoh: 10 dan 0)
        {"nama": "Pembagian dengan penyebut 0 (10/0)", "input": ["1", "10", "0"]},
        
        # Skenario 3: Pilih perkalian kedua angka valid (contoh: 5 dan 4)
        {"nama": "Perkalian angka valid (5*4)", "input": ["2", "5", "4"]},
        
        # Skenario 4: Input kosong pada salah satu masukan
        {"nama": "Input kosong pada angka pertama", "input": ["1", "", "5"]},
        {"nama": "Input kosong pada angka kedua", "input": ["2", "5", ""]},
        {"nama": "Pilihan operasi kosong", "input": ["", "5", "4"]},
        
        # Skenario 5: Input angka negatif
        {"nama": "Angka pertama negatif", "input": ["1", "-5", "3"]},
        {"nama": "Angka kedua negatif", "input": ["2", "5", "-3"]},
        {"nama": "Kedua angka negatif", "input": ["1", "-5", "-3"]},
    ]
    
    for idx, sken in enumerate(skenario, 1):
        print(f"\nSkenario {idx}: {sken['nama']}")
        print("-" * 40)
        
        # Simulasi input dengan mengganti fungsi input
        import sys
        from io import StringIO
        
        # Simpan input asli
        original_input = __builtins__.input
        
        # Buat input simulasi
        def mock_input(prompt=""):
            return sken['input'].pop(0)
        
        # Ganti fungsi input dengan mock
        __builtins__.input = mock_input
        
        try:
            operasi()
        finally:
            # Kembalikan fungsi input asli
            __builtins__.input = original_input
    
    # Contoh interaksi manual
    print("\n" + "="*60)
    print("CONTOH INTERAKSI MANUAL")
    print("="*60 + "\n")
    
    # Reset untuk interaksi manual
    operasi()