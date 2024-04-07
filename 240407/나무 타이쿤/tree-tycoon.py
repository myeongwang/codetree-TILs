# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
height = [
    list(map(int, input().split()))
    for _ in range(n)
]

fertilizer = [
    [False for _ in range(n)]
    for _ in range(n)
]
next_fert = [
    [False for _ in range(n)]
    for _ in range(n)
]

# 문제에서 주어진 순서대로 → ↗ ↑ ↖ ← ↙ ↓ ↘
dxs = [0, -1, -1, -1,  0,  1, 1, 1]
dys = [1,  1,  0, -1, -1, -1, 0, 1]


def init_fertilizer():
    for i in range(n - 2, n):
        for j in range(2):
            fertilizer[i][j] = True


def next_pos(x, y, d, p):
    nx = (x + dxs[d] * p + n * p) % n
    ny = (y + dys[d] * p + n * p) % n
    return (nx, ny)


def move(d, p):
    # Step1. 그 다음 fert 위치를 저장할 
    #        next_fert를 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_fert[i][j] = False

    # Step2. 각 영양제를 이동합니다.
    for i in range(n):
        for j in range(n):
            if fertilizer[i][j]:
                nx, ny = next_pos(i, j, d, p)
                next_fert[nx][ny] = True
    
    # Step3. next_fert 값을 fert로 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            fertilizer[i][j] = next_fert[i][j]


def grow():
    for i in range(n):
        for j in range(n):
            if fertilizer[i][j]:
                height[i][j] += 1


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def get_diag_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs[1::2], dys[1::2]):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and height[nx][ny] >= 1:
            cnt += 1

    return cnt


def diagonal_grow():
    for i in range(n):
        for j in range(n):
            if fertilizer[i][j]:
                cnt = get_diag_cnt(i, j)
                height[i][j] += cnt


def determine_fert():
    for i in range(n):
        for j in range(n):
            # 기존 특수 영양제는 없애주고
            if fertilizer[i][j]:
                fertilizer[i][j] = False

            # 새로운 특수 영양제는 추가해줍니다.
            elif height[i][j] >= 2:
                fertilizer[i][j] = True
                height[i][j] -= 2
            

def simulate(d, p):
    # Step 1. 특수 영양제를 이동시킵니다.
    move(d, p)
    
    # Step 2. 특수 영양제 위치에 있던 리브로수가 성장합니다.
    grow()
    
    # Step 3. 대각선 방향의 높이가 1이상인 리브로수 만큼 
    #         더 성장합니다. 
    diagonal_grow() 
    
    # Step 4. 새로운 특수 영양제를 추가하고, 
    #         기존 영양제를 없애줍니다.
    determine_fert()


def get_score():
    return sum([
        height[i][j]
        for i in range(n)
        for j in range(n)
    ])


init_fertilizer()

# m번에 걸쳐 시뮬레이션을 진행합니다.
for _ in range(m):
    d, p = tuple(map(int, input().split()))

    simulate(d - 1, p)

ans = get_score()
print(ans)