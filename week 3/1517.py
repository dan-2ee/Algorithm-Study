def Merge_sort(start, end):
    global cnt
    if start < end:
        mid = (start + end) // 2
        Merge_sort(start, mid)
        Merge_sort(mid + 1, end)

        #merge
        l, r = start, mid+1
        tmp = []
        while l <= mid and r <= end:
            if lst[l] <= lst[r]:
                tmp.append(lst[l])
                l += 1
            else:
                tmp.append(lst[r])
                r += 1
                cnt += (mid - l + 1)  #왼쪽 리스트의 원소 개수만큼 swap 횟수 추가

        # 남아있는 원소들 처리
        if l <= mid:
            tmp = tmp + lst[l:mid+1]
        if r <= end:
            tmp = tmp + lst[r:end+1]

        for i in range(len(tmp)):
            lst[start + i] = tmp[i]  #lst의 값을 정렬된 값으로 바꿈

N = int(input())
lst = list(map(int, input().split()))
cnt = 0
Merge_sort(0, N-1)
print(cnt)