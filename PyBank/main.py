# Dependencies
import os, csv
csv_path = os.path.join("..","Resources", "budget_data.csv")

# Lists to store data
month = []
budget = []
total_budget = 0
budget_change = [0]

# Read in the CSV file
with open(csv_path, newline='', encoding="utf-8") as budget_file:
    # Split the data on columns
    csv_reader = csv.reader(budget_file, delimiter =",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        # Add date
        month.append(row[0])
        # Add budget 
        budget.append(int(row[1]))
    # count total months 
    total_month = len(month)
    print(f"Total Month included in the dataset is: {total_month}")

    # Calculate the total budgets
    for budgets in budget:
        total_budget +=budgets
    print(f"The Total amount is: ${total_budget}") 

    # Calculte the budget change
    for i in range(1,len(budget)):
        budget_change.append(budget[i] - budget[i-1])
    #print(len(budget_change))

    # Calculate the average budget change
    average_change = sum(budget_change)/(len(budget_change)-1)
    average_change = round(average_change,2)

    print(f"Average change is:${average_change}")

    # Calculate the greatest change
    greatest_increase = max(budget_change)
    greatest_decrease = min(budget_change)

    for i in range(0, len(budget_change)):
        if budget_change[i] == greatest_increase:
            greateast_increase_month = month[i]
        elif budget_change[i] == greatest_decrease:
            greatest_decrease_month = month[i]


    print(f"The greatest increase is: ${greatest_increase}")
    print(f"The greatest decrease is: ${greatest_decrease}")
    print(f"The greatest increase month is: {greateast_increase_month}")
    print(f"The greatest decrease month is: {greatest_decrease_month}")
#Create a dictionary file to write to

dict = {"Total months": total_month, "Total amount": total_budget , "Average change": average_change, "The greatest increase": greatest_increase,
                     "The greatest decrease": greatest_decrease, "The greatest increase month": greateast_increase_month, "The greatest decrease month": greatest_decrease_month}
f = open('outfile.txt', 'w')
writer = csv.writer(f, delimiter = '\t')
for key, value in dict.items():
    writer.writerow([key] + [value])
