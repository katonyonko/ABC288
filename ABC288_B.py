import io
import sys

_INPUT = """\
6
5 3
abc
aaaaa
xyz
a
def
4 4
z
zyx
zzz
rbg
3 1
abc
arc
agc
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  S=sorted([input() for _ in range(N)][:K])
  print(*S,sep='\n')