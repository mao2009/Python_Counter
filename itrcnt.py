def count(start, end=None, step=None):
    if step == 0:
        raise IndexError
    if hasattr(step, "__iter__"):
        raise TypeError

    if (hasattr(start, "__iter__")
        or hasattr(end, "__iter__")):
        return __iter_count(start, end, step)
    else:
        return __num_count(start, end, step)
        
def __iter_count(start,end=None, step=None):
    items = None
    if hasattr(start, "__iter__"):
        if step is not None:
            raise IndexError
        items = start
        count = 0
        step = end

    if hasattr(end, "__iter__"):
        count = start
        items = end

    if step is None:
        step = 1
        
    for item in items:
        yield count, item
        count += step

def __num_count(start, end=None, step=None):
    if end is None:
        end = start
        start = 0
    count = start

    if step is None:
        step = 1

    if start > end:
        if step > 0:
            step *= -1
        while count >= end:
            yield count
            count += step
    else:
        if step < 0:
            step *= -1
        while count <= end:
            yield count
            count += step

