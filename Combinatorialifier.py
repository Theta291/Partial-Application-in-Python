#Exercise: Try to make a function that accepts a function of only positional arguments and returns a function that takes the same number of positional arguments and, given they are all iterators, attempts every combination of one arguments from each iterator.
#Skills: Partial application, Iteration

papplycomboreverse = lambda fun, xiter : lambda *args : [fun(*args, x) for x in xiter]

def combo(fun):
    def returnfun(*args):
        currfun = fun
        for arg in reversed(args):
            currfun = papplycomboreverse(currfun, arg)
        return currfun()
    return returnfun
