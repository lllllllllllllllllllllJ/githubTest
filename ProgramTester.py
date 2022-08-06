# Program used to test code and demonstrate questions

import Question1 as Q1
import Question2 as Q2
import Question3 as Q3
import Question5 as Q5

if __name__ == "__main__":

    try:
        # Question 1 
        print(Q1.factorialIterative(9))
        print(Q1.factorialRec(9))
        print(Q1.fibinacciIterative(4))
        print(Q1.fibinacciRec(4))

        # Question 2 
        print(Q2.GCD(40, 25))

        # Question 3
        print(Q3.convert(29923, 15))

        # Question 5
        Q5.towers(3, 1, 3)

        ...
    except Exception as e:
        print("Exception in program >> %s %s" % (e.__class__, e))


