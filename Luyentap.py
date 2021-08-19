#Lap theo 1 list
listnumber = ['a','b','c','d']
for i in listnumber:
    print(i)

#Lap theo 1 chuoi
listfruit = "apple"
for i in listfruit:
    print(i,sep='',end="")

print('\n')

#Lap theo Range()
for i in range(5):
    print(i,end=',')
print('\n')

#lap theo range co 2 tham so
for i in range(5,10):
    print(i,end=',')
print('\n')

#lap theo range co 3 tham so
for i in range(0,10,2):
    print(i, end=',')
print('\n')

#vong lap long nhau
listnumber = [1,2,3,4]
listfruit = ['a','b','c','d']
for i in listnumber:
    print(i,end='.')
    for i in listfruit:
        print(i,end='')
print('\n')

#vong lap ket hop break
fruit = ['apple', 'banana', 'cherry']
for i in fruit:
    print(i)
    if i == 'banana':
        break
print('\n')

#vong lap ket hop continue
av = ['a','b','c','d']
for i in av:
    if i == 'b':
        continue
    print(i,end='')
print('\n')
#vong lap ket hop Pass
for i in 'Python':
    if i == 'h':
        pass
        print(' this is pass block')
    print(i,end='')
print('\tgood bye!\n')
#vong lap ket hop Else
for i in [1,2,3]:
    print(i,end=' ')
else:
    print('Finally finished\n')
#vong lap Else se khong xay ra neu break trong vong lap
for i in [1,2,3,4,5]:
    if i == 3:
        break
    print(i, end=' ')
else:
    print('Vong lap ket thuc')
print('out of loop\t\n')

#Khac biet For vaf While
#Hien thi cac so tu 1 den 11
for i in range(11):
    print(i,end='.')
print('\n')

i = 0
while i <= 10:
    print(i,end='.')
    i += 1
print('\n')

#in ra tung phan tu trong mang long nhau
lists = [[1,2,3],['a','b','c'],[9.1 , 9.0 , 2.3]]
for ab in lists:
    for i in ab:
        print(i,end=' ')