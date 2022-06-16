from django.http import HttpResponse
from django.template import loader
import random

class Node:

    def __init__(self, value):

        self.data = value

        self.next = None

def rev(arr):
    
    head = None

    for i in arr:

        # if the node doesn t exist i mean is NULL, then do it   

        if head is None:

            head = Node(i)

        else:

            # insert the node at the end
            c = Node(i)
            
            ptr = head

            while ptr.next is not None:

                  ptr = ptr.next

            ptr.next = c  
            
    next = None
    prev = None 
    curr = head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    out = []
    c = prev
    while c is not None:
        
        out.append(c.data)

        c = c.next

    return out

def solveLIS( vec ):    
    
    n = len( vec )

    L = [ 0 ] * ( n )

    L[ n - 1 ] = 1

    for i in range(n - 2, -1, -1):
        
        max = 0

        for j in range(i + 1, n):

            if vec[i] < vec[j] and L[j] > max:

                max = L[ j ] 

        L[i] = 1 + max

    maxL = L[ 0 ]

    startPos = 0

    for i in range(1, n):

        if L[ i ] > maxL:

           maxL = L[ i ]

           startPos = i

    out = []

    maxL2 = maxL

    out.append(vec[startPos])       

    for i in range(startPos + 1, n):

        if vec[i] > vec[startPos] and maxL-1 == L[i]:

            out.append(vec[i])
            maxL -= 1       

    return [maxL2, startPos, out]       


def index( request ):

  k = 0

  arr = [ 0 ] * 10 

  for i in range( 10 ):

      arr [ k ] = random.randrange( 0, 100 )

      k += 1

  reverse = rev( arr )

  k = 0

  list = [ 0 ] * 10 

  for i in range( 10 ):

      list [ k ] = random.randrange( 0, 100 )

      k += 1

  # Time Complexity O(n^2)
  results = solveLIS( list )  

  maxL = results[0]

  startPos = results[1]

  subsequence = results[2]

  context = {"arr" : arr, "reverse": reverse, "list":list, "subsequence": subsequence, "startPos" : startPos, "maxL": maxL }

  template = loader.get_template('events.html')

  return HttpResponse(template.render(context, request))