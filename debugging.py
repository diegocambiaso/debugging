# import pdb; pdb.set_trace() to use in Python till 3.7
# breakpoint() is the new way stated in Python 3.8

while True:
    try:
        breakpoint()
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

print(x)
