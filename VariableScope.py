'''
LEGB scope order:
Local -> Enclosing -> Global -> Built-in
'''

x = 'global x'
def outer():
    x = 'local outer x'
    def inner():
        x = 'local inner x'
        print(x)
    inner()
    print(x)
outer()
print(x)

#========================================
import builtins
print(dir(builtins))

m = min([5, 1, 4, 2, 3])
print(m)

def min(list):
    return max(list)

m = min([5, 1, 4, 2, 3])
print(m)