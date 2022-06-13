from django.shortcuts import render

from django.http import HttpResponse

#
# Check Order Array
# input: [1,2,3,4,5] => Output: ASCENDING
# input: [5,4,3,2,1] => Output: DESCENDING
# input: [5,8,3,2,1] => Output: Unordered
#

def checkorder(arr, order):

    order = "DESCENDING ORDER"

    i = 1

    n = len(arr)

    while i < n and arr[i] == arr[0]:
        i += 1
    if i == n:
        order = "Constant Sequence"
    else:
        if arr[i] > arr[i-1]:            
            order = "ASCENDING"
            for j in range(i, n):
                if arr[j] < arr[j-1]:
                    order = "Unordered"
                    break                
        if arr[i] < arr[i-1]:            
            order = "DESCENDING"
            for j in range(i, n):
                if arr[j] > arr[j-1]:
                    order = "Unordered"
                    break                

    return [arr, order]

def insertionsort(arr, n):
    
    for i in range(1, n):
        aux = arr[i]
        j = i - 1
        while j >= 0 and aux < arr[j]:
              arr[j+1] = arr[j]
              j -= 1
        arr[j+1] = aux     

def _qs(arr, lo, hi):
    
     i = lo
     j = hi
     p = arr[(lo + hi) // 2]

     while i <= j:

         while p > arr[i]:
               i += 1
         while p < arr[j]:
               j -= 1
         if i <= j:
             arr[i], arr[j] = arr[j], arr[i]
             i += 1
             j -= 1
     if lo < j:
         _qs(arr, lo, j)
     if i < hi:
         _qs(arr, i, hi)             


def quicksort(arr, n):
    _qs(arr, 0, len(arr) - 1)

def checkMountain(arr):
    
    i = 0

    n = len(arr)

    while i < n - 1 and arr[ i ] < arr[ i + 1]:

          i += 1

    if i == 0 or i == n - 1:

        return False     

    else:

        if i < n - 1:

            while i < n - 1 and arr[i] > arr[i + 1]:

                i += 1

            if i == n - 1:

                return True

            else:
                return False        

def bubble(arr, n):

    finished = False

    while finished is False:

         swapped = False

         for i in range(0, n - 1):

             if arr[i] > arr[i+1]:

                swapped = True

                arr[i], arr[i+1] = arr[i+1], arr[i]

         if swapped is True:

            n -= 1

         else:

            finished = True    

def index(request):

    input = [9,8,7,6,5,4,3,2,1]

    insertionsort( input, len( input ) )

    mountain = [1,2,3,4,5,4,3,2,1]

    aspect = checkMountain( mountain )

    mountain2 = [10,12,3,4,5,4,3,2,0]

    aspect2 = checkMountain( mountain2 )

    arr = [1,2,3,4,5,6,7,8]

    order = "ASCENDING ORDER"

    result = checkorder(arr, order)

    order = result[1]  

    context = {"data" : input, "header2": "Quick Sort", "header3": "Insertion Sort" ,"header": "Bubble Sort", "vec": mountain, "aspect": aspect, "vec2": mountain2, "aspect2": aspect2, "checkorder": [arr, order]}

    return render(request, "about.html", context)