def print_pattern(rows, cols):
    for i in range(rows):
        for i in range(cols):
            print(" ___", end="    ")
        print()
        for i in range(cols):
            if i == cols-1:
                print("/   \\", end="")
            else:
                print("/   \\___", end="")
        print()
        for i in range(cols):
            print("\\   /", end="   ")
        print()
    for i in range (cols):
        print(" ___",end="    ")
r=int(input("Enter number of rows :"))
c=int(input("Enter number of columns :"))
print_pattern(r,c)