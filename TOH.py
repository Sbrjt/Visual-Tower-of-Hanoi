import os


def TOH(N):

    A = list(range(1, N + 1))
    B = []
    C = []

    # f -> recursive function; g -> for printing

    def f(n, a, b, c):

        if n == 1:
            x = a.pop(0)
            c.insert(0, x)

            input('\x1b[3mPress Enter...\x1b[0m\t')
            g()

        else:
            f(n - 1, a, c, b)  # a -> b
            f(1, a, b, c)  # a -> c
            f(n - 1, b, a, c)  # b -> c

    def g():
        os.system('cls')

        print('A')
        for i in range(N - len(A)):
            print()
        for i in A:
            print(' ' * (N - i), end='')
            print('_' * 2 * i, end='')
            print()

        print('\nB')
        for i in range(N - len(B)):
            print()
        for i in B:
            print(' ' * (N - i), end='')
            print('_' * 2 * i, end='')
            print()

        print('\nC')
        for i in range(N - len(C)):
            print()
        for i in C:
            print(' ' * (N - i), end='')
            print('_' * 2 * i, end='')
            print()
        print()

    g()
    f(N, A, B, C)
    print('Done! 🎉')


n = int(input('\033[1m\033[4m\x1b[3mTower of Hanoi\n\x1b[0mEnter no. of disks: '))
TOH(n)
