#방향: 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [ 0, 1, 0,-1]

L, N, Q = map(int, input().split())
# 벽으로 둘러싸서, 범위체크 안하고, 범위밖으로 밀리지 않게 처리
arr = [[2]*(L+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(L)]+[[2]*(L+2)]
units = {} # 새로운 입력 저장용 
# v = [[0]*(N+2) for _ in range(N+2)] # 디버거로 동작확인용
init_k = [0]*(N+1) # 초기 체력 저장용 

for m in range(1, N+1): # 기사들에 대한 입력 
    si,sj,h,w,k=map(int, input().split())
    units[m]=[si,sj,h,w,k]
    init_k[m]=k                 # 초기 체력 저장(ans 처리용)
    # for i in range(si,si+h):    # 디버그용(제출시 삭제 가능)
    #     v[i][sj:sj+w]=[m]*w


def push_unit(start, dr):       # s를 밀고, 연쇄처리..
    q = []       #밀 대상들       # push 후보를 저장
    pset = set()                # 이동 기사번호 저장(중복체크 위함)
    damage = [0]*(M+1)          # 각 유닛별 데미지 누적 

    q.append(start)             # 초기데이터 append
    pset.add(start)

    while q: # q에 데이터가 있는 동안 
        cur = q.pop(0)          # q에서 데이터 한개 꺼냄 #기사 번호 
        ci,cj,h,w,k = units[cur] # 기사 위치 가져오기 

        # 명령받은 방향진행, 벽이아니면, 겹치는 다른조각이면 => 큐에 삽입
        ni,nj=ci+di[dr], cj+dj[dr]
        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if arr[i][j]==2:    # 벽!! => 모두 취소
                    return # 벽이면 밀수 없으니 그냥 끝내. 
                if arr[i][j]==1:    # 함정이라면 데미지 누적 
                    damage[cur]+=1  # 데미지 누적 
        
        # 움직였을 때 다른 유닛이 있으면 계도 움직여야 하니 
        # 겹치는 다른 유닛있는 경우 큐에 추가(모든 유닛 체크)
        for idx in units:
            if idx in pset: continue    # 이미 움직일 대상이면 체크할 필요없음

            ti,tj,th,tw,tk=units[idx]
            # 겹치는 경우
            if ni<=ti+th-1 and ni+h-1>=ti and tj<=nj+w-1 and nj<=tj+tw-1:
                q.append(idx)
                pset.add(idx)
                
    # 명령 받은 기사는 데미지 입지 않음
    damage[start]=0 # 다시 0으로 맞추기 

    # 이동, 데미지가 체력이상이면 삭제처리
    for idx in pset:
        si,sj,h,w,k = units[idx]

        if k<=damage[idx]:  # 체력보다 더 큰 데미지면 삭제
            units.pop(idx)
        else:
            ni,nj=si+di[dr], sj+dj[dr]
            units[idx]=[ni,nj,h,w,k-damage[idx]]



for _ in range(Q):
  idx, dr = map(int,input().split())
  if id in units:
    push_unit(idx,dr)


ans = 0
for idx in units:
  ans+= init_k[idx]- units[idx][4]
print(ans)