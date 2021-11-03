import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()
res = [[0] * (len(str2)+1) for i in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            res[i][j] = res[i - 1][j - 1] + 1
        else:
            res[i][j] = max(res[i - 1][j], res[i][j - 1])

print(res[-1][-1])
