#Name: Chandan Suthar
#StudentId: CT_CSI_DS_5312
#Contact No: 7665837658
#Email ID: chandansuthar92@gmail.com
#College name: Poornima Institute of Engineering and Technology

###---------------------------Create lower triangular, upper triangular and pyramid containing the "*" character.-------------------------

def ltp(row):
    print(" Lower Triangular Pattern: ")
    for i in range(1, row + 1):
        print("* " * i)
    print()

    
def utp(row):
    print(" Upper Triangular Pattern: ")
    for i in range(row, 0, -1):
        khalijagah = "  " * (row - i)
        taare = "* " * i
        print(khalijagah + taare)
    print()

    
def compyramid(row):
    print(" Pyramid Pattern: ")
    for i in range(row):
        khalijagah = "  " * (row - i - 1)
        taare = "* " * (2 * i + 1)
        print(khalijagah + taare)
    print()

nrow = 5
ltp(nrow)
utp(nrow)
compyramid(nrow)
