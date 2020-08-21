#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
Runtime: Linear time O(n)

Explanation: a increases by a + n^2 for each loop, but the while loop is n^3. As n grows absurdly large, the runtime will increase by 0(n).

b)

Runtime: Quadratic time O(n2)

Explanation: Loops through each item in range(n), which is linear o(n). And within that loop, another while loop is run so long as j (which is multiplied by 2 every time) is less than n - which is also linear o(n). 

c)

Runtime: Linear time 0(n)

Explanation: As size of the input increases, runtime will grow at the same rate. Function is called n times before reaching its base case. 


## Exercise II


Throw an egg from the first floor, the second floor, third floor, and so on. If the eggs breaks, we've found f. Worst case, this approach takes n amount of times. This approach optimizes for fewest number of broken eggs, but probably involves more throws. 

Runtime complexity: 0(n)

Maybe a more optimal answer for fewr drops but more breaks (better runtime):

Go to the middle floor (n/2) and throw an egg. If it does not break, find the middle floor of the top half of floors and throw another egg. If it breaks, find the middle floor of the bottom half of floors and throw another egg. Continue until youy find the lowest possible floor at which the egg breaks (f)

Runtime complexity: 0(logn)
