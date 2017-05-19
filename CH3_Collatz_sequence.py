#! python 3
#! CH3_Collatz_sequence - script to to calculate collatz seq
def collatz(number):

        if number % 2 == 0:
            print (number/2)
            return number/2

        elif number % 2 == 1:
            result = (3 * number + 1 )
            print (result)
            return result

while True:
    try:
        number = int(input('Enter a number '))
    except ValueError:
        print ('Integers only')
        continue
    if number < 0 or number == 0:
        print ('Not positive integer')
        continue

    while number != 1:
        number = collatz(int(number))
    break
