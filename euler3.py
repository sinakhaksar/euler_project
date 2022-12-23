

#number = 600851475143

def divisor_by_prime (number):
    bigest_prime = 0
    number_check = 1
    for i in range (2, number):
        if number % i == 0:
            number_check = number_check * i
            if number_check == number:
                print(i,number_check)
                break
            if i > bigest_prime:
                bigest_prime = i
                print(i)
                

divisor_by_prime(600851475143)
