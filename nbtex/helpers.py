def varArgFunc(func, *args):
    if len(args) == 1:
        return func(args[0])
    return [func(arg) for arg in args]
