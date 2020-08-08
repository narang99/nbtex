from IPython.display import Latex
def addEnv(s, env='gather'):
    env = '{' + env + '}'
    return r'\begin' + env + str(s) + r'\end' + env
def latex(v):
    return Latex(addEnv(v.build()))
