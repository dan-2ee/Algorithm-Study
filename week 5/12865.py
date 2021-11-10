N, K = map(int, input().split())
obj = [[0, 0]]
bag = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    obj.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = obj[i][0]
        value = obj[i][1]

        if j < weight:
            # 현재 물건이 현재 돌고있는 무게보다 가볍다면 [이전 물건][같은 무게] 값을 그대로 가져옴
            bag[i][j] = bag[i - 1][j]
        else:
            # max(현재 물건 가치 + [이전 물건][현재 가방 무게 - 현재 물건 무게], [이전 물건][현재 가방 무게])
            # max = 현재까지의 물건들로 구성할 수 있는 가장 가치 높은 구성
            bag[i][j] = max(value + bag[i - 1][j - weight], bag[i - 1][j])

print(bag[N][K])    # K 무게일 때의 가치 최댓값

