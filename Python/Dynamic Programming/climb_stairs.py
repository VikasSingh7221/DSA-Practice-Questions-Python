# // Given an integer n, there is a staircase with n steps, starting from the 0th step.
# // Determine the number of unique ways to reach the nth step, 
# // given that each move can be either 1 or 2 steps at a time.


n = 6

def f(n):
    if n == 0 or n == 1:
        return n
    return f(n-1) + f(n-2)


for i in range(0,10):
    print(f(i),end = ' ')
print()