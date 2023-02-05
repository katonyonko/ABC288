import io
import sys

_INPUT = """\
6
5 2
3 1 4 1 5
9 2 6 5 3
3 5
20 8
29 27 79 27 30 4 93 89 44 88 70 75 96 3 78 39 97 12 53 62
32 38 84 49 93 53 26 13 25 2 76 32 42 34 18 77 14 67 88 12
1 3 4 5 8 14 16 20
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  def sliding_window(A,L):
    """
    A: 列のi番目の要素
    L: 最小値を調べる長さ
    """
    ans = []
    que = deque()
    for i, a in enumerate(A):
      while que and a <= que[-1][1]:
        que.pop()
      que.append((i, a))
      ans.append(que[0][1])
      if que and que[0][0] <= i+1-L:
        que.popleft()
    return ans[L-1:]

  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  C=list(map(int,input().split()))
  X=set((map(lambda x:int(x)-1,input().split())))
  cost=[sliding_window(C,i+1) for i in range(N)]
  dp=[10**15]*((N+1)**2)
  dp[0]=0
  for i in range(N):
    for j in range(N+1):
      if i not in X: dp[(i+1)*(N+1)+j]=min(dp[(i+1)*(N+1)+j],dp[i*(N+1)+j])
      s=max(0,i-j+1)
      if j>0: dp[(i+1)*(N+1)+j]=min(dp[(i+1)*(N+1)+j],dp[i*(N+1)+j-1]+A[i]+cost[i-s][s])
  print(min(dp[-N-1:]))