#String manipulation
# Essential for splitting numbers into individual digits.
# Question one
def digitSum(N):
    str_N = str(N)
    sum = int(str_N[0]) + int (str_N[1])
    print(sum)
digitSum(95)
