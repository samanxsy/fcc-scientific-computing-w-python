# # Budget App - Free Code Camp

class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.balance = 0
    self.name = category
    self.withdrawals = 0

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.balance -= amount
      self.withdrawals += amount
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.category}")
      category.deposit(amount, f"Transfer from {self.category}")
      return True
    else:
      return False

  def __str__(self):
    title = f"{self.category:*^30}\n"
    items = ""
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
    total = f"Total: {self.balance:.2f}"
    return title + items + total


def create_spend_chart(categories):
  withdrawals = []
  names = []
  for category in categories:
    withdrawals.append(
      sum([item['amount'] for item in category.ledger if item['amount'] < 0]))
    names.append(category.category)

  # Total withdrawalss
  total_withdrawals = sum(withdrawals)
  percentage_spent = [
    int(withdrawal / total_withdrawals * 10) * 10 for withdrawal in withdrawals
  ]

  # The chart
  chart = "Percentage spent by category\n"
  for i in range(100, -10, -10):
    chart += str(i).rjust(3) + "| "
    for percentage in percentage_spent:
      if percentage >= i:
        chart += "o  "
      else:
        chart += "   "
    chart += "\n"

  chart += "    " + "---" * len(names) + "-\n"

  # length of the longest category name
  max_name_length = max([len(name) for name in names])

  for i in range(max_name_length):
    chart += "     "
    for name in names:
      if i < len(name):
        chart += name[i] + "  "
      else:
        chart += "   "
    chart += "\n"

  # Removing the last newline character from the chart
  chart = chart[:-1]

  return chart
