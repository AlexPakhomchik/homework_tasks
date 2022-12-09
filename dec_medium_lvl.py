def fil_1(filt):
    def fil_2(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            for i in list(args):
                if filt in i:
                    raise ValueError
        return wrapper
    return fil_2


@fil_1(filt='Oleg')
def qwe(a, b, c):
    pass



