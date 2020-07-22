f = open("output.txt", "a")


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def twin_primes(digit):
    start = pow(10, digit-1)
    end = pow(10, digit)
    for i in range(start, end):
        j = i + 2
        if is_prime(i) and is_prime(j):
            f.write(str(i) + " " + str(j) + "\n")


d = input()
f.write('The following lines contains all the twin prime numbers of ' + d + ' digits' + "\n")
twin_primes(int(d))
f.close()
