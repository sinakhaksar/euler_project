
import time
start_time = time.time()

def is_prime(number):
    is_prime = True
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0 :
            is_prime = False
            break
    return is_prime
sum = 0 
counter = 0
for i in range(2, 2000000):
    if is_prime(i) :
        sum += i
        counter += 1
       
print(sum)
print("--- %s seconds ---" % (time.time() - start_time))
