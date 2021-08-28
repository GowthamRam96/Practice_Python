from __future__ import print_function

class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i): # Fallback for iteration
        print('get[%s]:' % i, end='') # Also for index, slice
        return self.data[i]
    def __iter__(self): # Preferred for iteration
        print('iter=> ', end='') # Allows only one active iterator
        self.ix = 0
        return self
    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self, x): # Preferred for 'in'
        print('contains: ', end='')
        return x in self.data
    next = __next__ # 2.X/3.X compatibility
if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5]) # Make instance
    print(3 in X) # Membership
    for i in X: # for loops
        print(i, end=' | ')
    print()
    print([i ** 2 for i in X]) # Other iteration contexts
    print( list(map(bin, X)) )
    I = iter(X) # Manual iteration (what other contexts do)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break

#Results
'''
contains: True
iter=> next:1 | next:2 | next:3 | next:4 | next:5 | next:
iter=> next:next:next:next:next:next:[1, 4, 9, 16, 25]
iter=> next:next:next:next:next:next:['0b1', '0b10', '0b11', '0b100', '0b101']
iter=> next:1 @ next:2 @ next:3 @ next:4 @ next:5 @ next:
'''
