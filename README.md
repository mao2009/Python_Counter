# Counter

Counter is altanative for range and enumrator.

## Install

`pip install counter`

## How to

```python
count(start, end=None, step=None)
```

## Import
```python
from counter import count
```

### e.g.

```python
for i in count(1,10):
    print(i)
```

```
1
2
3
4
5
6
7
8
9
10
```

```python
for i in count(1,10,2):
    print(i)
```

```
1
3
5
7
9
```

```python
items = ['foo', 'bar']
for i, item in (1,items):
    print(i,item)
```

```
1 foo
2 bar
```
```python
items = ['foo', 'bar']
for i, item in (0,items,2):
    print(i,item)
```

```
0 foo
2 bar
```