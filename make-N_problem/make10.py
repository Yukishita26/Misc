import itertools
from operator import add, sub, mul, truediv
from fractions import Fraction as F
operators = [add, sub, mul, truediv]

def calc(nums, ops):
  nums = list(nums[::-1])
  ops = list(ops[::-1])
  assert len(nums)-1==len(ops)
  n = len(ops)
  top = nums.pop()
  for k in range(n):
    x = nums.pop()
    o = ops.pop()
    top = o(top, x)
  return top

### operatorを使用
*a, x = map(int, input().split())
a = [F(v) for v in a]
n = len(a)
for nums in itertools.permutations(a):
  for ops in itertools.product(*[operators]*(n-1)):
    y = calc(list(nums), list(ops))
    if x==y:
      num_int = list(map(str, nums))
      op_sym = [{add:"+", sub:"-", mul:"*", truediv:"/"}[op] for op in ops]
      print(" ".join(sum([num_int[:1]] + [[o, n] for n, o in zip(num_int[1:], op_sym)], [])))
      exit()

### evalを使用
symbols = ["+","-","*","/"]
#*a, x = map(int, input().split())
#n = len(a)
x = F(x)
for ps in itertools.permutations(a):
  for ss in itertools.product(*[symbols]*(n-1)):
    fs = []
    for p, s in zip(ps, ss):
      fs += [f"F({p})", s]
    fs += [f"F({ps[-1]})"]
    f = " ".join(fs)
    if x==eval(f):
      print(" ".join(fs).replace("F(", "").replace(")", ""))
      exit()
print("No")