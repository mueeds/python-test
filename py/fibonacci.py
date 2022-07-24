seq = [0,1]
result = 0

while result < 100:

    result = seq[-1] + seq[-2]
    if (result < 100):
        seq.append(result)
print(seq)