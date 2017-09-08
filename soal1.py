# LIBRARY
from random import randint

# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
arr = [randint(1,100) for i in range(0,100)]

# FUNGSI INSERTION SORT
# Tulis algoritma disini...
def insertionSort(list):
   for index in range(1,len(list)):

     currentvalue = list[index]
     position = index

     while position>0 and list[position-1]>currentvalue:
         list[position]=list[position-1]
         position = position-1

     list[position]=currentvalue

list = arr
insertionSort(arr)
print(arr)