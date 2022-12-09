def dec(func):
    def revers(*args):
        func(*args)
        print(*args)
    return revers


@dec
def empty(*args):
    pass


empty(1, 2, 3, 21312, 23, 3123, 2233)
