n, *num = map(int, open(0).read().split())
dic, deque = {}, []
for i in num[::-1]:
    if i not in dic:
        dic[i] = 1
        deque.append(i)
print(*deque[::-1])
