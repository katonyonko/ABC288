import io
import sys

_INPUT = """\
6
3
234
4
5915
9
998244353
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N=int(input())
  X=input()
  ans=0
  tmp2=[1]
  for i in reversed(range(N)):
    x=int(X[i])
    ans+=x*tmp2[-1]
    ans%=mod
    tmp2.append((tmp2[-1]*10+ans)%mod)
  print(ans)