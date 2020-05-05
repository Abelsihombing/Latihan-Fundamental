# soal 1
# z = ''
# for item in range(5):
#     for item1 in range(item-1, 4):
#         z += ' * '
#     z += ' \n'
# print(z)

# # soal 2
# z = ''
# for item in range(5,1,-1):
#     for item1 in range(0,item):
#         z += ' * '
#     if item>2:
#         z += '\n'
# y = ''
# for item2 in range(5):
#     for item3 in range(0,item2+1):
#         y += ' * '
#     y += '\n'
# print(z)
# print(y)

# # #soal 3
# angka = 19
# for item in range(0,angka,+2):
#         print("-"*(angka-1-item)+"* "*(item+1))

# cara 2
# z = ''
# for i in range(0,10,1):
#     for j in range(0,21):
#         if j >= 10-i and j <= 10+i :
#             z += '* '
#         else :
#             z += '- '
#     z += '\n'
# print(z)


# # # ## soal 4
# angka = 19
# for item in range(0,angka,+2):
#     if item <= angka:
#         print(" "*(item+1)+"* "*(angka-item))

# # soal 5
# angka = 9
# for item in range(0,angka,+2):
#     if item <= angka:
#         print(" -"*(angka+1-item)+"  * "*(item+1))
# for item in range(0,angka,+2):
#         print(" -"*(item+1)+  "  * "*(angka-item))

# soal bonus
# size = int(input('masukan besar bintang: ')
# z = ''
# for j in range(size+1) :
#     if j < size:
#         for k in range(i, size*2):
#             if k <= size-j or k >= size+j:
#                 z += ' * '
#             else:
#                 z += '  '
#         z += '\n'
#     else:
#         for i in range(size-2,-1,-1):
#             for m in range

# ANOTHER VERSION
# You're using code navigation to jump to definitions or references.
# Learn more or give us feedback

#Hw1

# z = ''
# for i in range(5, 0, -1):
#     for j in range (0, i):
#         z += ' * '
#     z += '\n'    
# print(z)    

#Hw2

# z = ''
# for i in range(5, 0, -1):
#     if (i > 1):
#         for j in range (0, i):
#             z += ' * '
#         z += '\n'
#     elif i == 1:
#         for k in range (0, 5):
#             for l in range (0 , k+1):
#                 z += ' * '
#             z += '\n'        
# print (z)    

# # Hw3        
# z= ''
# for i in range (0,10,1):
#     for j in range (0, 21):
#         if j >= 10-i and j <= 10+i:
#             z += ' * '
#         else: 
#             z += '   '    
#     z += '\n'
# print (z)                

#Hw4
# z= ''
# for i in range (10,-1, -1):
#     for j in range (0, 21):
#         if j >= 10-i and j <= 10+i:
#             z += ' * '
#         else: 
#             z += '   '    
#     z += '\n'
# print (z)         
# 
# 
#       

#Hw5 Bintang Rapi

# z= ''
# for i in range (0,11):
#     if i < 10:
#         for j in range (0, 21):
#             if j >= 10-i and j <= 10+i:
#                 z += ' * '
#             else: 
#                 z += '   '    
#         z += '\n'
#     else:
#         for k in range (10,-1, -1):
#             for l in range (0, 21):
#                 if l >= 10-k and l <= 10+k:
#                     z += ' * '
#                 else: 
#                     z += '   '    
#             z += '\n'
# print (z)       

#Hw5 Bintang Tidak Rapi

# z= ''
# for i in range (0,11):
#     if i < 10:
#         for j in range (0, 21):
#             if j >= 10-i and j <= 10+i:
#                 z += ' * '
#             else: 
#                 z += '   '    
#         z += '\n'
#     else:
#         for k in range (11,-1, -1):
#             for l in range (0, 21):
#                 if l >= 10-k and l <= 10+k:
#                     z += ' * '
#                 else: 
#                     z += '   '    
#             z += '\n'
# print (z)     

# HW Bonus
# size = int(input('Masukkan Besar Bintang: '))
# z = ''
# for j in range (size+1):
#     if j < size:
#         for k in range (1,size*2):
#             if k <=size-j or k >= size+j:
#                 z += ' * '
#             else:
#                 z += '   '
#         z += '\n'            
#     else:
#         for l in range (size-2, -1, -1):
#             for m in range (1,size*2):
#                 if m <=size-l or m >= size+l:
#                     z += ' * '
#                 else:
#                     z += '   '
#             z += '\n'

# print(z)     