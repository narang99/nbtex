from nbtex.core.Ast import makeVar
class OperatorSymbols:
    def __init__(self):
        pass

    @property
    def plus(self):
        return makeVar("+")

    @property
    def minus(self):
        return makeVar("-")

    @property
    def multiply(self):
        return makeVar("*")

    @property
    def power(self):
        return makeVar("^")

    @property
    def space(self):
        return makeVar("\\hspace{1mm}")

    @property
    def eq(self):
        return makeVar("=")

    @property
    def lt(self):
        return makeVar("<")

    @property
    def leq(self):
        return makeVar(r"\leq")

    @property
    def leqq(self):
        return makeVar(r"\leqq")

    @property
    def leqslant(self):
        return makeVar(r"\leqslant")

    @property
    def gt(self):
        return makeVar(">")

    @property
    def geq(self):
        return makeVar(r"\geq")

    @property
    def geqq(self):
        return makeVar(r"\geqq")

    @property
    def geqslant(self):
        return makeVar(r"\geqslant")

    @property
    def nless(self):
        return makeVar(r"\nless")

    @property
    def nleq(self):
        return makeVar(r"\nleq")

    @property
    def lneq(self):
        return makeVar(r"\lneq")

    @property
    def nleqq(self):
        return makeVar(r"\nleqq")

    @property
    def lneqq(self):
        return makeVar(r"\lneqq")

    @property
    def lvertneqq(self):
        return makeVar(r"\lvertneqq")

    @property
    def nleqslant(self):
        return makeVar(r"\nleqslant")

    @property
    def ngtr(self):
        return makeVar(r"\ngtr")

    @property
    def ngeq(self):
        return makeVar(r"\ngeq")

    @property
    def gneq(self):
        return makeVar(r"\gneq")

    @property
    def ngeqq(self):
        return makeVar(r"\ngeqq")

    @property
    def gneqq(self):
        return makeVar(r"\gneqq")

    @property
    def gvertneqq(self):
        return makeVar(r"\gvertneqq")

    @property
    def ngeqslant(self):
        return makeVar(r"\ngeqslant")

    @property
    def vartriangleleft(self):
        return makeVar(r"\vartriangleleft")

    @property
    def trianglelefteq(self):
        return makeVar(r"\trianglelefteq")

    @property
    def lesssim(self):
        return makeVar(r"\lesssim")

    @property
    def lessapprox(self):
        return makeVar(r"\lessapprox")

    @property
    def prec(self):
        return makeVar(r"\prec")

    @property
    def preceq(self):
        return makeVar(r"\preceq")

    @property
    def precsim(self):
        return makeVar(r"\precsim")

    @property
    def precapprox(self):
        return makeVar(r"\precapprox")

    @property
    def vartriangleright(self):
        return makeVar(r"\vartriangleright")

    @property
    def trianglerighteq(self):
        return makeVar(r"\trianglerighteq")

    @property
    def gtrsim(self):
        return makeVar(r"\gtrsim")

    @property
    def gtrapprox(self):
        return makeVar(r"\gtrapprox")

    @property
    def succ(self):
        return makeVar(r"\succ")

    @property
    def succeq(self):
        return makeVar(r"\succeq")

    @property
    def succsim(self):
        return makeVar(r"\succsim")

    @property
    def succapprox(self):
        return makeVar(r"\succapprox")

    @property
    def ntriangleleft(self):
        return makeVar(r"\ntriangleleft")

    @property
    def ntrianglelefteq(self):
        return makeVar(r"\ntrianglelefteq")

    @property
    def lnsim(self):
        return makeVar(r"\lnsim")

    @property
    def lnapprox(self):
        return makeVar(r"\lnapprox")

    @property
    def nprec(self):
        return makeVar(r"\nprec")

    @property
    def npreceq(self):
        return makeVar(r"\npreceq")

    @property
    def precnsim(self):
        return makeVar(r"\precnsim")

    @property
    def precnapprox(self):
        return makeVar(r"\precnapprox")

    @property
    def ntriangleright(self):
        return makeVar(r"\ntriangleright")

    @property
    def ntrianglerighteq(self):
        return makeVar(r"\ntrianglerighteq")

    @property
    def gnsim(self):
        return makeVar(r"\gnsim")

    @property
    def gnapprox(self):
        return makeVar(r"\gnapprox")

    @property
    def nsucc(self):
        return makeVar(r"\nsucc")

    @property
    def nsucceq(self):
        return makeVar(r"\nsucceq")

    @property
    def succnsim(self):
        return makeVar(r"\succnsim")

    @property
    def succnapprox(self):
        return makeVar(r"\succnapprox")

    @property
    def eqslantless(self):
        return makeVar(r"\eqslantless")

    @property
    def lessgtr(self):
        return makeVar(r"\lessgtr")

    @property
    def lesseqgtr(self):
        return makeVar(r"\lesseqgtr")

    @property
    def lesseqqgtr(self):
        return makeVar(r"\lesseqqgtr")

    @property
    def eqslantgtr(self):
        return makeVar(r"\eqslantgtr")

    @property
    def gtrless(self):
        return makeVar(r"\gtrless")

    @property
    def gtreqless(self):
        return makeVar(r"\gtreqless")

    @property
    def gtreqqless(self):
        return makeVar(r"\gtreqqless")

    @property
    def ll(self):
        return makeVar(r"\ll")

    @property
    def lll(self):
        return makeVar(r"\lll")

    @property
    def lessdot(self):
        return makeVar(r"\lessdot")

    @property
    def preccurlyeq(self):
        return makeVar(r"\preccurlyeq")

    @property
    def curlyeqprec(self):
        return makeVar(r"\curlyeqprec")

    @property
    def gg(self):
        return makeVar(r"\gg")

    @property
    def ggg(self):
        return makeVar(r"\ggg")

    @property
    def gtrdot(self):
        return makeVar(r"\gtrdot")

    @property
    def succcurlyeq(self):
        return makeVar(r"\succcurlyeq")

    @property
    def curlyeqsucc(self):
        return makeVar(r"\curlyeqsucc")

    @property
    def neq(self):
        return makeVar(r"\neq")

    @property
    def equiv(self):
        return makeVar(r"\equiv")

    @property
    def thickapprox(self):
        return makeVar(r"\thickapprox")

    @property
    def approx(self):
        return makeVar(r"\approx")

    @property
    def approxeq(self):
        return makeVar(r"\approxeq")

    @property
    def cong(self):
        return makeVar(r"\cong")

    @property
    def ncong(self):
        return makeVar(r"\ncong")

    @property
    def sim(self):
        return makeVar(r"\sim")

    @property
    def thicksim(self):
        return makeVar(r"\thicksim")

    @property
    def nsim(self):
        return makeVar(r"\nsim")

    @property
    def simeq(self):
        return makeVar(r"\simeq")

    @property
    def backsim(self):
        return makeVar(r"\backsim")

    @property
    def backsimeq(self):
        return makeVar(r"\backsimeq")

    @property
    def eqsim(self):
        return makeVar(r"\eqsim")

    @property
    def doteq(self):
        return makeVar(r"\doteq")

    @property
    def div(self):
        return makeVar(r"\div")

    @property
    def doteqdot(self):
        return makeVar(r"\doteqdot")

    @property
    def fallingdotseq(self):
        return makeVar(r"\fallingdotseq")

    @property
    def risingdotseq(self):
        return makeVar(r"\risingdotseq")

    @property
    def triangleq(self):
        return makeVar(r"\triangleq")

    @property
    def circeq(self):
        return makeVar(r"\circeq")

    @property
    def eqcirc(self):
        return makeVar(r"\eqcirc")

    @property
    def bumpeq(self):
        return makeVar(r"\bumpeq")

    @property
    def Bumpeq(self):
        return makeVar(r"\Bumpeq")

    @property
    def asymp(self):
        return makeVar(r"\asymp")

    @property
    def mid(self):
        return makeVar(r"\mid")

    @property
    def shortmid(self):
        return makeVar(r"\shortmid")

    @property
    def vdash(self):
        return makeVar(r"\vdash")

    @property
    def dashv(self):
        return makeVar(r"\dashv")

    @property
    def Vdash(self):
        return makeVar(r"\Vdash")

    @property
    def parallel(self):
        return makeVar(r"\parallel")

    @property
    def shortparallel(self):
        return makeVar(r"\shortparallel")

    @property
    def vDash(self):
        return makeVar(r"\vDash")

    @property
    def Vvdash(self):
        return makeVar(r"\Vvdash")

    @property
    def models(self):
        return makeVar(r"\models")

    @property
    def nmid(self):
        return makeVar(r"\nmid")

    @property
    def nshortmid(self):
        return makeVar(r"\nshortmid")

    @property
    def nvdash(self):
        return makeVar(r"\nvdash")

    @property
    def nVdash(self):
        return makeVar(r"\nVdash")

    @property
    def nparallel(self):
        return makeVar(r"\nparallel")

    @property
    def nshortparallel(self):
        return makeVar(r"\nshortparallel")

    @property
    def nvDash(self):
        return makeVar(r"\nvDash")

    @property
    def nVDash(self):
        return makeVar(r"\nVDash")


Operator = OperatorSymbols()