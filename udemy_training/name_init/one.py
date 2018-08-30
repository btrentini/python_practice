#one.py
#Built-in variable that gets assigned a script

#Python does the below in the background...we add an IF just to check
# if this is the main file
'''
if __name__  == "__main__":
    myfunc()
'''
def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    print("ONE.PY is being run directly")
else:
    print("ONE.PY HAS BEEN IMPORTED")
