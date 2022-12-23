n = 2520
# it's better to start here than 0 ;  
condition = True 
listt = [11,13,14,16,17,18,19,20]
# we only need to test the list 

while condition :
    counter = 0 
    for i in listt :
        if n % i == 0 :
            counter += 1 
        else : 
            n +=1
            break
    if counter == len(listt) :
        print('>>>',n)
        condition = False
        quit()

'''
it takes a while to run this 
so i just give you the answer 

it's  232792560

'''
 
