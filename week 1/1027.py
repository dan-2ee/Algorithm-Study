N = int(input())
building_lst = list(map(int, input().split()))
max_visible = 0

for x1 in range(N):
    visible = 0
    # 볼 수 있는 빌딩 수 - 오른쪽
    max_slope = -9999999999
    for x2 in range(x1+1, N):
        slope = (building_lst[x2]-building_lst[x1])/(x2-x1)
        if slope > max_slope:
            visible += 1
            max_slope = slope
    # 볼 수 있는 빌딩 수 - 왼쪽
    min_slope = 9999999999
    for x2 in range(x1-1, -1, -1):
        slope = (building_lst[x2]-building_lst[x1])/(x2-x1)
        if slope < min_slope:
            visible += 1
            min_slope = slope

    if max_visible < visible:
        max_visible = visible

print(max_visible)