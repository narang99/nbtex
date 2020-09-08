from nbtex.core.Ast import makeVar
class SetSymbols:
    def __init__(self):
        pass

    @property
    def Subset(self):
        return makeVar(r"\Subset")

    @property
    def sqsubset(self):
        return makeVar(r"\sqsubset")

    @property
    def triangleleft(self):
        return makeVar(r"\triangleleft")

    @property
    def blacktriangleleft(self):
        return makeVar(r"\blacktriangleleft")

    @property
    def supset(self):
        return makeVar(r"\supset")

    @property
    def Supset(self):
        return makeVar(r"\Supset")

    @property
    def sqsupset(self):
        return makeVar(r"\sqsupset")

    @property
    def triangleright(self):
        return makeVar(r"\triangleright")

    @property
    def blacktriangleright(self):
        return makeVar(r"\blacktriangleright")

    @property
    def cap(self):
        return makeVar(r"\cap")

    @property
    def Cap(self):
        return makeVar(r"\Cap")

    @property
    def sqcap(self):
        return makeVar(r"\sqcap")

    @property
    def vartriangle(self):
        return makeVar(r"\vartriangle")

    @property
    def blacktriangle(self):
        return makeVar(r"\blacktriangle")

    @property
    def cup(self):
        return makeVar(r"\cup")

    @property
    def Cup(self):
        return makeVar(r"\Cup")

    @property
    def sqcup(self):
        return makeVar(r"\sqcup")

    @property
    def triangledown(self):
        return makeVar(r"\triangledown")

    @property
    def blacktriangledown(self):
        return makeVar(r"\blacktriangledown")

    @property
    def In(self):
        return makeVar(r"\in")

    @property
    def subseteq(self):
        return makeVar(r"\subseteq")

    @property
    def subseteqq(self):
        return makeVar(r"\subseteqq")

    @property
    def sqsubseteq(self):
        return makeVar(r"\sqsubseteq")

    @property
    def ni(self):
        return makeVar(r"\ni")

    @property
    def supseteq(self):
        return makeVar(r"\supseteq")

    @property
    def supseteqq(self):
        return makeVar(r"\supseteqq")

    @property
    def sqsupseteq(self):
        return makeVar(r"\sqsupseteq")

    @property
    def notin(self):
        return makeVar(r"\notin")

    @property
    def nsubseteq(self):
        return makeVar(r"\nsubseteq")

    @property
    def subsetneq(self):
        return makeVar(r"\subsetneq")

    @property
    def varsubsetneq(self):
        return makeVar(r"\varsubsetneq")

    @property
    def nsubseteqq(self):
        return makeVar(r"\nsubseteqq")

    @property
    def subsetneqq(self):
        return makeVar(r"\subsetneqq")

    @property
    def varsubsetneqq(self):
        return makeVar(r"\varsubsetneqq")

    @property
    def uplus(self):
        return makeVar(r"\uplus")

    @property
    def nsupseteq(self):
        return makeVar(r"\nsupseteq")

    @property
    def supsetneq(self):
        return makeVar(r"\supsetneq")

    @property
    def varsupsetneq(self):
        return makeVar(r"\varsupsetneq")

    @property
    def nsupseteqq(self):
        return makeVar(r"\nsupseteqq")

    @property
    def supsetneqq(self):
        return makeVar(r"\supsetneqq")

    @property
    def varsupsetneqq(self):
        return makeVar(r"\varsupsetneqq")


Set = SetSymbols()