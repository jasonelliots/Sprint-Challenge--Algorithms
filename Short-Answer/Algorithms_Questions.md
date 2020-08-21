# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
Runtime: Linear time O(n)

Explanation: a increases by a + n^2 for each loop, but the while loop is n^3. As n grows absurdly large, the runtime will increase by 0(n). 

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

Runtime: Quadratic time O(n2)

Explanation: Loops through each item in range(n), which is linear o(n). And within that loop, another while loop is run so long as j (which is multiplied by 2 every time) is less than n - which is also linear o(n). 

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
Runtime: Linear time 0(n)

Explanation: As size of the input increases, runtime will grow at the same rate


## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

n = stories of the building

f = lowest floor at which an egg is broken if thrown off 


Throw an egg from the first floor, the second floor, third floor, and so on. If the eggs breaks, we've found f. Worst case, this approach takes n amount of times. This approach optimizes for fewest number of broken eggs, but probably involves more throws. 

Runtime complexity: 0(n)

Maybe a more optimal answer for less drops but more breaks (better runtime):

Go to the middle floor (n/2) and throw an egg. If it does not break, find the middle floor of the top half of floors and throw another egg. If it breaks, find the middle floor of the bottom half of floors and throw another egg. Continue until youy find the lowest possible floor at which the egg breaks (f)

Runtime complexity: 0(logn)


