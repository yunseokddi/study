hello  = "hello"

def world():
    return "world"

if __name__ == "__main__":
    print("{} direct".format(__name__))

else:
    print("{} import".format(__name__))
