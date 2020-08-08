s = input()
G, B = [], []
for idx, i in enumerate(s):
    if i == 'G':
        G += [idx]
    else:
        B += [idx]
res1 = sum(G) - (len(G) * (len(G) - 1) // 2)
res2 = sum(B) - (len(B) * (len(B) - 1) // 2)
print(min(res1, res2))
