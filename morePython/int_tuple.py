class IntTuple(tuple):
    def __init__(self, iterable):
        # before
        super(IntTuple, self).__init__(iterable)
        # after


t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print t