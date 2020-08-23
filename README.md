# NbTex  

A light-weight pythonic wrapper around LaTeX specifically to python-like interface to write mathemical latex in Jupyter Notebooks.   
**NOTE:** Only Jupyter Notebooks are supported. Tests done in notebooks too

You can create latex for:

+ `+`: Adding
+ `-`: Subtraction
+ `*`: Multiplication
+ `pow`: Exponents
+ `^`: Exponents (another way)
+ `/`: Fractions
+ `|`: Space in generated latex
+ `()`: Function calling with arbitrary args
+ `<`, `>`, `<=`, `>=`: Ordering operators
+ `==`, `!=`: Equal and Not Equal
+ `~`: Inversion of the topmost operator in the expression (eg: ~(x*y) will give LaTeX for division/fraction)
+ Matrices
+ Differentiation
+ Partial Differentiation
+ Integration
+ Integration over partials
+ Summation
+ Product
+ Vector notation

## Usage  
The usage is best presented by examples  
Look at the [docs](https://github.com/narang99/nbtex/tree/master/docs)   
**NOTE:** Jupyter Notebooks uploaded on github are making the rendered latex slightly weird. The generation in a normal notebook seems to be absolutely normal
