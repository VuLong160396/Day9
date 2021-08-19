
startNumber, endNumber = input("Enter a two number: ").split()
startNumber = int(startNumber)
endNumber = int(endNumber)

if endNumber < startNumber:
    	print('The ending number must be greater than start')
else:
    	for number in range(startNumber, endNumber + 1):
            if number % 3 == 0 and number % 5 == 0:
            	print("FizzBuzz")
            	continue
            elif number % 3 == 0:
                print("Fizz")
                continue
            elif number % 5 == 0:
                print("Buzz")
                continue
            else:
                print(number)