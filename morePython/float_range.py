# reversed(l) # iter(l) 

class FloatRnage:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

if __name__ == '__main__':
    for x in FloatRnage(1.0, 4.0, 0.5):
        print x

    for x in reversed(FloatRnage(1.0, 4.0, 0.5)):
        print x