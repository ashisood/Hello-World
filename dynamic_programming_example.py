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
            #print("from memo")
            return memo[n]

        if n == 1 or n == 2:
            result = 1
        else:
            result = fib(n - 1, memo) + fib(n - 2, memo)
            memo[n] = result
        #print("after recursion")
        return result

    return fib(n, memo)


def fib2(n):
    memo = [None] * (n + 1)
    #print(memo)
    if n > 2:
        memo[2] = memo[1] = 1
    else:
        return 1

    for i in range(3, len(memo)):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


if __name__ == '__main__':
    import timeit

    f = fib(10)
    print(f"recursive fib(10)={f}")
    f = fib1(10)
    print(f"recursive with memo fib(10)={f}")
    f = fib2(10)
    print(f"iterative with memo fib(10)={f}")
    t1 = timeit.timeit("fib(10)", setup="from __main__ import fib")
    t2 = timeit.timeit("fib1(100)", setup="from __main__ import fib1")
    t3 = timeit.timeit("fib2(1000)", setup="from __main__ import fib2")
    print(f"recursive fib(10) {t1}")
    print(f"recursive with memo fib1(10) {t2}")
    print(f"iterative with memo fib2(10) {t3}")

