#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This will run forever, except in the case that n = 0. then it is constant (steps = test).

If n is a size of input, it must be >= 0.
So, n^3 will be >= 0 (call it z)
So, a (==0) will always (except in one edge case, where n = 0) be less than z.



b) O(n) = n^2 
   Except in edge case: n == 0, where order is O(1)
   The outer for loop is O(n)
   Within that, the loop up to n is O(n).
   So, an O(n) running O(n) times.
  
   


c) O(n) = n^n

Hard problem.

In the edge case (n = 0) it is constant.

Above that, it gets hyperexponentially complex.



## Exercise II


very Totally Simplest: set dropped == 0.  actually O(0)



If success increases with unbroken drops, bu tnot with height:

Test floor zero.  If an egg breaks, stop. If it does not break, drop all from here.

O(1)



If success is some product of unbroken drops and floor dropped from, use the bracketing strategy.


Initially set high to n, and low to zero.
Test boundaries: as above, 
    if they break from floor 0:
        halt
    elif they don't break from the penthouse:
        halt testing and drop away.
    else:
       recurse:
           Set new test floor (f) to low + ((high - low) / 2)
           If no break: 
              set new low to f
              recurse
        If breakage:
            set new high to f
            recurse
        (halt recursion wen high == low + 1)
    
 O(logn)