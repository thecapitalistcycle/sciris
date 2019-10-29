import numpy as np
import sciris as sc


def test_colorize():
    sc.heading('test_colorize()')
    sc.colorize(showhelp=True)
    sc.colorize('green', 'hi') # Simple example
    sc.colorize(['yellow', 'bgblack']); print('Hello world'); print('Goodbye world'); sc.colorize('reset') # Colorize all output in between
    bluearray = sc.colorize(color='blue', string=str(range(5)), output=True); print("c'est bleu: " + bluearray)
    sc.colorize('magenta') # Now type in magenta for a while
    print('this is magenta')
    sc.colorize('reset') # Stop typing in magenta
    return


def test_printing():
    sc.heading('test_printing()')
    example = sc.prettyobj()
    example.data = sc.vectocolor(10)
    print('sc.pr():')
    sc.pr(example)
    print('sc.pp():')
    sc.pp(example.data)
    string = sc.pp(example.data, doprint=False)
    return string
    

def test_promotetolist():
    sc.heading('test_promotetolist()')
    ex1 = 'a'
    ex2 = {'a', 'b'}
    ex3 = np.array([0,1,2])
    res1 = sc.promotetolist(ex1)
    res2a = sc.promotetolist(ex2)
    res2b = sc.promotetolist(ex2, objtype='str')
    res3a = sc.promotetolist(ex3)
    res3b = sc.promotetolist(ex3, objtype='number')
    errstr = ''
    try:
        sc.promotetolist(ex3, objtype='str')
    except Exception as E:
        errstr = str(E)
    assert res1 == ['a']
    assert res2a == [{'a', 'b'}]
    assert sorted(res2b) == ['a', 'b'] # Sets randomize the order...
    assert repr(res3a) == repr([np.array([0,1,2])]) # Direct quality comparison fails due to the array
    assert res3b == [0,1,2]
    assert errstr == "promotetolist() type mismatch: Incorrect type: object is <class 'numpy.int64'>, but str is required"
    print(res1)
    print(res2a)
    print(res2b)
    print(res3a)
    print(res3b)
    print('Example error message: %s' % errstr)
    return


def test_suggest():
    sc.heading('test_suggest()')
    string = 'foo'
    ex1 = ['Foo','Bar']
    ex2 = ['FOO','Foo']
    ex3 = ['Foo','boo']
    ex4 = ['asldfkj', 'aosidufasodiu']
    ex5 = ['foo', 'fou', 'fol', 'fal', 'fil']
    res1 = sc.suggest(string, ex1)
    res2 = sc.suggest(string, ex2)
    res3 = sc.suggest(string, ex3)
    res4 = sc.suggest(string, ex4, threshold=4)
    try:
        sc.suggest(string, ex1, threshold=4, die=True)
    except Exception as E:
        errstr = str(E)
    res5a = sc.suggest(string, ex5, n=3)
    res5b = sc.suggest(string, ex5, fulloutput=True)
    assert res1 == 'Foo'
    assert res2 == 'Foo'
    assert res3 == 'Foo'
    assert res4 == None
    assert res5a == ['foo', 'fou', 'fol']
    assert res5b == {'foo': 0.0, 'fou': 1.0, 'fol': 1.0, 'fal': 2.0, 'fil': 2.0}
    assert errstr == '"foo" not found - did you mean "Foo"?'
    print(res1)
    print(res2)
    print(res3)
    print(res4)
    print(res5a)
    print(res5b)
    print('Example error message: %s' % errstr)
    return
    

if __name__ == '__main__':
    test_colorize()
    test_printing()
    test_promotetolist()
    test_suggest()