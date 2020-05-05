# # # soal 1
# x = 4
# y = 3
# z = 2
# w = (((x+y*z)/x*y)**z)
# print(w)

# # soal 2
# number1 = int(input('masukan angka berapa aja : '))
# print('hasilnya adalah : ' + str(int(number1 ** 2))) 
# print("kuadrat dari "+ str(angka) + "=" +str(angka**2))

# # soal 3
# x = 485
# tahun = ( x/360)
# bulan = ( x/30)
# minggu = ( (x*48)/360 )
# print('tahunnya : ' +str(int(round(tahun))))
# print('bulannya : ' +str(int(round(bulan))))
# print('minggunya : ' +str(int(round(minggu))))

# Cara 2 From Cornel
# import math
# total_hari1 = int(input('Masukkan Hari : '))
# years = str(math.floor(total_hari1/360))
# month = str(math.floor(total_hari1 % 360) // 30)
# week = str(math.floor(((total_hari1 % 360) %30)/7))
# day = str(math.floor(((total_hari1 % 360)%30)%7))
# print(years + ' tahun, ' + month + ' bulan, ' + week + ' minggu, ' + day + ' hari')

# # # soal 4
# x = 49
# rasio = 0.4
# RasioAndi = 2
# RasioBudi = 5
# jumlahumur = int(x/(RasioAndi+RasioBudi))
# print('umur Andi 2 tahun : ' +str(int(jumlahumur*RasioAndi)+2))
# print('umur Budi 2 tahun : ' +str(int(jumlahumur*RasioBudi)+2))

# Cara 2 from cornel
# total = int(input('Total Umur = '))
# rasio = float(input('Rasio Umur X : Y = '))
# umurY = (total * 10)/(10 + (rasio*10))
# umurX = total - umurY
# print(umurX + 2)
# print(umurY + 2)

# ## soal 5
# kalimat = input('nama kalimat : ')
# huruf = input('huruf apa : ')
# print('jumlah kalimat yang dicari : ' +str(kalimat.count(huruf)))

# # cara 2 ??
# word = input('kata :')
# cari = input('karakter yg dicari :')
# print(int(len(word.split(cari)))-1)

# # soal 6
# from math import floor
# S = 120
# Va = 60
# Vb = 40
# jam1 = 9
# T2 = (S/(Va+Vb))
# jam2 = floor(T2)
# menit1 = 0
# menit2 = (T2-jam2)*60
# print(int(jam1*100+jam2*100+menit1+menit2))

#cara 2

# ## soal github 1
# x = int(input('input : '))
# print('output = ')
# print(((x%100)*100) + (x//100))

# cara 2
# a = int(input('masukan angka : '))
# print('Output : {} '.format(a%100*100 + a // 100))

# # soal github 2
# from math import pi
# radius = 12
# Luas = pi*radius**2
# print(Luas)

# ## cara 2
# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# ## soal github 3
# x = int(input('Masukkan 2 angka pertama: '))
# y = int(input('Masukkan 2 angka kedua: '))
# a = x // 10
# b = x % 10
# c = y // 10
# d = y % 10
# print(a * 1000 + c * 100 + b * 10 + d )

# ## soal github 4
# x = input('masukkan kata : ')
# y = input('kata mana yang mau dihilangkan :' )
# print('output : ' + (x.replace(y, '')))

# soal github 5
x = input('masukkan kata : ')
lis = x.split()
print(lis)
print(lis[1] +' '+ lis[0])

# No6
# import math

# jarak_dalam_km = int(input("Jarak antara kendaraan?: "))
# kecepatan_a_km_per_h = int(input("Kecepatan kendaraan a?: "))
# kecepatan_b_km_per_h = int(input("Kecepatan kendaraan b?: "))
# jam_berangkat = int(input('Jam Berangkat?: '))
# menit_berangkat = int(input('Menit Berangkat?: '))

# waktu_tabrakan_dalam_menit = (
#     jarak_dalam_km/(kecepatan_a_km_per_h + kecepatan_b_km_per_h))*60
# print(str(waktu_tabrakan_dalam_menit) + ' menit')

# jam = math.floor(waktu_tabrakan_dalam_menit/60) + jam_berangkat
# menit = (menit_berangkat + (waktu_tabrakan_dalam_menit%60)) % 60

# print('Waktu A & B bertabrakan adalah jam {}.{} WIB'.format(int(jam), int(menit)))
# #jam 10.12 WIB




