saldoAwal = 0

print('===SELAMAT DATANG DI KOPERASI SIMPAN PINJAM===')

## Landing Page
# Registrasi akun 
tanya  = input('Masukkan pilihan Anda [ create / login ] :')

if tanya == 'create' :
    akun = input('Masukkan nama akun :')
    password = input('Masukkan password  :')

    akunUlang = input('Masukkan nama akun anda sekali lagi :')
    passwordUlang = input('Masukkan password anda sekali lagi  :')

    if akun == akunUlang :
        if password == passwordUlang :
            print('Akun berhasil dibuat')
        else :
            print('Password anda salah !')
    else :
        print('Akun anda tidak terdaftar') 
elif tanya == 'login' :
    akun1 = 'segarnapitupulu'
    password1 = 'segar1234'
    limitSalah = 3
    
    for i in range(limitSalah) : 
        akunn = input('Masukkan nama akun :')
        passwordd = input('Masukkan password  :')
        limitSalah -= 1
    
        if akunn == akun1 :
            if passwordd == password1 :
                print('Akun berhasil login !')
                break
            else :
                print('Password anda salah !')
        else :
            print('Akun anda salah !')
        
        if limitSalah == 0 :
            print('Anda telah diblokir !')
            break
else :
    print('Anda memasukkan pilihan yang salah !')
    exit()
    
print('Halo', akun, ',')
# Saldo
if tanya == 'create' :
    saldoAwal += 100000 # Simpanan pokok : pembayaran wajib yang dilakukan untuk menjadi member dan tidak dapat ditarik selama jadi anggota
elif tanya == 'login' :
    saldoAwal = 300000 # Saldo yang sudah berada di akun user
    
# Transaksi
i = 0
while i >= 0 :
    transaksi = input('Anda ingin melakukan transaksi apa [ simpanan, pinjaman, penarikan, cicilan ] ?')
    
    # Simpanan
    
    
            
            
    tanya2 = input('Apakah anda ingin melakukan transaksi lain lagi [ yes / no ] ?')
            
    if tanya2 == 'yes' :
        i += 1
    else :
        break
            