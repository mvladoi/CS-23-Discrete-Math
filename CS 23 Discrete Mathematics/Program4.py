

import random, time
 
def quicksort( aList ):
    _quicksort( aList, 0, len( aList ) - 1 )
 
def _quicksort( aList, first , last ):
    if first < last:
      pivot = partition( aList, first, last )
      _quicksort( aList, first, pivot - 1 )
      _quicksort( aList, pivot + 1, last )
 
 
def partition( aList, first, last ) :
    pivot = first + random.randrange( last - first + 1 )
    swap( aList, pivot, last )
    for i in range( first, last ):
      if aList[i] <= aList[last]:
        swap( aList, i, first )
        first += 1
 
    swap( aList, first, last )
    return first
 
 
def swap( A, x, y ):
  A[x],A[y]=A[y],A[x]



n = 2**6
while n <= 2**12:
  data = [random.random() for i in range(n)]
  before = time.process_time()
  quiksort(data)              # find min
  after = time.process_time()
  print(n, after-before)
  n *= 2


