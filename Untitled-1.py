def pattern(num_rows):
    for i in range(num_rows+1):
        for j in range(i,0,-1):
            print(j, end=" ")
        print()   
    for i in range(num_rows):
        for j in range(i,0,-1):
            print(j, end=" ")
        print()          
num_rows = int(input("Enter no. of rows:"))
pattern(num_rows)