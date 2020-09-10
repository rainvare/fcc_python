def arithmetic_arranger(problems, wantAnswer=False):
	
	#To check the length pf problem which should not be more than 5 
    if len(problems) > 5:
        return "Error: Too many problems."
	
	#allowed operators list
    ops = ['+', '-']


	#lines for desired output 
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    for i, problem in enumerate(problems):
		
		#split to get operands and operator
        num1, op, num2 = problem.split(" ")
	
		#check if operator is allowed
        if op not in ops:
            return "Error: Operator must be '+' or '-'."

		#check if operand is digit
        if num1.isnumeric() == False or num2.isnumeric() == False:
            return 'Error: Numbers must only contain digits.'

		#check if numbers are 4 digits and not more than that
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

		#for calculations
        if op == '+':
            result = int(num1) + int(num2)
        else:
            result = int(num1) - int(num2)

		#spacing	
        maxLength = max(len(num1),len(num2)) + 2

		#rjust is used for right align the string
        line1 += num1.rjust(maxLength)
        line2 += op + num2.rjust(maxLength-1)
        line3 += '-' * maxLength
        line4 += str(result).rjust(maxLength)
		
		#adding extra length after every problem
        if i < len(problems) - 1:
            line1 += " " * 4
            line2 += " " * 4
            line3 += " " * 4
            line4 += " " * 4  

    if wantAnswer == True:
        solution = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
        solution = line1 + '\n' + line2 + '\n' + line3

    return solution