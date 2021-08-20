condition = False
try: 
    number  = int(input("Nhap so: "))
    print(f'Bang cuu chuong cua {number}')
    condition = True
    if condition:
        for i in range(1,10):
            print(f'{number} x {i} =', number*i )
except:
    print('Dinh dang khong hop le,moi nhap so nguyen!!!')