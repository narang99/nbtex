# nbTeX  

A light-weight pythonic wrapper around LaTeX specifically to python-like interface to write mathemical latex in Jupyter Notebooks.   
**NOTE:** Only Jupyter Notebooks are supported. Tests done in notebooks too  

## Motivation

A lot of us in data science extensively use notebooks and sometimes have to write some latex in markdown. Most of us are not familiar with LaTeX. Therefore instead of going on a hunt for LaTeX on the internet, you can use this library for writing LaTeX in a pythonic manner.   
**NOTE:** We only support Math LaTeX because Jupyter Notebook users normally do other stuff in normal markdown and not in LaTeX.

## Features

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
