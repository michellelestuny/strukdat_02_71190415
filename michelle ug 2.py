import random
import timeit

#rekrusif
    
def fibonacci (n):
  if n < 1:
    return [n]

  return fibonacci(n - 1) + [n]

for i in range(1,101):
    start = timeit.default_timer()
    hasil = fibonacci(i)
    end = timeit.default_timer()
    print('Ukuran ', hasil, ': ', end-start, ' second.')

#iteratif
    
FibArray = [0, 1]
 
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n < len(FibArray):
        return FibArray[n]
    else:       
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]

for i in range(1,101):
    start = timeit.default_timer()
    hasil = fibonacci(i)
    end = timeit.default_timer()
    print('Ukuran ', hasil, ': ', end-start, ' second.')

              
