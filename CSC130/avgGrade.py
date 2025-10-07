def user_name():
    name = str(input("Please enter your name: "))
    return name
def grades():
    x = float(input("Enter your score: "))
    y = float(input("Enter your score: "))
    return x,y
def grade_average():
    x = grades()
    y = grades()
    total = x + y
    avg = total / 200 * 100
    return avg
name = user_name
x = grades()
y = grades()
avg = grade_average()
print(avg)
