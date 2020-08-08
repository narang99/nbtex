# Pytex  

A light-weight pythonic wrapper around LaTeX specifically to provide python-like interface to write mathemical latex in Jupyter Notebooks.   
**NOTE:** Only Jupyter Notebooks are supported for now. Tests done in notebooks too

## Usage  
The usage is best presented by examples

### Examples

```python
from pytex import makeVar, wrap
a,b,c,d = makeVar('a','b','c','d')
wrap(a | b | c | d)

```
