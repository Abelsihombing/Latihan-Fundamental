# #  Soal 1
# def nbYear(p0, percent, aug, p):
#     years = 0
#     percentage = percent/100
#     while p0 < p :
#         p0 = (p0+p0 *percentage+ aug )
#         years += 1
#     print(years)
# nbYear(1000, 0, 50, 1070)
# # nbYear(1500, 5, 100, 5000)

# Soal 2
# def tickets(people):
#     Dompet = []  
#     result = ''
#     if people[0] == 25:
#         Dompet.append(people[0])
#         if len(people) > 1:
#             for x in people[1:]:
#                 if x == 25 :
#                     Dompet.append(x)
#                 elif x == 50:
#                     if 25 in Dompet:
#                         Dompet.remove(25)
#                         Dompet.append(50)
#                         result = 'YES'
#                     else:
#                         result = 'NO'
#                 elif x == 100:
#                     if 50 in Dompet:
#                         Dompet.remove(50)
#                         if 25 in Dompet:
#                             Dompet.remove(25)
#                             Dompet.append(100)
#                             result = 'YES'
#                         else:
#                             result = 'NO'
#                     elif 25 in Dompet:
#                         Dompet.remove(25)
#                         if 25 in Dompet:
#                             Dompet.remove(25)
#                             if 25 in Dompet:
#                                 Dompet.remove(25)
#                                 Dompet.append(100)
#                                 result = 'YES'
#                             else:
#                                 result = 'NO'
#                         else:
#                             result = ' NO'
#                     else:
#                         result = 'NO'
#         else:
#             result = "YES"
#     else:
#         result = 'NO'
#     # print(Dompet)
#     return result

# # print(tickets([25, 25, 50]))
# # print(tickets([25, 25, 50, 100]))
# print(tickets([25, 25, 25, 25, 100, 50, 25]))
# # # # print(tickets([25, 50, 50]))
# # # print(tickets([25, 50, 25, 100]))
# # # print(sum(people))

# Soal 3    
# def rowSumOddNumbers(n):
#     num = 1
#     total = 0
#     list = []
#     for row in range(0, n):
#         for col in range(row,n-1):
#             print(end=' ')
#         for col in range(0, row+1):
#             if num < 10:
#                 pr_num = f' {num}'   
#             else:
#                 pr_num = str(num)
#             print(pr_num,end=' ')
#             if(row == n-1):
#                 list.append(num)
#             num += 2
#         print()
    
#     a = ''
#     for i in range(len(list)):
#         total += list[i]
#         a += str(list[i])
#         if (i != len(list) -1) and len(list):
#             a += '+'
#         if len(list) == 1:
#             print('\nTotal: {}'.format(total))
#         if len(list)>1:
#             print('\nTotal: {} = {}'.format(a,total))

# rowSumOddNumbers(4)