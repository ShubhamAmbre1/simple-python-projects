import csv 

amount_lis = []

def check_expence():
	total_expense = []
	with open('expense.csv', 'r') as f:
		x = csv.reader(f, delimiter=',')
		for items in x:
			total_expense.append(int(items[1]))
	print(sum(total_expense))
	print()

def add_expense():
	item = str(input("Enter Expense:"))
	amount = int(input("Enter Expense amount:"))
	lis = [item, int(amount)]
	
	with open('expense.csv', 'a',newline = "\n") as f:
		y = csv.writer(f)
		y.writerow(lis)
	print()

def budget():
	pass

if __name__ == "__main__":
	while True:
		i = int(input("1) To check expense type 1\n2) To add expense type 2\n3) To exit\nEnter no. = " ))

		if i == 1:
			check_expence()

		elif i == 2:
			add_expense()

		elif i == 3:
			quit()


