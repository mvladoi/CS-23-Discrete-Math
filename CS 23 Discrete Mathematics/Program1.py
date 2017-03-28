

def is_reflexive(Set, Relation):
  a = list(Set)
  b = list (Relation)
  for i in range (len(a)):
   c = a[i]
   if (c,c) not in b:
      return False
    
  return True 




 
def is_symmetric(Relation):
  c = list(Relation)
  for item in range (len(c)):
    (a,b) = c[item]
    if not(b,a) in c:
     return False
  
  return True




 
def is_antisymmetric(Relation):
 c = list(Relation)
 for item in range (len(c)):
    (a,b) = c[item]
    if ((b,a) in c and b != a):
     return False

 return True 





 
def is_transitive(Relation):
 c = list(Relation)
 x = len (c)
 if x == 3:
   (a,b) = c[0]
   (d,e) = c[1]
   if b != d:
     return False
    
 for item in range (len(c)- 1):
    (a,b) = c[item]
    for i in range (len (c)):
     (d,e) = c[i]
     if (d,e) != (a,b):
        if (b == d) and (a,e) not in c:
          return False
  
 return True





 
def composite(R, S):
 r = list(R)
 s = list(S)
 w = set()
 for item in range (len(r)):
   (a,b) = r [item]
   for i in range (len(s)):
     (c,d) = s[i]
     if (b == c):
       w.add((a,d))
       
 return w    
  





def is_equivalence(Set, Relation):
 a = is_reflexive(Set, Relation)
 b = is_symmetric(Relation)
 c = is_transitive(Relation)
 print a, b, c
 if (a and b and c):
   return True
  
 return False 



a = is_equivalence(set([1, 2, 3, 4]), set([(1, 2), (3, 3), (4, 4), (1, 4), (2, 1), (2, 2), (4, 1), (1, 1)]))
print a

 




