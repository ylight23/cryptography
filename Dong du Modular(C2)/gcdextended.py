# from numpy import number


# numbers=[2,4,5,6,10,15,30]
# bigger_number=[x for x in numbers if x!=10]
# print(bigger_number)



# # dinh nghia ham cua do dai ten
# def Do_dai_ten(name): 
#     return len(name)
# #kiem tra do dai
# ten= input("Nhap ten: ")
# print("Do dai ten: ",Do_dai_ten(ten))  

# def ham_ngoai():
#     x = "Biến cục bộ"
 
#     def ham_trong():
#        #nonlocal x
#        x = "Biến nonlocal"
#        print("Bên trong:", x)
 
#     ham_trong()
#     print("Bên ngoài:", x)

# ham_ngoai()

# def Xin_chao(*ten_chao):
#     """
#     Hàm này sẽ chào một danh sách người cho trước
#     """
#     for ten in ten_chao:
#        print("Xin chào",ten)

# Xin_chao("Hải","Hoa","Công","1234","^^^^")

# a = 1 # Biến toàn cục

# def them():
#     global a
#     a = a + 9 
#     print("Trong them():", a)

    
# print("Trong main:", a)
# them()


# import module sys để gọi ra các ngoại lệ
import sys

#!/usr/bin/env python
import math
c=50
h=30
value = []
items=[x for x in input("Nhập giá trị của d: ").split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# Code by Quantrimang.com
print (','.join(value))