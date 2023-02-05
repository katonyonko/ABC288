import io
import sys

_INPUT = """\
6
4
3 5
2 -6
-5 0
314159265 123456789
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  for i in range(N): print(sum(list(map(int,input().split()))))