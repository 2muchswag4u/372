
#while
# i=1
# while i<10:
#     print(i)
#     pass


#for

# for k in range(10):
#     print(k)

# for j,k in enumerate(range(10)):
#     print(j)
#     print("k",k)
#
# for item in "[1,2,3,4,5,6,7]":
#     print(item*2)
#
# for item in "[1,2,3,4,5,6,7]":
#     print(item*2)

# for l,line in enumerate(open("archivo.txt")):
#     for p in line.split():
#         for f in p:
#             if f=="r":
#                 pass
#             else:
#                 print(f)
#
# lista = []
# for i in range(10):
#     lista.append(i)
# print(lista)

# lista =[i for i in range(10)]
# print(lista)
import random
r = 1
while r != 99:
    r=random.randint(1,10000)
    print(r)
