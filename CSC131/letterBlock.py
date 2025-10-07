def evenRow():
    print("A B A B A B A B")

def oddRow():
    print("B A B A B A B A")

for i in range(4):
    for n in range(2):
        if n % 2 == 0:
            row = evenRow()
        else:
            row = oddRow()
