#simple class with empty object instance

class dummy:
    pass

dummy.name='GowthamRam'
dummy.College='PSG'
dummy.Work='Currently in FMC and Formerly in FCA'


print(dummy)

print('----------------------------')

print(dummy.name)

print('----------------------------')

print(dummy.College)

print('----------------------------')

x=dummy()
y=dummy()

print(x.name)
print(y.Work)

a = list(dummy.__dict__.keys())
print(a)


#Expected Results are given below
'''<class '__main__.dummy'>
----------------------------
GowthamRam
----------------------------
PSG
----------------------------
GowthamRam
Currently in FMC and Formerly in FCA'''
['__module__', '__dict__', '__weakref__', '__doc__', 'name', 'College', 'Work']
