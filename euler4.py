import time
start_time = time.time()

cheak = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        c = a * b
        c = str(c)
        digits = len(c)
        if digits == 2 or 4 or 6 :
            if c[0] == c[-1] and  c[1] == c[-2] :
                if c[2] == c[-3]:
                    c= int(c)
                    if c > cheak:
                        cheak = c
                        print(f"{a} * {b}={c} -c {cheak}")
                    else:
                        break
                    

print(cheak)
print("--- %s seconds ---" % (time.time() - start_time))


#beat ime is --- 0.8402700424194336 seconds ---
# cheaka is 906609