T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    arr = []
    ans = 0
    for i in range(H):
        row = input()
        arr.append(row)
        if row.count('#') == W:
            ans += 1
    for j in range(W):
        check = True
        for k in range(H):
            if arr[k][j] == '.':
                check = False
                break
        if check:
            ans += 1
    if ans == H+W:
        ans = min(H, W)
    print(ans)