def func(n):
    sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
    
    return sum 

# print(func(5))

# print(func(33))


def func2(n):
    a = 0
    i = 0 
    while (a < n * n * n):
      a = a + n * n
      i += 1
    return i



def bunnyEars(bunnies):
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies-1)

print(bunnyEars(500))