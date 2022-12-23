num = open("txt.txt")
lines = num.readlines()
for i in range(0,len(lines)):
    lines[i] = int(lines[i])
    #lines[l] = int(lines[l])
linesum = sum(lines)
answer = str(linesum)[0:10]
print(answer)