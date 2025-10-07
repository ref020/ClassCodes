count = 0
for i in range(1, 1000001):
    b = i
    x = list(str(b))
    for n in range(1, len(x)):
        if (x[n] == "0"):
            count += 1
print (count)