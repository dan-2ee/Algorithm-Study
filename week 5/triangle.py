def solution(n):
    res = [[0] * n for i in range(n)]  # n만큼 배열 만들어주기
    x, y = -1, 0  # 처음 시작은 아래로 내려가기 때문에 x=-1로 시작
    num = 1
    answer = []

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1  # 아래
            elif i % 3 == 1:
                y += 1  # 오른쪽
            elif i % 3 == 2:  # 대각선
                x -= 1
                y -= 1
            res[x][y] = num
            num += 1

    answer = [j for i in res for j in i if j != 0]  # 0이 아닌 값들 넣어주기
    return answer