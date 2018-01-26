s = list(map(int, input('Enter the sequence:').split()))

n = len(s)

lis = [1] * n # inital: every single number is a sequence of size 1
p = [i for i in range(n)] # remember the relation of element of the lis

for i in range(1, n):
    p[i] = p[i-1]
    for j in range(i):
        if s[i] > s[j] and lis[i] < lis[j] + 1:
            lis[i] = lis[j] + 1
            p[i] = j

max_lis = 1
k = 0
for i in range(n):
    if lis[i] > max_lis:
        max_lis = lis[i]
        k = i

ans = [s[k]]
while k != p[k]:
    k = p[k]
    ans.append(s[k])

print(ans[::-1])

