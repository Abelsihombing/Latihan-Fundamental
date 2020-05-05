# ## Soal 1
# History = [] 
# class Bikinmenu():
#     def __init__(self,nama, menu,harga):
#         self.name = nama
#         self.Menu = menu
#         self.Harga = harga

#     def get_menu(self):
#         for i in range(len(self.Menu)):
#           print('{}. {} Harganya adalah {}'.format(i+1, self.Menu[i], self.Harga[i]))
#         print('\n')

#     def menu_price(self):
#         pilih = int(input('mau beli yang mana ? : '))
#         if pilih == 1:
#             print('{} telah membeli {} dengan harga {}'.format(self.name, self.Menu[0], self.Harga[0]))
#         if pilih == 2:
#             print('{} telah membeli {} dengan harga {}'.format(self.name, self.Menu[1], self.Harga[1]))
#         if pilih == 3:
#             print('{} telah membeli {} dengan harga {}'.format(self.name, self.Menu[2], self.Harga[2]))
#         History.append(self.Menu[pilih-1])  

#     def get_history(self):
#         z = self.name + ' telah membeli'
#         for i in range(len(History)):
#             z += ' '+ History[i]
#             if len((History))>2 and (i != (len(History)-1)):
#                 z += ' , '
#             if (i == (len(History)-2)) and (len(History) != 1):
#                 z += ' dan '
#         print(z)

# Paul = Bikinmenu('Paul',['Ayam Goreng','Nasi Bakar','Sate Kambing'], [1000, 2000, 3000])   

# Paul.get_menu()
# Paul.menu_price()
# Paul.get_history()
# Paul.get_menu()
# Paul.menu_price()
# Paul.get_history()
# Paul.get_menu()
# Paul.menu_price()
# Paul.get_history()
# Paul.get_menu()
# Paul.menu_price()
# Paul.get_history()

# Soal 2
# import random
# class ramal:
#     def __init__(self, money):
#         self.uang = money

#     def menu(self):
#         x = True
#         while (x == True):
#             print('Pilih Ramalan Anda :')
#             print('1. Ramalan Pekerjaan')
#             print('2. Ramalan Kesehatan')
#             print('3. Ramalan Percintaan')
#             print('4. Keluar')
#             pilih = int(input('Masukkan Pilihan : '))

#             if(self.uang < 10000):
#                 parameter = [['Sangat Buruk', 'Buruk','Biasa Saja'],['Baik'],['Sangat baik']]
#                 Probabilty = [0.8, 0.1, 0.1]
#                 Prob1 = random.choices(parameter,Probabilty)
#                 prob2 = random.choices(Prob1[0])
#                 final1 = prob2[0]

#             elif(self.uang > 10000 and self.uang < 50000):
#                 parameter = [['Sangat Buruk', 'Buruk','Biasa Saja'],['Baik'],['Sangat baik']]
#                 Probabilty = [0.8, 0.1, 0.1]
#                 Prob1 = random.choices(parameter,Probabilty)
#                 prob2 = random.choices(Prob1[0])
#                 final1 = prob2[0]

#             elif(self.uang > 50000):
#                 parameter = [['Sangat Buruk', 'Buruk','Biasa Saja'],['Baik'],['Sangat baik']]
#                 Probabilty = [0.8, 0.1, 0.1]
#                 Prob1 = random.choices(parameter,Probabilty)
#                 prob2 = random.choices(Prob1[0])
#                 final1 = prob2[0]

#             if (pilih == 1):
#                 print(' Hasil Ramalan Anda {} ' .format(final1))
#             elif (pilih == 2):
#                 print('Hasil Ramalan Anda {} ' .format(final1))
#             elif (pilih == 3):
#                 print(' Hasil Ramalan Anda {} ' .format(final1))
#             elif (pilih == 4):
#                 print('Terima Kasih')
#                 x = False

# a = ramal(150000)
# a.menu()