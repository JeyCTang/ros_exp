# The Note of absl-python library

- The [official documentation](https://abseil.io/docs/python/quickstart)
- [Youtube](https://abseil.io/docs/python/quickstart) video for details interpretation

Briefly to say, absel-py is a command-line tool. When we try to run the program (we definitely did that before),
we might do the command like the following(here we use python):
```Python
python demo.py --name "xxxxx" --num 10
```
The parameters we typed after `demo.py` are what we have done with `absl-py` in the code. Those parameters are
called flags. 

I wrote an example in `demo01.py`, I think the problem is to understand the concept of `absl-py` and know what
is the usage. 

One thing I want to say is how to implement `absl-py` command when we run the program. In the official
documentation, we don't have to install `Bazel` to build the bazel files. We can just run the program like this:
```python
python demo01.py -name="Jey" -num_times=10
python demo01.py --name=Jey --num_times=10 
python demo01.py --name Jey --num_times 10
python demo01.py -name Jey -num_times 10
python demo01.py -name=Jey -num_times=10
```
Those above 5 commands are the same, for string, we can either use double quotations ("") or not.