
def arithmetic_arranger(problems, show_answers=False):

    nums1 = []
    nums2 = []
    dash = []
    sums = []

    for val in problems:
        for i in range(len(val)):
            #print(val[i])
            if (val[i] == '+' or val[i] == '-'):
                nums1.append(val[:i])
                nums2.append(val[i]+val[i+1:]) 
                dash.append('-----')
                if (val[i] == '+'):
                    sums.append(str(int(val[:i])+int(val[i+1:]))) #opperation
                else:
                    sums.append(str(int(val[:i])-int(val[i+1:]))) #opperation

    if (show_answers == False):
        print(f"  {'   '.join(nums1)}\n{'    '.join(nums2)}\n{'   '.join(dash)}")
    else:
        print(f" {'      '.join(nums1)}\n{'    '.join(nums2)}\n{'    '.join(dash)}\n  {'     '.join(sums)}")


#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
#arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
arithmetic_arranger(["3801 - 2", "123 + 49"])

print('\n\n')
















def arithmetic_arranger(problems, show_answers=False):
    # Lists to hold each part of the formatted problems
    first_operands = []
    second_operands = []
    dashes = []
    results = []

    # Process each problem
    for problem in problems:
        # Split the problem into its components
        num1, operator, num2 = problem.split()

        # Check if the numbers are valid (all digits)
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if the operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Convert strings to integers for arithmetic operation
        num1_int = int(num1)
        num2_int = int(num2)

        # Calculate the result based on the operator
        if operator == '+':
            result = num1_int + num2_int
        else:
            result = num1_int - num2_int

        # Determine the width needed for the current problem
        width = max(len(num1), len(num2)) + 2

        # Format each part of the problem to be right-aligned
        first_operands.append(num1.rjust(width))
        second_operands.append(operator + num2.rjust(width - 1))
        dashes.append('-' * width)
        results.append(str(result).rjust(width))

    # Join each part with four spaces between problems
    first_line = '    '.join(first_operands)
    second_line = '    '.join(second_operands)
    dash_line = '    '.join(dashes)

    # If show_answers is True, include the results
    if show_answers:
        result_line = '    '.join(results)
        arranged_problems = f"{first_line}\n{second_line}\n{dash_line}\n{result_line}"
    else:
        arranged_problems = f"{first_line}\n{second_line}\n{dash_line}"

    # Print the arranged problems
    print(arranged_problems)


# Test cases
#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
#arithmetic_arranger(["3801 - 2", "123 + 49"])



