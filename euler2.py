

sum_of_evens = 0 
a,b = 1,2
n = 4000000
while a < n:
    if a % 2 == 0 :
        sum_of_evens += a 
    a,b = b , a+b

print(sum_of_evens)