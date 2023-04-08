def arithmetic_arranger(problems, results=False):

  if len(problems) > 5:
    return "Error: Too many problems."

  first_row = []
  second_row = []
  dash_line = []
  answer_row = []

  for problem in problems:
    components = problem.split()

    if components[1] not in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."
    if not components[0].isdigit() or not components[2].isdigit():
      return "Error: Numbers must only contain digits."
    if len(components[0]) > 4 or len(components[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    num1 = int(components[0])
    op = components[1]
    num2 = int(components[2])
    result = num1 + num2 if op == "+" else num1 - num2

    max_length = max(len(components[0]), len(components[2])) + 2

    first_row.append(components[0].rjust(max_length))
    second_row.append(op + " " + components[2].rjust(max_length - 2))
    dash_line.append("-" * max_length)
    answer_row.append(str(result).rjust(max_length) if results else "")

  arranged_problems = "    ".join(first_row) + "\n" + "    ".join(
    second_row) + "\n" + "    ".join(dash_line)
  if results:
    arranged_problems += "\n" + "    ".join(answer_row)

  return arranged_problems
