# `__future__` module

#1. Interpretation
When we read the code, especially, when we read some old version code. We would always see 
the `__future__` at the beginning of code. This module is to let us can use some new&latest
futures of new version python in the old version of python. 

I.g. The `print` function in python 2.x and python 3.x are different.
```python
# python 2.x 
print "Hello World"

# python 3.x
print("Hello World")
```
Assuming our current python version is python 2.x, thus, if we want to use `print` function
with the format of python 3.x, then we can use `__future__` module. 
```python
# python 2.x
from __future__ import print_function
print("Hello World")
```
**IMPORTANT:**
Moreover, after we import `__future__` module, if we are still going to use the format of python 2.x,
the there is an error when we try to execute the code.

# 2. Extension
Some other functions in `__future__` module:
1. `division`
```python
# python 2.x
5/2
>>> 2

from __future__ import division
5/2

>>> 2.5
```
2. `with`
```python
# python 2.x
try:
    with open('text.txt', 'w') as f:
        f.write('Hello World')
finally:
    f.close()

from __future__ import with_statement
with open('test.txt', 'w') as f:
    f.write('Hi There!')
```
# 3. `absolute_import`
This function is aim at the python version before 2.4, when we import a `.py` file, Python would 
check if the `.py` is in the current work directory. Thus, if we want to import the original `.py` (in Python module),
we can use `from __future__ import absolute_import`
