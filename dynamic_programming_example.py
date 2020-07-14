import timeit


def fib(n):
    result = 0
    if n == 1 or n == 2:
        return 1
    else:
        result += (fib(n - 1) + fib(n - 2))
    return result


def fib1(n):
    memo = [None] * (n + 1)

    def fib(n, memo):
        """
        :type memo: object
        """
        if memo[n] is not None:
            print("from memo")
            return memo[n]

        if n == 1 or n == 2:
            result = 1
        else:
            result = fib(n - 1, memo) + fib(n - 2, memo)
            memo[n] = result
        print("after recursion")
        return result

    return fib(n, memo)


def fib2(n):
    memo = [None] * (n + 1)
    print(memo)
    if n > 2:
        memo[2] = memo[1] = 1
    else:
        return 1

    for i in range(3, len(memo)):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]
print(fib(5))
print(fib1(100))
print(fib2(100))

if __name__ == '__main1__':
    import timeit

    f = fib(10)
    print(f)
    f = fib1(10)
    print(f)
    f = fib2(10)
    print(f)
    t1 = timeit.timeit("fib(10)", setup="from __main__ import fib")
    t2 = timeit.timeit("fib1(10)", setup="from __main__ import fib1")
    t3 = timeit.timeit("fib2(10)", setup="from __main__ import fib2")
    print(t1)
    print(t2)
    print(t3)

