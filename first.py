res =[]
with open('info.txt', 'rt') as f:
    while temp := f.readline():
        res += temp.split(', ')
res = list(map(lambda x: x.rstrip('\n'), res))
#res = set(res)
res = sorted(int(x) for x in set(res))
print(res)