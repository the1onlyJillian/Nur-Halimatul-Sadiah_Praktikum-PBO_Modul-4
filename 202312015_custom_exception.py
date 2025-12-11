class UmurTidakValidError(Exception):
    """Kesalahan untuk umur yang tidak masuk akal."""
    pass

class UmurTerlaluMudaError(UmurTidakValidError):
    """Kesalahan untuk umur yang terlalu muda."""
    pass

class UmurTerlaluTuaError(UmurTidakValidError):
    """Kesalahan untuk umur yang terlalu tua."""
    pass

class AkunTidakDiizinkanError(Exception):
    """Kesalahan untuk pendaftaran akun yang tidak diizinkan."""
    pass

def set_umur(umur):
    #Validasi umur terlalu muda (< 5)
    if umur < 5:
        raise UmurTerlaluMudaError(f"Umur {umur} tahun terlalu muda! Minimum 5 tahun.")
    
    # Validasi umur negatif
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    
    #Validasi umur terlalu tua (> 100)
    if umur > 100:
        raise UmurTerlaluTuaError(f"Umur {umur} tahun terlalu tua! Maksimum 100 tahun.")
    
    # Validasi umur terlalu besar (tetap dipertahankan)
    if umur > 150:
        raise UmurTidakValidError("Umur terlalu besar, periksa kembali input.")
    
    return umur

def daftar_akun(umur):
    """POIN E: Fungsi untuk mendaftar akun hanya untuk umur 18 ke atas"""
    if umur < 18:
        raise AkunTidakDiizinkanError(f"Umur {umur} tahun tidak cukup untuk membuat akun. Minimum 18 tahun.")
    
    return f"Akun berhasil dibuat untuk pengguna berumur {umur} tahun."

def main():
    print("=== PROGRAM VALIDASI UMUR ===")
    print("Validasi umur: 5 - 100 tahun")
    print("Daftar akun: 18 tahun ke atas")
    print("-" * 40)
    
    #Loop hingga mendapatkan input yang valid
    while True:
        try:
            input_str = input("\nMasukkan umur (atau 'keluar' untuk berhenti): ").strip()
            
            if input_str.lower() == 'keluar':
                print("Program dihentikan.")
                break
            
            u = int(input_str)
            umur = set_umur(u)
            
            print(f"✓ Umur {umur} tahun valid!")
            
            # POIN E: Coba daftar akun
            try:
                hasil_daftar = daftar_akun(umur)
                print(f"✓ {hasil_daftar}")
            except AkunTidakDiizinkanError as e:
                print(f"✗ {e}")
            
            # Tanyakan apakah ingin melanjutkan
            lanjut = input("\nApakah ingin memasukkan umur lagi? (ya/tidak): ").strip().lower()
            if lanjut != 'ya':
                print("Terima kasih telah menggunakan program!")
                break
                
        except ValueError:
            print("✗ Input harus berupa bilangan bulat!")
        
        except UmurTerlaluMudaError as e:
            print(f"✗ {e}")
        
        except UmurTerlaluTuaError as e:
            print(f"✗ {e}")
        
        except UmurTidakValidError as e:
            print(f"✗ {e}")
        
        except Exception as e:
            print(f"✗ Terjadi kesalahan tak terduga: {e}")

if __name__ == "__main__":
    # POINT A: Demonstrasi custom exception bekerja
    print("\n=== DEMONSTRASI CUSTOM EXCEPTION ===")
    
    test_cases = [
        ("Umur negatif", -5),
        ("Umur terlalu muda", 3),
        ("Umur valid muda", 7),
        ("Umur valid dewasa", 25),
        ("Umur terlalu tua", 120),
        ("Umur ekstrem", 200),
    ]
    
    for desc, umur_test in test_cases:
        print(f"\nTest: {desc} ({umur_test} tahun)")
        print("-" * 30)
        try:
            result = set_umur(umur_test)
            print(f"✓ Berhasil: Umur {result} tahun valid")
            
            # Test daftar akun
            try:
                akun_result = daftar_akun(result)
                print(f"✓ {akun_result}")
            except AkunTidakDiizinkanError as e:
                print(f"✗ {e}")
                
        except (UmurTidakValidError, UmurTerlaluMudaError, UmurTerlaluTuaError) as e:
            print(f"✗ {e}")
    
    print("\n" + "="*50)
    
    # Jalankan program interaktif
    main()