import io
import sys

_INPUT = """\
6
7 3
3 -1 1 -2 2 0 5
2
1 6
2 7
20 4
-19 -66 -99 16 18 33 32 28 26 11 12 0 -16 4 21 21 37 17 55 -19
5
13 16
4 11
3 12
13 18
4 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  AA=[[0] for i in range(K)]
  for i in range(N):
    for j in range(K):
      if i%K==j: AA[j].append(AA[i%K][-1]+A[i])
      else: AA[j].append(AA[j][-1])
  # print(AA)
  Q=int(input())
  for _ in range(Q):
    l,r=map(int,input().split())
    l-=1
    ans='Yes'
    for i in range(1,K):
      # print(r,l,K,r-i,r,l,r-K)
      if AA[(r-i)%K][r]-AA[(r-i)%K][l]!=AA[r%K][r]-AA[r%K][l]: ans='No'
    print(ans)