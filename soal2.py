class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def printStack(self):
        print (self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# VARIABLE
# Sebagai inputan yang akan divalidasi
inputan = input("Masukkan: ")

# KELAS STACK
# Buatlah kelas objek Stack dengan 1 atribut yaitu array, lalu memiliki fungsi sbg berikut:
# isEmpty() -> return True jika Stack kosong dan False jika terisi.
# push(item) -> memasukkan item kedalam Stack
# pop() -> mengeluarkan item pada Stack
# size() -> menghitung jumlah item pada Stack
# printStack() -> output seluruh isi Stack

# FUNGSI VALIDASI BRACKETS
# Tulis algoritma disini...
def stackValidation(string_input):
    stak = Stack()
    result = True
    for items in string_input:
        if items == '(':
            stak.push('x')
        elif items == ')':
            if stak.isEmpty() == False :
                stak.pop()
            else :
                result == False
                return False
    if not stak.isEmpty():
        result = False
    return result

print(stackValidation(inputan))