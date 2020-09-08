from nbtex.core.Ast import makeVar
class GreekSymbols:
    def __init__(self):
        pass

    @property
    def alpha(self):
        return makeVar(r"\alpha")

    @property
    def beta(self):
        return makeVar(r"\beta")

    @property
    def gamma(self):
        return makeVar(r"\gamma")

    @property
    def delta(self):
        return makeVar(r"\delta")

    @property
    def epsilon(self):
        return makeVar(r"\epsilon")

    @property
    def zeta(self):
        return makeVar(r"\zeta")

    @property
    def eta(self):
        return makeVar(r"\eta")

    @property
    def theta(self):
        return makeVar(r"\theta")

    @property
    def iota(self):
        return makeVar(r"\iota")

    @property
    def kappa(self):
        return makeVar(r"\kappa")

    @property
    def lambd(self):
        return makeVar(r"\lambda")

    @property
    def mu(self):
        return makeVar(r"\mu")

    @property
    def nu(self):
        return makeVar(r"\nu")

    @property
    def xi(self):
        return makeVar(r"\xi")

    @property
    def mathrm(self):
        return makeVar(r"\mathrm")

    @property
    def pi(self):
        return makeVar(r"\pi")

    @property
    def rho(self):
        return makeVar(r"\rho")

    @property
    def sigma(self):
        return makeVar(r"\sigma")

    @property
    def tau(self):
        return makeVar(r"\tau")

    @property
    def upsilon(self):
        return makeVar(r"\upsilon")

    @property
    def phi(self):
        return makeVar(r"\phi")

    @property
    def chi(self):
        return makeVar(r"\chi")

    @property
    def psi(self):
        return makeVar(r"\psi")

    @property
    def omega(self):
        return makeVar(r"\omega")

    @property
    def varepsilon(self):
        return makeVar(r"\varepsilon")

    @property
    def vartheta(self):
        return makeVar(r"\vartheta")

    @property
    def varkappa(self):
        return makeVar(r"\varkappa")

    @property
    def varpi(self):
        return makeVar(r"\varpi")

    @property
    def varrho(self):
        return makeVar(r"\varrho")

    @property
    def varphi(self):
        return makeVar(r"\varphi")

    @property
    def varsigma(self):
        return makeVar(r"\varsigma")

    @property
    def Gamma(self):
        return makeVar(r"\Gamma")

    @property
    def Delta(self):
        return makeVar(r"\Delta")

    @property
    def Theta(self):
        return makeVar(r"\Theta")

    @property
    def Lambda(self):
        return makeVar(r"\Lambda")

    @property
    def Upsilon(self):
        return makeVar(r"\Upsilon")

    @property
    def Xi(self):
        return makeVar(r"\Xi")

    @property
    def Phi(self):
        return makeVar(r"\Phi")

    @property
    def Pi(self):
        return makeVar(r"\Pi")

    @property
    def Psi(self):
        return makeVar(r"\Psi")

    @property
    def Sigma(self):
        return makeVar(r"\Sigma")

    @property
    def Omega(self):
        return makeVar(r"\Omega")

    @property
    def digamma(self):
        return makeVar(r"\digamma")

    @property
    def aleph(self):
        return makeVar(r"\aleph")

    @property
    def beth(self):
        return makeVar(r"\beth")

    @property
    def gimel(self):
        return makeVar(r"\gimel")

    @property
    def daleth(self):
        return makeVar(r"\daleth")

    @property
    def forall(self):
        return makeVar(r"\forall")

    @property
    def exists(self):
        return makeVar(r"\exists")

    @property
    def nexists(self):
        return makeVar(r"\nexists")

    @property
    def Finv(self):
        return makeVar(r"\Finv")

    @property
    def Game(self):
        return makeVar(r"\Game")

    @property
    def backepsilon(self):
        return makeVar(r"\backepsilon")

    @property
    def imath(self):
        return makeVar(r"\imath")

    @property
    def jmath(self):
        return makeVar(r"\jmath")

    @property
    def ell(self):
        return makeVar(r"\ell")

    @property
    def Bbbk(self):
        return makeVar(r"\Bbbk")

    @property
    def amalg(self):
        return makeVar(r"\amalg")

    @property
    def nabla(self):
        return makeVar(r"\nabla")

    @property
    def mho(self):
        return makeVar(r"\mho")

    @property
    def partial(self):
        return makeVar(r"\partial")

    @property
    def eth(self):
        return makeVar(r"\eth")

    @property
    def hbar(self):
        return makeVar(r"\hbar")

    @property
    def hslash(self):
        return makeVar(r"\hslash")

    @property
    def Im(self):
        return makeVar(r"\Im")

    @property
    def Re(self):
        return makeVar(r"\Re")

    @property
    def wp(self):
        return makeVar(r"\wp")

    @property
    def emptyset(self):
        return makeVar(r"\emptyset")

    @property
    def varnothing(self):
        return makeVar(r"\varnothing")

    @property
    def complement(self):
        return makeVar(r"\complement")

    @property
    def circledS(self):
        return makeVar(r"\circledS")


"default symbol lookup class, can change name later maybe"
Greek = GreekSymbols()