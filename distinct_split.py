from collections import Counter

for _ in range(int(input())):
    n, s = int(input()), input()
    c1, c2 = Counter(), Counter(s)
    result = len(c2)

    for j in s:
        c1[j] += 1
        c2[j] -= 1
        if c2[j] == 0:
            c2.pop(j)

        result = max(result, len(c1) + len(c2))
    print(result)
