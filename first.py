tot = 0
tot_suc = 0
tot_un = 0
min_val = float('inf')
max_val = float('-inf')
while (num :=int(input('Please rost: '))) != -1:
    if 150 <= num <= 180:
        tot_suc +=1
        if min_val > num:
            min_val = num
        if num > max_val:
            max_val = num
    else: tot_un += 1

    tot +=1
print(f'kandidate: {tot}')
print(f'Succ: {tot_suc}')
print(f'Unsucc: {tot_un}')
print(f'Min: {min_val}')
print(f'MMax: {max_val}')