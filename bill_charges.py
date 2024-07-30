# Mr. T got the Electricity bill of his house. He felt that the bill amount was too much. He come to you to understand the relation between amount and number of units with Electricity bill.


# Instructions are give on Electricity biil that :
# 1. For first 50 units Rs. 0.50/unit.
# 2. For next 100 units Rs. 0.75/unit.
# 3. For next 100 units Rs. 1.20/unit.
# 4. For above 250 units Rs. 1.50/unit.
# 5. An additional surcharge of 20% is added to the bill.

# NOTE: As the electricity bill can have any real value (floating point), you have to tell the Integral value of the bill. For eg. Integral value of 2.91 is 2.

# To avoid manual calculation again and again, You have to write a code which take number of Unit (suppose N) from user and print the amount.

import math
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    A = int(input())s
    bill = 0
    charges = [(0.5, 50), (0.75, 100), (1.2,100), (1.5,'All')]
    slab = 0
    while A > 0:
        if slab < 3 and A > charges[slab][1]:
            bill += charges[slab][0]*charges[slab][1]
            A -= charges[slab][1]
            slab += 1
            # print('A = ',A)
            # print('slab = ', slab)
        else:
            bill += A*charges[slab][0]
            break
        
    bill += bill*0.2
    print(math.floor(bill))

    return 0

if __name__ == '__main__':
    main()