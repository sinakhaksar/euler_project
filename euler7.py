
def is_prime(number):
    is_prime = True
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0 :
            is_prime = False
            break
    return is_prime
counter = 0
for i in range(2,1000000):
    if is_prime(i) :
        counter += 1
        if counter == 10001:
            print(counter ,"prime is ->", i)
            break
        