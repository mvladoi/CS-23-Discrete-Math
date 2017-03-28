import as8
 
def fun1(n):
  for i in range (n):
   for j in range (n):
    t= i + j
  return t
 
def fun2(n):
  for i in range (n):
   k = i+i
  return k 
 
def fun3(n):
  import math, time
  return len(range(int(abs(math.log(time.time()**-3)))))
 
for fun in (fun1, fun2, fun3):
  # Print the name of the function and our estimated running time
  print(fun.__name__, as8.estimate_big_o(fun))
