import sys
try:
  N = int(sys.argv[1])
except Exception:
  N = 100


if __name__=="__main__":
  for i in range(1, N+1):
    print(fb(i))
