# Soal 1
# def timeConverter(seconds):
#     jam = seconds//3600
#     menit = (seconds%3600)//60
#     detik = (seconds%3600)%60
#     if jam <= 99 and menit <= 59 and detik <= 59 : 
#         print('{}:{}:{}'.format(str(jam).zfill(2),str(menit).zfill(2),str(detik).zfill(2)))
#     else:
#         print('invalid input')
# timeConverter(54640)

# Soal 2
# def spinwords(string):
#     kata = string.split()
#     for i in kata:
#         if len(i) >= 5 :
#             print(i[::-1], end=' ')
#         else:
#             print(i, end=' ') 
# spinwords("hey fellow warrior")
# spinwords("This is not easy but everyone capable to pass the test")

# Cara 2
# def spinwords(string):
#     word = []
#     for i in string.split():
#         if len(i) >= 5:
#             reverse = []
#             for idx in range(len(i)-1,-1,-1):
#                 reverse.append(i[idx])
#             word.append(''.join(reverse))
#         else:
#             word.append(i)
#         # print(word)
#     return ' '.join(word)
# # print(spinwords('This is not easy but everyone capable to pass the test'))
# print(spinwords('feeling my way through the darkness'))

# Soal 3
# def moveZeros(list):
#     length = len(list)
#     for item in range(length):
#         for item2 in range(length):
#             if (str(list[item2]) == '0' and item2 != length-1) :
#                 num1 = list[item2]
#                 list[item2] = list[item2 + 1]   
#                 list[item2 + 1] = num1
#     print(list)           
# moveZeros([False,1,0,1,2,0,1,3,"a"])
# moveZeros([0,0,0,"Test",0,3,"a",True]) 

# # Soal 4 PaginationHelper
# from math import ceil
# class PaginationHelper:
#     def __init__(self, list, page):
#         self.book = list
#         self.page = page
#         self.page_count = ceil(len(self.book)/self.page)
#         self.item_count = len(self.book)
#         self.book_list = []
#         self.page_dict = {}
#         # membuat list dalam list
#         for i in range(self.page_count):
#             temp = []
#             if i == self.page_count - 1:
#                 if self.item_count % self.page > 0:
#                     for j in range(self.item_count % self.page):
#                         temp.append(self.book[j + i*self.page])
#                 else:
#                     for l in range(self.page):
#                         temp.append(self.book[l + i*self.page])
#             else:
#                 for k in range(self.page):
#                     temp.append(self.book[k + i*self.page])
#             self.book_list.append(temp)
        
#         for idx, val in enumerate(self.book_list):
#             for idx1 in range(len(val)):
#                 self.page_dict[idx1 + (self.page * idx )] = idx
#         # {key : value} = {index dr item : index dr page}
    
#     def page_item_count(self, num):
#         try:
#             print(len(self.book_list[num]))
#         except:
#             print(-1)

#     def page_index(self, num):
#         if num > self.item_count or num < 0:
#             print(-1)
#         else:
#             print(self.page_dict[num])

# helper = PaginationHelper('a b c d e f g h' .split(), 4)
# print(helper.page_count)
# print(helper.item_count)
# helper.page_item_count(0)
# helper.page_item_count(1)
# helper.page_item_count(3)
# print('\n')
# helper.page_index(7)
# helper.page_index(2)
# helper.page_index(20)
# helper.page_index(-10)
        