N = int(input())  #수열의 크기
positive_lst=[]   #양수 저장
negative_lst=[]   #음수 저장
result = 0

for i in range(N):
    num = int(input())
    if num > 1:
        positive_lst.append(num)
    elif num <= 0:
        negative_lst.append(num)
    else:
        result += 1      #1은 그냥 더함

positive_lst.sort(reverse=True)   #양수는 내림차순 정렬
negative_lst.sort()               #음수는 오름차순 정렬
pl, nl = len(positive_lst), len(negative_lst)

#양수 리스트 합 계산
if pl % 2 == 0:
    for i in range(0,pl,2):
        result += positive_lst[i] * positive_lst[i+1]
else:
    for i in range(0,pl-1,2):
        result += positive_lst[i] * positive_lst[i+1]
    result += positive_lst[pl-1] # 마지막 숫자는 더해주기

#음수 리스트 합 계산
if nl % 2 == 0:
    for i in range(0,nl,2):
        result += negative_lst[i] * negative_lst[i+1]
else:
    for i in range(0,nl-1,2):
        result += negative_lst[i] * negative_lst[i+1]
    result += negative_lst[nl-1] # 마지막 숫자는 더해주기
print(result)