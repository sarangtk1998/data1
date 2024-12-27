
f = open('hello.txt','w')

for i in range(1,21):
    f.write('this is line %d\r'%i)

f.close()


f = open('hello.txt')

cont = f.readline()
cont1 = f.readline()

f.seek(0)

cont2 = f.read(18)
print(cont)
print(cont1)
print(cont2)

f.close()

