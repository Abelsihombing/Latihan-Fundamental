# # PR moivie
def printMenu():
    print('\n\nMenu: \n1. Pesan Tiket\n2. Lihat History\n3. Keluar')

def printFilm():
    print('\nList Film\n1. The Incredibles\n2. Toy Story')

def printPilihJadwal(x):
    print('\nPilih Jadwal film ' + x + ': ')
    print('1. Siang\n2. Malam')

# def printRow(Row1,Row2):
#     modif = ['      ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#     print('Tempat Duduk(X)')

#     for a in modif:
#         print(a,end=' ')
#     print('')
#     for i in Row1:
#         print(i, end=' ')
#     print('')
#     for j in Row2:
#         print(j, end = ' ')
#     print('')

def pilihDuduk(ListRow1, ListRow2, judulfilm):
    i = 0
    inputPesan = int(input('\nPesan Tiket Berapa kali: '))
    
    while(i<inputPesan):
        inputRow = int(input('Row (1-2): '))
        inputSeat = int(input('Seat (1-10): '))
        
        if(inputRow==1):      
            if(ListRow1[inputSeat]=='O'):
                ListRow1[inputSeat] = 'X'
                i+=1
            else:
                print ('Tempat Duduk Tidak tersedia\n')
        elif(inputRow==2):      
            if(ListRow2[inputSeat]=='O'):
                ListRow2[inputSeat] = 'X'
                i+=1
            else:
                print ('Tempat Duduk Tidak tersedia\n')
        else:
            print ('Row hanya 2, silahkan coba lagi!\n')    
    # printRow(ListRow1,ListRow2)
    modif = ['      ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    print(' '.join(modif))
    print(' '.join(ListRow1))
    print(' '.join(ListRow2))

i = True
row1_Film1_siang = ['Row1: ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']   
row2_Film1_siang = ['Row2: ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']   
row1_Film1_malam = ['Row1: ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
row2_Film1_malam = ['Row2: ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
row1_Film2_siang = ['Row1: ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']   
row2_Film2_siang = ['Row2: ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
row1_Film2_malam = ['Row1: ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
row2_Film2_malam = ['Row2: ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
history = []

while(i == True):
    printMenu()
    inputMenu = int(input('Tentukan pilihan: '))
    
    if (inputMenu == 1):       
        printFilm()
        inputFilm = int(input('Silahkan pilih Film: '))
        
        if (inputFilm == 1):
            printPilihJadwal('The Incredibles')
            inputSiangMalam = int(input('Pilihan: '))
            if(inputSiangMalam==1):
                pilihDuduk(row1_Film1_siang, row2_Film1_siang, 'The Incredibles')
            elif(inputSiangMalam==2):
                pilihDuduk(row1_Film1_malam, row2_Film1_malam, 'The Incredibles')
            else:
                print('Salah input Jadwal!')
                continue

        elif (inputFilm == 2):
            printPilihJadwal('Toy Story')
            inputSiangMalam = int(input('Pilihan: '))
            if(inputSiangMalam==1):
                pilihDuduk(row1_Film2_siang, row2_Film2_siang, 'Toy Story')
            elif(inputSiangMalam==2):
                pilihDuduk(row1_Film2_malam, row2_Film2_malam, 'Toy Story')
            else:
                print('Salah input Jadwal!')
                continue
        else:
            print('Salah input Film!')
    
    if(inputMenu == 3):
        print('\nTerima Kasih!')
        i = False

# # Cara 2
# film = {1:'The Incredibles', 2:'Toy Story'}
# jadwal = {1: 'Siang', 2: 'Malam'}
# kursi_history = {}

# for i in film.values():
#     for j in jadwal.values():
#         kursi_history[i+j]= 0
# history = {}

# def kursi():
#     c = []
#     for i in range(2):
#         d = []
#         for j in range(10):
#             d.append('O')
#         c.append(d)
#     return c
#     [['o', 'o', 'o'],
#      ['o', 'o', 'o']]

# def pesan_tiket():
#     print('List film:\n1. The Incredibles\n2. Toy Story')
#     while(True):
#         pilih_film = int(input('Silahkan Pilih Film: '))
#         if pilih_film == 1 or pilih_film == 2:
#             break
#     while(True):
#         pilih_jadwal = int(input('Pilih Jadwal Film {}:\n1. Siang\n2. Malam\nPilihan:'.format(film[pilih_film])))
#         if pilih_jadwal == 1 or pilih_jadwal == 2:
#             break
#     while(True):
#         tiket_kali = int(input('Pesan Tiket Berapa Kali: '))
#         if tiket_kali > 0 or tiket_kali <= 20:
#             break
    
#     def pesan_kursi(kali):
#         for i in range(kali):
#             row = int(input('Row: '))
#             seat = int(input('Seat: '))
#             try:
#                 if kursi_history[film[pilih_film] + jadwal[pilih_jadwal]][row-1][seat-1] == 'O':
#                     kursi_history[film[pilih_film] + jadwal[pilih_jadwal]][row-1][seat-1] = 'X'
#                 else:
#                     print('Kursi Tidak Tersedia')
#             except:
#                 print('Salah Input')
            
#             j = ''
#             for k in range(2):
#                 for l in kursi_history[film[pilih_film] + jadwal[pilih_jadwal]][k]:
#                     j+=l
#                 j += '\n'
#             history[film[pilih_film] + jadwal[pilih_jadwal] + str(row) + str(seat)] = [film[pilih_film], jadwal[pilih_jadwal],row,seat]
#             print('Tempat Duduk\n'+j)
    
#     if kursi_history[film[pilih_film] + jadwal[pilih_jadwal]] == 0:
#         kursi_history[film[pilih_film] + jadwal[pilih_jadwal]] = kursi()
#         pesan_kursi(tiket_kali)
#     else:
#         pesan_kursi(tiket_kali)

# def lihat_history():
#     # {'the incredibles11': ['the incredibles', 'siang', 1,1]}\
#     for i in history.values():
#         # print('Film{jadwal} Jadwal {film} seat {seat} Row {row}'.format(film =i[0], jadwal=i[1], seat = 1[2], row = i[3]))
#         print(f"Film {i[0]} Jadwal {i[1]}")

# while(True):
#     pilih = int(input('Menu:\n1. Pesan Tiket\n2. Lihat History\n3. Keluar\nTentukan pilihan:'))
#     if pilih == 1:
#         pesan_tiket()
#     elif pilih == 2:
#         lihat_history()
#     elif pilih == 3:
#         break   
