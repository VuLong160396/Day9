a , b = input('Enter 2 number: ').split()
a = int(a)
b = int(b)
if b < a:
    print('the ending number must be greater than start number!!!')
else:
    for i in range(a,b+1):
        if i % 3 == 0 and i % 5 == 0: 
            print('FizzBuzz')
            continue
        elif i % 3 == 0:
            print('Fizz')
            continue
        elif i % 5 == 0:
            print('Buzz')
            continue
        else:
            print(i)


