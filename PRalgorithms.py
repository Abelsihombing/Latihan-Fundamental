# ## SOAL 1
# list_angka = [1,3,3,3,4,4,2,4]
# import math

# def getmean(x) :
#     sum = 0
#     for item in x :
#         sum += item

#     mean = sum / len(x)
#     return mean

# print(getmean(list_angka))

# def getmedian(x):
#     x.sort()
#     median = 0
#     if (len(x) % 2 != 0) :
#         median = x[(len(x) / 2)]
#     else:
#         mid1 = x[(int(len(x)/ 2)) -1]
#         mid2 = x[int(len(x)/ 2)]
#         median = (mid1 + mid2)/2
#     return median

# print(getmedian(list_angka))

# def getmode(x):
#     largestCount = 0
#     modes = []
#     for i in x:
#         if i in modes:
#             continue
#         count = x.count(i)
#         if count > largestCount:
#             del modes[:]
#             modes.append(i)
#             largestCount = count
#         elif count == largestCount:
#             modes.append(i)
#     return modes 
# print(getmode(list_angka))

# cara 2
# def mode_list(x):
#     ind = set(x)
#     counter = {}
#     modus = []
#     for i in ind:
#         z = 0
#         for j in x:
#             if i == j :
#                 z += 1
#         counter[i] = z
#     max_count = max(counter.values())
#     for k in counter:
#         if counter[k] == max_count:
#             modus.append(k)
#     if len(modus) == len(set(x)):
#         modus = []
#     return modus
# print(mode_list(list_angka))

# def variance(x):
#     num1 = 0
#     for num in list_angka:
#         num1 += (num - getmean(list_angka)) ** 2
#         num2 = num1 / (len(list_angka) - 1)
#     return num2
# print(variance(list_angka))

# def stddev(x):
#     n1 = 0
#     for item in list_angka:
#         n1 += (item - getmean(list_angka)) ** 2
#         n2 = n1 / (len(list_angka) - 1)
#         var = math.sqrt(n2)
#     return var
# print(stddev(list_angka)) 

# def varpop(x):
#     y1 = 0
#     for var in list_angka:
#         y1 += (var - getmean(list_angka)) ** 2
#         y2 = y1 / (len(list_angka))
#     return y2
# print(varpop(list_angka)) 

# def skewness(x):
#     s1 = 0
#     for pop in list_angka:
#         s1 += (pop - getmean(list_angka)) ** 3
#         s2 = s1 / (len(list_angka))
#         s3 = s2 / (varpop(list_angka) ** 3)
#     return s3  
# print(skewness(list_angka))

# def kurtosis(x):
#     o1 = 0
#     for you in list_angka:
#         o1 += (you - getmean(list_angka)) ** 4
#         o2 = o1 / (len(list_angka))       
#         o3 = o2 / varpop(list_angka)** 4
#         o4 = o3 - 3
#     return o4
# print(kurtosis(list_angka))

## Soal 2

def triangular(x):
    a = 1
    list1 = []
    number1 = 0
    for bro in range(1,x+1):
        list1 = []
        for cuy in range(1,bro+1):
            if (cuy == bro):
                list1.append(a)
                print(list1)
                number1+=a
            else:
                print(a, end=' ')
            a+=1
angka = int(input('berapa? : '))
triangular(angka)