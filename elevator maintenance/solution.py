# x = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
x = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
def func(x):
    z = [0,0,0,0]
    for idx, i in enumerate((x.split("."))):
        z[idx] = int(i)
    z[-1] = len(x.split("."))
    return z

print(sorted(x, key=lambda x: func(x)))