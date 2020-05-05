# soal 1
# x = [40, 100, 1, 5, 25, 10]
# x.sort()
# print(x)

# soal 2
# x = [40, 100, 1, 5, 25, 10]
# nilai_terkecil = min(x)
# nilai_tertinggi = max(x)
# print(nilai_terkecil)
# print(nilai_tertinggi)

# Soal 3

# tugas = []

# def menu():
#     print('1. isi array')
#     print('2. lihat array')
#     print('3. sort array ascending')
#     print('4. sort array descending')
#     print('5. nilai tertinggi & terendah')
#     print('6. jumlah ganjil dan genap')
#     print('7. keluar')
#     main_menu = int(input('pilih menu : '))
#     print(main_menu)

#     if main_menu == 1:
#         nilai = int(input("masukan berapa banyak jumlah angkanya : "))
#         for item in range(0, nilai):
#             print('silahkan masukin angka : ')
#             ele =int(input())
#             tugas.append(ele)
#     if main_menu == 2:
#         print('list nilai :')
#         print(tugas)
#     if main_menu == 3:
#         tugas.sort()
#         print('berikut list dari urutan terkecil : ')
#         print(tugas)
#     if main_menu == 4 :
#         tugas.sort(reverse=True)
#         print('berikut list dari urutan terbesae : ')
#         print(tugas)
#     if main_menu == 5 :
#         print('nilai tertinggi : ' +str(int(max(tugas))))
#         print('nilai terendah : ' +str(int(min(tugas))))
#     if main_menu == 6:
#         genap, ganjil = 0, 0
#         for y in tugas:
#             if y % 2 == 0:
#                 genap += 1
#             else:
#                 ganjil += 1
#         print('jumlah angka genap: ' +str(int(genap)))
#         print('jumlah angka ganjil: ' +str(int(ganjil)))
#     if main_menu == 7:
#         print(input(('Terima Kasih')))

#     menu()
# menu()

# CARA LAIN
# Fungsi sort

# def fungsi_sort_ascending(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr

# def fungsi_sort_descending(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] < arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr    

# # # Fungsi minimum maximum

# def minmax(list):
#     angka_min = fungsi_sort_ascending(list)[0]
#     angka_max = fungsi_sort_descending(list)[0]
#     return print('Nilai tertinggi {} dan nilai terendah {}'.format(angka_max,angka_min))

# # #Fungsi odd and even count

# def odd_even(list):
#     genap = 0
#     ganjil = 0
#     for i in list:
#         if i % 2 == 0:
#             genap += 1
#         else:
#             ganjil += 1    
#     return print('Jumlah angka ganjil ada {} dan angka genap ada {}'.format(ganjil, genap))

# # #Fungsi Insert Word to array
# def insert_word(list):
#     jumlah = int(input('Berapa kali memasukkan angka: '))
#     for l in range(jumlah):
#         a = int(input('Masukkan angka: '))
#         list.append(a)  


# # #Fungsi menu utama
# def menuarray():
#     x = []
#     pilihan = 1
#     while(pilihan < 6):
#         print ('Main menu \n')
#         print ('1. Isi Array' + '\n'+ '2. Lihat Array' + '\n'+ '3. Sort Array' + '\n'+ '4. Nilai tertinggi dan terendah' 
#             +'\n'+'5. Jumlah Ganjil dan Genap' + '\n'+ '6. Keluar')
        
#         pilihan = int(input('Piilh yang mana?: '))

#         if (pilihan == 1):
#             jumlah = int(input('Berapa kali memasukkan angka: '))
#             for l in range(jumlah):
#                 a = int(input('Masukkan angka: '))
#                 x.append(a)  

#         if (pilihan == 2):
#             print (x)

#         if (pilihan == 3):
#             c = int(input('1. Ascending' + '\n'+ '2. Descending' + '\n'+ 'Pilih yang mana: '))
#             if c == 2:       
#                 fungsi_sort_descending(x)
#             elif c == 1:
#                 fungsi_sort_ascending(x)
#             else: 
#                 print('Invalid input, coba lagi')
#                 pilihan = 1    

#         if (pilihan == 4):
#             minmax(x)
 
#         if (pilihan == 5):
#             odd_even(x)

#         if (pilihan == 6):
#             print('Terima kasih')

#         if (pilihan <= 0 or pilihan > 6):
#             print('Invalid input, coba lagi')
#             pilihan = 1
               
# menuarray()

# list_function = [insert_word, print, fungsi_sort_ascending, fungsi_sort_descending, minmax, odd_even]
# def menu_lain():
#     x = []
#     pilihan = 1
#     while(pilihan < 7):
#         print ('Main menu \n')
#         print ('1. Isi List' + '\n'+ '2. Lihat List' + '\n'+ '3. Sort List Ascending' + 
#                '\n'+ '4. Sort List Desscending' + '\n' +
#                 '5. Nilai tertinggi dan terendah' 
#                 +'\n'+'6. Jumlah Ganjil dan Genap' + '\n'+ '7. Keluar')
        
#         pilihan = int(input('Piilh yang mana?: '))      
#         if (pilihan == 7):
#             print('Terima kasih')
#         elif (pilihan <= 0 or pilihan > 6):
#             print('Invalid input, coba lagi')
#             pilihan = 2
#         else:
#             list_function[pilihan-1](x)    

# menu_lain()


