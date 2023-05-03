import shelve


filename=r'C:\Users\Franz\OneDrive\_PhD\Code\Test_files\shelve.out'
my_shelf = shelve.open(filename,'n') # 'n' for new


T='Hiya'
x=3
values=[1,2,3]
var_list=dir()
var_list=var_list()
print(var_list)

for key in dir():
    try:
        my_shelf[key] = globals()[key]
    except TypeError:
        #
        # __builtins__, my_shelf, and imported modules can not be shelved.
        #
        print('ERROR shelving: {0}'.format(key))
my_shelf.close()

del T
del x
del values

my_shelf = shelve.open(filename)
for key in my_shelf:
    globals()[key]=my_shelf[key]
my_shelf.close()

print(T) # Hiya
print(x) # 3
print(values) # [1, 2, 3]