height = int(input("Enter the height you want the pyramid: "))
if 1<height<8:
    row = 0
    while (row<height):
        # for creating space before the hash
        space = 0
        while space <= height-row-1:
            print(" ",end = "")
            space +=1
        col = 0
        while col <= row:
            print("#", end = "")
            col += 1
        col = 0
        print(" ",end="")
        while col <= row:
            print("#", end = "")
            col += 1
        print("\n", end = "")
        row += 1
else:
    print("Plese Enter the number between 1 to 8")

#Alternative code:

#height = int(input("Enter the height you want the pyramid: "))
#row = 1
#c = 0
#while height>0:
#    print(height*" ",end ="")
#    print(row*"#",end ="")
#    print(" ",end ="")
#    print(row*"#")
#    row +=1
#    height -=1