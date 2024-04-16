di=[-1,0,1,0] #상,우,하,좌
dj=[0,1,0,-1]


L,N,Q = map(int,input().split()) # 4 3 3
arr = [[2]*(L+2)] + [[2]+ list(map(int,input().split())) +[2] for _ in range(L)] + [[2]*(L+2)]
units ={}
init_k =[0]*(N+1)

for i in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    units[i]=[r,c,h,w,k] # r:좌측 상단 x좌표 , c: 좌측 하단 y좌표  , h: 높이, w: 너비 , k: 목숨
    init_k[i]=k

def push_units(start,dr):
    q= [] # 밀 기사 후보 , 일단 명령 한 개당 하나 것지, 그리고 무조건 pop() 해줘야겠지
    pset = set() # 이동 기사 번호
    damage = [0] * (N + 1)
    q.append(start)
    pset.add(start) # set은 중복허용 안함. dict도 중괄호 사용하나 key-value 형태

    while q: # q에 원소가 없을 때까지
        cur = q.pop(0) # q.pop(0): q에서 젤 첫번째 원소 제거, q.pop() 가장 마지막 원소제거: 근데 여기선 어차피 한 개 씩만 들어가서 딱히 상관없음.

        ci,cj,ch,cw,ck = units[cur] # 이걸 여기서 재정의한다는 생각을 하기가 쉽지 않음.
        ni, nj = ci + di[dr], cj + dj[dr] # 미리 정의해놓은 거에 대한 움직임(dr) 받아와서 움직임 정의

        for i in range(ni, ni+ch): # 이제 탐색하면서 ==2:벽, ==1:함정 찾아야함. 이제 이해가 됐네 왜 ni+cw가 이나라 ni+ch 인지 ㅠ
            for j in range(nj,nj+cw):
                if arr[i][j]==2: # 벽이라면
                    return
                if arr[i][j]==1: # 함정이라면
                    damage[cur]+=1
        # 겹치는 것들 q, pset에 추가해줘야지
        for idx in units:
            if idx in pset: continue # 이미 밀릴 후보라면 continue

            ti,tj,th,tw,tk = units[idx]
            # 겹치는 녀석들 정의
            if ni<=ti+th-1 and nj<=tj+tw-1 and ni+ch-1>= ti and nj+cw -1>=tj:
                pset.add(idx)
                q.append(idx)

    damage[start]=0 # 명령 받은 기사는 뎀지 안 입음

    # 이제 초기체력 보다 데미지가 큰 녀석들은 삭제 처리 + 이동처리 해줘야지 # 지금은 데미지를 먼저 입고 이동처리 하는 느낌임. (데미지 입은 녀석들은 이동처리를 해야하니깐) 원래는 이동처리하고 데미지 입음
    for idx in pset:

        si,sj,sh,sw,sk = units[idx]

        if sk<= damage[idx]:
            units.pop(idx)
        else:
            ni,nj = si + di[dr], sj+dj[dr]
            units[idx]=[ni,nj,sh,sw,sk-damage[idx]]

for _ in range(Q):
    idx, dr = map(int,input().split())
    push_units(idx,dr)

ans = 0

for idx in units:
    ans += (init_k[idx]- units[idx][4])
print(ans)