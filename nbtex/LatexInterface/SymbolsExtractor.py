"Methods for extracting properties from: https://en.wikipedia.org/wiki/Wikipedia:LaTeX_symbols"
import re


def getNameSym(pasta):
    lst = []
    for l in pasta.split("\n"):
        r = re.search("{.*}", l)
        if r is not None:
            p = r.group()[1:-1]
            ps = p.split(" ")
            if len(ps) > 1 and ps[1] != "\\":
                lst.append(ps[1])
    return [(arg[1:], arg) for arg in lst]


def getDefs(l):
    for name, ap in l:
        name = ap[1:]
        print(
            f"""@property
def {name}(self):
    return Var(r'{ap}')"""
        )


def getProps(cl):
    l = []
    for v in vars(cl):
        if isinstance(vars(cl)[v], property):
            l.append(v)
    return l


def getWrappedProps(cl, objName):
    l = getProps(cl)
    s = ""
    for name in l:
        s += f"{objName}.{name} | "
    sx = f"wrap({s[:-2]})"
    s = "{{" + f"wrap({s[:-2]})" + "}}"
    return sx
