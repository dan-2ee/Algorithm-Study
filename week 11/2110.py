N, C = map(int, input().split())

house = []
for _ in range(N):
    x = int(input())
    house.append(x)

house.sort()

start = 1
end = house[-1] - house[0]

wifi = 0

while start <= end:
    mid = (start + end) // 2
    current = house[0]
    count = 1
    for i in range(1, len(house)):
        if house[i] >= current + mid:
            count += 1
            current = house[i]

    if count >= C:
        start = mid + 1
        wifi = mid
    else:
        end = mid - 1

print(wifi)