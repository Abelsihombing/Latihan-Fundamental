# # # Soal 1
# list_kata = ['Merdeka', 'Hello' , 'Hellos', 'Hohib', 'Kari ayam']
# print(list_kata)
# i = input('search : ')
# print(list(filter(lambda x: i in x.lower(), list_kata)))

# Cara 2 from Cornel
# #Duplikat Filter
# def filterlist(function,list_container):
#     hasil = []
#     for i in list_container:
#         if function(i):
#             hasil.append(i)
#     return hasil

# # #Duplikat Map
# def maplist(function,list_container):
#     hasil =[]
#     for item in list_container:
#         hasil.append(function(item))
#     return hasil


# list_kata=['Merdeka', 'Hello', 'Hellos', 'sohib', 'Kari Ayam']

# # print(maplist(lambda x: x.capitalize(), list_kata))
# # print(filterlist(lambda x: 'H' in x, list_kata))

# # Soal 2

# num0 = [' __  ',
#         '|  | ',
#         '|__| ']
# num1 = ['     ',
#         '   | ',
#         '   | ']
# num2 = [' __  ',
#         ' __| ',
#         '|__  ']
# num3 = ['___  ',
#         '___| ',
#         '___| ']
# num4 = ['     ',
#         '|__| ',
#         '   | ']
# num5 = [' __  ',
#         '|__  ',
#         ' __| ']
# num6 = [' __  ',
#         '|__  ',
#         '|__| ']
# num7 = [' __  ',
#         '   | ',
#         '   | ']
# num8 = [' __  ',
#         '|__| ',
#         '|__| ']
# num9 = [' __  ',
#         '|__| ',
#         ' __| ']

# number = [num0 , num1 , num2 , num3 , num4 , num5 , num6 , num7 , num8 , num9]
# num = input('masukkan angka : ')
# list_number = num.split(' ')
# print(list_number)

# baris1 = ' '
# for item in list_number :
#     baris1 += number[int(item)][0]
# print(baris1)

# baris2 = ' '
# for item in list_number :
#     baris2 += number[int(item)][1]
# print(baris2)

# baris3 = ' '
# for item in list_number:
#     baris3 += number[int(item)][2]
# print(baris3)






