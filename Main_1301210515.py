# Daftar Fungsi
def bacadata(namafile):
    # (namafile).txt berisi input yang akan dibaca
    file = open(namafile, "r") 
    
    # Dicitonary Hari, Menyimpan data penjualan perpramuniaga
    dict_senin = {}
    dict_selasa = {}
    dict_rabu = {}
    dict_kamis = {}
    dict_jumat = {}    
    
    # Var teks berisi input yang dibaca perbaris
    teks = file.readline()
    
    # Input data dictionary sampai baris yang dibaca kosong(EOF)
    while teks != "" :
        # index 0 = nama, 1-5 = penjualan dari senin-jumat (FIXED INPUT)
        list_kata = teks.split() 
        
        # Dictionari hari berisi key = nama pramunaiga dan value = hasil penjualan perhari pramuniaga
        dict_senin[list_kata[0]] = list_kata[1]
        dict_selasa[list_kata[0]] = list_kata[2]
        dict_rabu[list_kata[0]] = list_kata[3]
        dict_kamis[list_kata[0]] = list_kata[4]
        dict_jumat[list_kata[0]] = list_kata[5]
        
        teks = file.readline()
    
    # Meminimalisi Eror
    file.close() 
    # List penjualan berisi dictionari penjualan yang dibentuk perhari
    dictionaryPenjualan = [dict_senin,dict_selasa,dict_rabu,dict_kamis,dict_jumat]
    return dictionaryPenjualan
def printdata(dictionaryPenjualan):
    # Agar output rapi (dioutputkan perhari)
    list_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
    
    i = 0 
    # Membaca semua dictionary hari yang terdapat pada dicitonary penjualan
    for dictionaryPenjualanPerhari in dictionaryPenjualan: 
        # Output Hari (Senin - Jumat)
        print("Hari",list_hari[i])
        # Membaca semua Nama yang terdapat pada dicitonary hari
        for pramuniaga in dictionaryPenjualanPerhari:
            # Output Nama dan penjualan pramuniaga pada hari tersebut
            print("Penjualan ",pramuniaga,"= ",dictionaryPenjualanPerhari[pramuniaga])
        print("\n")
        i += 1 
def penghasilan(namafile):
    
    # (namafile).txt berisi input yang akan dibaca
    file = open(namafile, "r")
    
    # Var teks berisi input yang dibaca perbaris
    teks = file.readline()
    
    # Menampung data dari pramuniaga dalam bentuk dictionary 
    listDicitonaryDataPramuniaga = []
    
    # Menampung data dari para Pramuniaga
    listDataPramuniaga = []
    
    # Selama baris yang dibaca bukan baris kosong(EOF), maka akan terus dilakukan
    # input data kedalam listDataPramuniaga per barisnya
    while teks != "" :
        listDataPramuniaga.append(teks.split())
        teks = file.readline()

    # Dictionary pada listDicitonaryDataPramuniaga dengan
    # key nama = nama, key penjualan = data penjualan perminggunya
    for dataPramunaiga in listDataPramuniaga:
        listDicitonaryDataPramuniaga.append({"nama":dataPramunaiga[0],"penjualan":dataPramunaiga[1:]}) 
        
    # Meminimalisir eror
    file.close()
    
    # Membaca semua dicitonary pramuniaga pada listDicitonaryDataPramuniaga
    for dataDictionaryPramuniaga in listDicitonaryDataPramuniaga:
        
        # Menampung Upah total upah mingguan dari pramuniaga
        upahPermingguTotal = [] 
        
        # Melakukan perhitungan upah harian dan insentif harian dari pramuniaga
        for penjualanPerhari in dataDictionaryPramuniaga.get("penjualan"):
            intPenjualanPerhari = int(penjualanPerhari) 
            
            # Pramuniaga akan memperoleh insentif jika pada hari tersebut ia berhasil menjual barang
            if intPenjualanPerhari != 0: 
                
                # total insentif ialah 2.5% dari penjualan perharinya
                insentif = (intPenjualanPerhari/40)
                upahPerhari = intPenjualanPerhari + insentif
                upahPermingguTotal.append(upahPerhari) 
                
        # Pramuniaga memperoleh upah mingguan sebesar 500 (ada/tidaknya penjualan)
        upahPerminggu = 500
        print("Penghasilan" ,dataDictionaryPramuniaga.get("nama"), "di Akhir Minggu =",sum(upahPermingguTotal) + upahPerminggu)
def bonus(namafile):
    # (namafile).txt berisi input yang akan dibaca
    file = open(namafile, "r")

    # Var teks berisi input yang dibaca perbaris
    dataPramuniagaDanPenjualan = file.readline()
    
    # List berisi data penjualan 
    listPenjualan = []
    # List berisi Nama pramuniaga dan penjualan
    listPramuniagaDanPenjualan = []
    
    # Membaca data Pramuniaga dan penjualan perbaris sesuai nama sampai baris kosong(EOF)
    while dataPramuniagaDanPenjualan != "" :
        # List pramuniaga dan penjualan berisi data pramuniaga
        # dan penjualan perNama
        listPramuniagaDanPenjualan.append(dataPramuniagaDanPenjualan.split())
        dataPramuniagaDanPenjualan = file.readline()
        
    # Menginput data Penjualan pernama sebagai dictionary ke dalam listPenjualan 
    # Data "nama" merupakan sebuah string dan data "penjualan" merupakan list data penjualan
    for pramuniagaDanPenjualan in listPramuniagaDanPenjualan:#Mengakses listkata dengan perulangan
        listPenjualan.append({"nama":pramuniagaDanPenjualan[0],"penjualan":pramuniagaDanPenjualan[1:]})
    
    # Meminimalisi eror
    file.close()
    
    # Melakulan perulangan untuk menghitung  total upah dari masing masing pramuniaga yang ada
    for dicitonaryDariListPenjualan in listPenjualan:
        # Menampung upah harian dan insentif harian dari masing masing pramuniaga yang ada
        upahHarianDanInsentifHarianTotal = [] 
        
        # Melakukan perhitungan insentif dari  penjualan perhari para pramuniaga
        for dataPenjualan in dicitonaryDariListPenjualan.get("penjualan"): 
            penjualanPerHari = int(dataPenjualan)
            
            # Pramuniaga tidak akan mendapatkan insentif jika penjualan = 0 (tidak ada penjualan pada hari tersebut)
            if penjualanPerHari != 0:
                
                # Penhitungan insentif sebesar 2.5% (seuai soal)
                insentif = (penjualanPerHari/40)
                upahHarianDanInsentifHarian = penjualanPerHari + insentif 
                upahHarianDanInsentifHarianTotal.append(upahHarianDanInsentifHarian) 
        
        # Upah perminggu dari masing-masing pramuniaga ada 500 (sesuai soal)
        upahPerminggu = 500
        # Upah perminggu yang diterima masing masing pramuniaga
        upahTotal = sum(upahHarianDanInsentifHarianTotal) + upahPerminggu
        
        # Bonus diberikan kepada pramuniaga yang memiliki nilai penjualan mingguan lebih dari 20000
        if upahTotal > 20000 : 
            print("Yang mendapat bonus minggu ini :" ,dicitonaryDariListPenjualan.get("nama")) 
            # Bonus yang diberikan ialah sebesar 1000
            print("Besar penghasilan",dicitonaryDariListPenjualan.get("nama") ,"setelah ditambahkan oleh bonus = ",upahTotal + 1000)

# Main Program
namafile = "maininput.txt" 
dictionaryPenjualan = bacadata(namafile) 
printdata(dictionaryPenjualan) 
penghasilan(namafile)
print() 
bonus(namafile)
print()