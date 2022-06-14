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

def index(request):

  k = 0
  arr = [0]*10 
  for i in range(10):
      arr[k] = random.randrange(0, 100)
      k += 1

  reverse = rev( arr )

  context = {"arr" : arr, "reverse": reverse }

  template = loader.get_template('events.html')

  return HttpResponse(template.render(context, request))