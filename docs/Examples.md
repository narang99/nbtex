# Pytex  

A light-weight pythonic wrapper around LaTeX specifically to provide python-like interface to write mathemical latex in Jupyter Notebooks.   
**NOTE:** Only Jupyter Notebooks are supported for now. Tests done in notebooks too

## Usage  
The usage is best presented by examples  
The next cells show some use cases

It is recommended to use the `Python-Markdown` extension to render the latex inside a markdown cell.  
You can enclose a python statement inside double curly braces (see Python-markdown on Jupyter website) `{ { statement } }`  inside a markdown cell if this extension is enable **and** the notebook is trusted.  

As an alternative: the function `latex` returns a `iPython.core.display.Latex` object. It has attribute `data` which can be printed in a code cell. This string can be enclosed in `$$ <output> $$` in a markdown cell

`platex` prints the latex that can be directly copy pasted inside a markdown cell.

## Variables

`Var` class is the basic class of the package which defines `+`,`-`, function calling etc. and constructs the LaTeX AST internally.  
Calling `latex` with any `Var` as argument gives the LaTeX in a platform dependent object. Since only Jupyter Notebooks are supported for now, it returns an `IPython.core.display.Latex` object


```python
from pytex import Var
from pytex.platforms.jupyter import latex
a = Var('a')
print(latex(a).data)
```

    \begin{gather}a\end{gather}


$$
\begin{gather}a\end{gather}
$$

`platex` prints the latex which can be put inside a markdown cell. we will use that


```python
from pytex.platforms.jupyter import platex
platex(a)
```

    \begin{gather}a\end{gather}


$$ \begin{gather}a\end{gather} $$

`makeVar` is a convenience function to create multiple `Var` variables easily.  
A list of operators supported:
+ `+`: Adding
+ `-`: Subtraction
+ `*`: Multiplication
+ `pow`: Exponents
+ `^`: Exponents (another way)
+ `==`: Equality (`=` cannot be used as assignment is a core feature of python)
+ `/`: Fractions
+ `|`: Space in generated latex
+ `()`: Function calling with arbitrary args
+ `<`, `>`, `<=`, `>=`: Ordering operators 


In some cases you can directly use literal constants (numbers, strings etc) like `'a', 'bc', 1, 2`. Use cases where this is safe will be discussed later.  
It is however usually safer to wrap all your constants inside `Var` using `makeVar` for concise syntax as shown below. (eg. binding const `2` to instance `_2` of `Var` as shown below)  
`Var` instances also can be called with arbitrary parameters for them to render as functions


```python
from pytex import makeVar
x,y,z,f,ab,_2 = makeVar('x','y','z','f','ab', 2)
op = f(x + y|z + ab) == x**2 + x + ab
platex(op)
```

    \begin{gather}f(x + y\hspace{1mm}z + ab) = x^2 + x + ab\end{gather}


$$ \begin{gather}f(x + y\hspace{1mm}z + ab) = x^2 + x + ab\end{gather} $$

Ordering Operators Example


```python
platex(x >= y)
```

    \begin{gather}x \geq y\end{gather}


$$ \begin{gather}x \geq y\end{gather} $$

String Argument passed to `Var` or `makeVar` is rendered in the latex. It is recommended to map arguments to approximately same names of `Var` instances


```python
a = Var('a')
b = Var('x')
c = makeVar('c')

# b will render as x in the latex, binding different names to variables is not recommended
platex(a == b + c)
```

    \begin{gather}a = x + c\end{gather}


$$ \begin{gather}a = x + c\end{gather} $$

`==` is overloaded version of `equals` method. Use whichever you prefer


```python
platex(a.equals(b + c))
```

    \begin{gather}a = x + c\end{gather}


You can also use Vectors. `Vector` class is used. `makeVector` convenience function similarly supported


```python
from pytex import Vector, makeVector
f,x,y = makeVector('f','x','y')
_1 = makeVar(1)
op = f(x,y) == x**y + x*y + _1
platex(op)
```

    \begin{gather}\vec{\mathbf{f}}(\vec{\mathbf{x}},\vec{\mathbf{y}}) = \vec{\mathbf{x}}^\vec{\mathbf{y}} + \vec{\mathbf{x}} * \vec{\mathbf{y}} + 1\end{gather}


$$ \begin{gather}\vec{\mathbf{f}}(\vec{\mathbf{x}},\vec{\mathbf{y}}) = \vec{\mathbf{x}}^\vec{\mathbf{y}} + \vec{\mathbf{x}} * \vec{\mathbf{y}} + 1\end{gather} $$

## Series

### Summation
**NOTE:** upper and lower limits are optional. (Shown in `Product`)


```python
from pytex import Sum
i, _1, _10 = makeVar('i', 1, 10)
op = Sum(i**2+i+1, i, _1, _10)
platex(op)
```

    \begin{gather}\sum_{i=1}^{10} i^2 + i + 1\end{gather}


$$ \begin{gather}\sum_{i=1}^{10} i^2 + i + 1\end{gather} $$

### Product


```python
from pytex import Product
i = makeVar('i')
op = Product(pow(i,2)+i+1, i)
platex(op)
```

    \begin{gather}\prod_{i} i^2 + i + 1\end{gather}


$$ \begin{gather}\prod_{i} i^2 + i + 1\end{gather} $$

## Derivatives and Partial Derivatives

Similar to `Var` we have `Derivative` and `Partial` implementations. `makeDerivative` and `makePartial` are parallel implementations of `makeVar`


```python
from pytex import makeDerivative

# NOTE: makeDerivative takes args in forms of tuples of size two
#       the first element in the tuple is the name of the differentiating variable
#       the second element is the degree of the variable
# NOTE: degree of 1 is not shown in latex

dx, dy = makeDerivative(('x', 1), ('y', 2))
x, y = makeVar('x', 'y')
op = dx | dy | x+y
platex(op)
```

    \begin{gather}\frac{d}{d x}\hspace{1mm}\frac{d^{2}}{d y^2}\hspace{1mm}x + y\end{gather}


$$ \begin{gather}\frac{d}{d x}\hspace{1mm}\frac{d^{2}}{d y^2}\hspace{1mm}x + y\end{gather}
 $$

You can use a more complex expression as differentiator too. Also shows an example of not equal


```python
x = makeVar('x')
f = (pow(x,2) + x + 1)
df = makeDerivative((f,2))

op = df | f != Var('2')
platex(op)
```

    \begin{gather}\frac{d^{2}}{d (x^2 + x + 1)^2}\hspace{1mm}x^2 + x + 1 \neq 2\end{gather}


$$ \begin{gather}\frac{d^{2}}{d (x^2 + x + 1)^2}\hspace{1mm}x^2 + x + 1 \neq 2\end{gather} $$

We used `|` for space between the variables. Calling `df` with `f` in the previous example will result in parenthesizing the function on which the differentiation operator acts.  
**NOTE:** The `=` here is normal python assignment to a new variable `op`. It wont be rendered as your latex. For that you either use `@` operator or the `equals` method


```python
op = df(f) != makeVar('2')
platex(op)
```

    \begin{gather}\frac{d^{2}}{d (x^2 + x + 1)^2}(x^2 + x + 1) \neq 2\end{gather}


$$ \begin{gather}\frac{d^{2}}{d (x^2 + x + 1)^2}(x^2 + x + 1) \neq 2\end{gather} $$


Same example with Partial


```python
from pytex import makePartial
x = makeVar('x')
f = pow(x,2) + x + 1
df = makePartial((f,3))

op = df | f == Var('1')
platex(op)
```

    \begin{gather}\frac{\partial ^{3}}{\partial  (x^2 + x + 1)^3}\hspace{1mm}x^2 + x + 1 = 1\end{gather}


$$ \begin{gather}\frac{\partial ^{3}}{\partial  (x^2 + x + 1)^3}\hspace{1mm}x^2 + x + 1 = 1\end{gather} $$

## Matrices and Vectors

You can make both matrices and vectors with a single class `Matrix` by giving appropriate dimensions  
`MatrixBuilder` provides a builder pattern API to create a Matrix.  

For `Matrix`, pass a list representing a matrix with appropriate dimensions


```python
from pytex import Matrix
# simple row vector
platex(Matrix([1,2,3]))
```

    \begin{gather}\begin{bmatrix} 1 &  2 &  3 \end{bmatrix}\end{gather}


$$ \begin{gather}\begin{bmatrix} 1 &  2 &  3 \end{bmatrix}\end{gather} $$


```python
# simple column vector
m = [[1],[2],[3]]
platex(Matrix(m))
```

    \begin{gather}\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}\end{gather}


$$ \begin{gather}\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}\end{gather}$$


```python
# adding subscript and powers
platex(Matrix(m, '3x1', 2))
```

    \begin{gather}\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}^{2}_{3x1}\end{gather}


$$  \begin{gather}\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}^{2}_{3x1}\end{gather} $$


```python
# different types of brackets, default is [] -> square brackets
# Passing anything else in surround renders the matrix without a border
platex(Matrix(m, surround='()') | Matrix(m, surround='||') | Matrix(m, surround='||||'))
```

    \begin{gather}\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}\hspace{1mm}\begin{vmatrix} 1 \\ 2 \\ 3 \end{vmatrix}\hspace{1mm}\begin{Vmatrix} 1 \\ 2 \\ 3 \end{Vmatrix}\end{gather}


$$ \begin{gather}\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}\hspace{1mm}\begin{vmatrix} 1 \\ 2 \\ 3 \end{vmatrix}\hspace{1mm}\begin{Vmatrix} 1 \\ 2 \\ 3 \end{Vmatrix}\end{gather} $$

A more complex matrix example


```python
from pytex import makePartial, makeVar, Matrix
from pytex.platforms.jupyter import latex
du, dv = makePartial('u', 'v')
X, Y = makeVar('X', 'Y')
l = [
    ['i', 'j', 'k'],
    [du|X, du|Y, 0],
    [dv|X, dv|Y, 0]
]
platex(Matrix(l, subscript='3x3', power=2,surround='||'))
```

    \begin{gather}\begin{vmatrix} i &  j &  k \\ \frac{\partial }{\partial  u}\hspace{1mm}X &  \frac{\partial }{\partial  u}\hspace{1mm}Y &  0 \\ \frac{\partial }{\partial  v}\hspace{1mm}X &  \frac{\partial }{\partial  v}\hspace{1mm}Y &  0 \end{vmatrix}^{2}_{3x3}\end{gather}


$$ \begin{gather}\begin{vmatrix} i &  j &  k \\ \frac{\partial }{\partial  u}\hspace{1mm}X &  \frac{\partial }{\partial  u}\hspace{1mm}Y &  0 \\ \frac{\partial }{\partial  v}\hspace{1mm}X &  \frac{\partial }{\partial  v}\hspace{1mm}Y &  0 \end{vmatrix}^{2}_{3x3}\end{gather} $$

Same example with `MatrixBuilder`


```python
# from pytex import MatrixBuilder
from pytex import makePartial, makeVar, Matrix
from pytex.platforms.jupyter import latex
du, dv = makePartial('u', 'v')
X, Y = makeVar('X', 'Y')

m = (Matrix.builder()
    .add('i','j','k')
    .add(du|X, du|Y, 0)
    .add(dv|X, dv|Y, 0)
    .create(subscript='3x3', power=2, surround='||'))
platex(m)
```

    \begin{gather}\begin{vmatrix} i &  j &  k \\ \frac{\partial }{\partial  u}\hspace{1mm}X &  \frac{\partial }{\partial  u}\hspace{1mm}Y &  0 \\ \frac{\partial }{\partial  v}\hspace{1mm}X &  \frac{\partial }{\partial  v}\hspace{1mm}Y &  0 \end{vmatrix}^{2}_{3x3}\end{gather}


$$ \begin{gather}\begin{vmatrix} i &  j &  k \\ \frac{\partial }{\partial  u}\hspace{1mm}X &  \frac{\partial }{\partial  u}\hspace{1mm}Y &  0 \\ \frac{\partial }{\partial  v}\hspace{1mm}X &  \frac{\partial }{\partial  v}\hspace{1mm}Y &  0 \end{vmatrix}^{2}_{3x3}\end{gather} $$

`MatrixWithDots` is also best explained by example


```python
from pytex import MatrixWithDots, makeVector, makeVar, makePartial
# Jacobian matrix

f, J = makeVector('f', 'J')
f1, fm = makeVar('f_1', 'f_m')
dx1, dxn = makePartial(('x_1',), ('x_n',))
op = J == MatrixWithDots([[dx1|f, dxn|f]])
platex(op)
```

    \begin{gather}\vec{\mathbf{J}} = \begin{bmatrix} \frac{\partial }{\partial  x_1}\hspace{1mm}\vec{\mathbf{f}} &  \cdots &  \frac{\partial }{\partial  x_n}\hspace{1mm}\vec{\mathbf{f}} \end{bmatrix}\end{gather}


$$ \begin{gather}\vec{\mathbf{J}} = \begin{bmatrix} \frac{\partial }{\partial  x_1}\hspace{1mm}\vec{\mathbf{f}} &  \cdots &  \frac{\partial }{\partial  x_n}\hspace{1mm}\vec{\mathbf{f}} \end{bmatrix}\end{gather} $$


```python
ll = [
    [dx1 | f1, dxn | f1],
    [dx1 | fm, dxn | fm],
]
op2 = op == MatrixWithDots(ll, shape=(3,3))
platex(op2)
```

    \begin{gather}\begin{bmatrix} \frac{\partial }{\partial  x_1}\hspace{1mm}f_1 &  \cdots &  \frac{\partial }{\partial  x_n}\hspace{1mm}f_1 \\ \vdots &  \ddots &  \vdots \\ \frac{\partial }{\partial  x_1}\hspace{1mm}f_m &  \cdots &  \frac{\partial }{\partial  x_n}\hspace{1mm}f_m \end{bmatrix} = \vec{\mathbf{J}} = \begin{bmatrix} \frac{\partial }{\partial  x_1}\hspace{1mm}\vec{\mathbf{f}} &  \cdots &  \frac{\partial }{\partial  x_n}\hspace{1mm}\vec{\mathbf{f}} \end{bmatrix}\end{gather}


$$ \begin{gather}\begin{bmatrix} \frac{\partial }{\partial  x_1}\hspace{1mm}f_1 &  \cdots &  \frac{\partial }{\partial  x_n}\hspace{1mm}f_1 \\ \vdots &  \ddots &  \vdots \\ \frac{\partial }{\partial  x_1}\hspace{1mm}f_m &  \cdots &  \frac{\partial }{\partial  x_n}\hspace{1mm}f_m \end{bmatrix} = \vec{\mathbf{J}} = \begin{bmatrix} \frac{\partial }{\partial  x_1}\hspace{1mm}\vec{\mathbf{f}} &  \cdots &  \frac{\partial }{\partial  x_n}\hspace{1mm}\vec{\mathbf{f}} \end{bmatrix}\end{gather} $$

`MatrixWithDots` is good with placing dots only when the list size is not the same as the shape passed. By default, it makes one extra row and one extra column unless size of the dimension is 1, in that case it makes a single row/column. For more than 1 size, it puts the last element in the row to the last column at that row and puts dots between them. Same for columns

The library provides many of the LaTeX math symbols by the same name with some exceptions in case of a name clash with python keyword (eg. `lambda`)


```python
from pytex import Greek as G, Set as st, Operator as opr
```


```python
op = G.beta | st.subseteq | G.Delta | opr.approxeq | Var('x') + 1
platex(op)
```

    \begin{gather}\beta\hspace{1mm}\subseteq\hspace{1mm}\Delta\hspace{1mm}\approxeq\hspace{1mm}x + 1\end{gather}


$$ \begin{gather}\beta\hspace{1mm}\subseteq\hspace{1mm}\Delta\hspace{1mm}\approxeq\hspace{1mm}x + 1\end{gather} $$
