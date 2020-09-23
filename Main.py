import os 
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

total_month= 0
net_changelist=[]
total_netchange=0
greatest_increase=["",0]
greatest_decrease=["",9999999]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    jan=next(csvreader)
    total_month=total_month+1
    total_netchange=total_netchange+int(jan[1])

    previous_net=int(jan[1])
    for row in csvreader:
        print(row)
        total_month=total_month+1
        total_netchange=total_netchange+int(row[1])
        change=int(row[1])- previous_net
        previous_net=int(row[1])
        net_changelist=net_changelist+[change]
        if change > greatest_increase[1]:
            greatest_increase[0]= row[0]
            greatest_increase[1]= change

        if change < greatest_decrease[1]:
            greatest_decrease[0]= row[0]
            greatest_decrease[1]= change

average_change= round(sum(net_changelist)/len(net_changelist),2)

print(f"total month {total_month}")
print(f"total net {total_netchange}")
print(f"average net change {average_change}")
print(f"great increase {greatest_increase[0]}{greatest_increase[1]}")
print(f"great decrease {greatest_decrease[0]}{greatest_decrease[1]}")