import one
print("TOP LEVEL IN TWO.PY")

one.func()

if __name__ =='__main__':
    print("2 not imported")
else:
    print("2 WAS IMPORTED!")
