# 1*2*3*...N
def fact(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1
    return fact(N-1) * N

# count string
def lenOfString(str):
    if not str:
        return 0
    return 1 + lenOfString(str[1:])

# sum of a list integer
def sumList(numlist):
    if not numlist:
        return 0
    return numlist[0] + sumList(numlist[1:])

#Dynamic programming with Recursion
#• Break a large problem into smaller problems recursively.
#• Avoid solving the same problem again.
#• Prefer lookup solutions instead of solving problems.
#• Save the solution of problems for later lookup.

def fibonacciDP(N, result=[]):
    # extend the result list and fill with 0
    result.extend([0] * (N - len(result) + 1))
    # base case
    if N == 0 or N == 1:
        return 1
    # lookup the list for results
    if result[N-1] == 0:
        result[N-1] = fibonacciDP(N-1, result) # if fib(N-1) not found
    if result[N-2] == 0:
        result[N-2] = fibonacciDP(N-2, result) # if fib(N-2) not found
    # calculate fib(N) and store the result in the list
    result[N] = result[N-1] + result[N-2]
    print(result)
    return result[N]

if __name__ == "__main__":
    result = fact(10)
    print(result) # factorial of 10

    s1 = "COMPUTER"
    result = lenOfString(s1)
    print(result) # count string

    numlist = [6, 5, 2, 1, 8, 9, 8, 6, 0, 4]
    result = sumList(numlist)
    print(result) # sum of a list integer

    fibonacciDP(10) # Dynamic programming with Recursion
