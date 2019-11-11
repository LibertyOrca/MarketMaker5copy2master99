import time


entrytime = 0
def entryfunc():
    q = 0
    global entrytime

    if q == 0:
        entrytime = time.time()

    else:
        entrytime = entrytime



entryfunc()

print(entrytime)

entryfunc()
print(entrytime)
