def total_bill(func, value):
  total = func(value)
  print(str(total))
  return total

def add_tax(tots):
  tax = tots * 0.20
  new_total = tots + tax
  print(str(new_total))
  return new_total

print(total_bill(add_tax, 100))

