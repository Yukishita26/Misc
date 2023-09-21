import sys
try:
  N = int(sys.argv[1])
except Exception:
  N = 100

def code(str_):
  r = [ord(s) for s in str_]
  return r + [0] * (8-len(r))

def fizzbuzz_list(n):
  res = []
  for i in range(1, n+1):
    if i%15==0:
      res.append("FizzBuzz")
    elif i%3==0:
      res.append("Fizz")
    elif i%5==0:
      res.append("Buzz")
    else:
      res.append(str(i))
  return res

def lagrange_interpolation(xs, ys):
  return " + ".join([
      f"{yj} * " + " * ".join([f"(x-{xi})/({xj}-{xi})" for i, xi in enumerate(xs) if i!=j])
      for j, (xj, yj) in enumerate(zip(xs,ys))
  ])

def create_fizzbuzz(n):
  fizzbuzz_learn = [code(s) for s in fizzbuzz_list(n)]
  exs = []
  for i in range(8):
    xs = range(1, len(fizzbuzz_learn)+1)
    ys = [line[i] for line in fizzbuzz_learn]
    exs += [lagrange_interpolation(xs, ys)]
  fb_code = "lambda x: ''.join([s for s in (" + ",".join([
    ("chr(int(" + ex + "))")
    for ex in exs
  ]) + ") if s!=chr(0)])"
  return fb_code

if __name__=="__main__":
    fb_code = create_fizzbuzz(N)
    print("""import sys
try:
  N = int(sys.argv[1])
except Exception:
  N = 100

fb = """ + fb_code + """

if __name__=="__main__":
  for i in range(1, N+1):
    print(fb(i))
""")