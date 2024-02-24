#task 1

def squares():
    n = int(input())
    sq = (int(i)**2 for i in range(0, n))
    for i in range(n):
        print(next(sq))
        
squares()

#task 2 

def evens():
    n = int(input())
    ev = (int(i) for i in range(0, n + 1, 2))
    for i in range(int(n / 2)):
        print(next(ev), end = ", ")
    print(next(ev))

evens()

#task 3

def divis():
    n = int(input())
    x = lambda x : x if(x % 3 == 0 and x % 4 == 0 and x != 0) else "o"
    a = (x(i) for i in range(0, n))
    for i in range(n):
        y = next(a)
        if(y != "o"):
            print(y)

divis()

#task 4

def squares(a, b):
    for i in range(a, b+1):
        yield i * i

#task 5
        
def countdown(n):
    while n >= 0:
        yield n
        n -= 1