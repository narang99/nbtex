from IPython.display import Latex


def addEnv(s, env="gather*"):
    env = "{" + env + "}"
    return r"\begin" + env + str(s) + r"\end" + env


def latex(v):
    return Latex(addEnv(v.build()))


def platex(v, returnLatexObject=True):
    l = Latex(addEnv(v.build()))
    print(l.data)
    if returnLatexObject:
        return l
