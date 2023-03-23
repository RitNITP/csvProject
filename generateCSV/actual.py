import csv

with open('customers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in mycursor.description])  # write header
    writer.writerows(mycursor)
