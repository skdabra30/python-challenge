# PyBank Challenge

# Import Modules
import os
import csv


# Create variables 
months = 0
net_pl = 0
sum_pl_change = 0

# Set path for csv file
csvpath = os.path.join("PyBank\Resources","budget_data.csv")

# Open csv file
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip headers
        csv_header=next(csvfile)
    
        # Loop data and get info for first line
        line = next(csvreader,None)
        greatest_increased_month = line[0]
        greatest_decreased_month = line[0]
        profit_loss = float(line[1])
        greatest_pl_decrease = profit_loss
        greatest_pl_increase = profit_loss
        previous_pl = profit_loss
        months = 1
        net_pl = float(line[1])
        pl_change = 0

        # One line at a time
        for line in csvreader:

            # Increase count for total months
            months = months + 1

            #Add P and L
            profit_loss = float(line[1])

            # Add to sum of Profit and Losses
            net_pl = net_pl + profit_loss

            # Find monthly change in Profit and Loss
            pl_change = (profit_loss - previous_pl)

            # Calculate sum of all monthly changes
            sum_pl_change = sum_pl_change + pl_change

            # Find greatest monthly increase Profit and Loss amount and
            # the month it occured in.
            if pl_change > greatest_pl_increase:
                greatest_increased_month = line[0]
                greatest_pl_increase = pl_change

            # Find greatest monthly decrease Profit and Loss amount and
            # the month it occured in.
            if pl_change < greatest_pl_decrease:
                greatest_decreased_month = line[0]
                greatest_pl_decrease = pl_change

            # Set previous profit and loss
            previous_pl = profit_loss

        # Finish calculations
        average_pl = float(net_pl/months)
        average_pl_change = float(sum_pl_change/(months-1))

        # Format numbers
        net_pl = int(net_pl)
        
        greatest_pl_increase = int(greatest_pl_increase)
        greatest_pl_decrease = int(greatest_pl_decrease)
        
        # Print analysis
        print(f"Financial Analysis:")
        print("-------------------------------------------------------")
        print(f"Total Months: {months}")
        print(f"Total Revenue: {net_pl} USD")
        print(f"Average Revenue Change: {average_pl_change:.2f} USD")
        print(f"Greatest Increase in Revenue: {greatest_increased_month} {greatest_pl_increase} USD")
        print(f"Greatest Decrease in Revenue: {greatest_decreased_month} {greatest_pl_decrease} USD")
        print("")
             


        # Open file
        filewriter = open("financialanalysis.txt", mode = 'w')

        # Print to file
        filewriter.write(f"Financial Analysis:\n")
        filewriter.write("-------------------------------------------------------\n")
        filewriter.write(f"Total Months: {months}\n")
        filewriter.write(f"Total Revenue: {net_pl} USD\n")
        filewriter.write(f"Average Revenue Change: {average_pl_change:.2f} USD\n")
        filewriter.write(f"Greatest Increase in Revenue: {greatest_increased_month} {greatest_pl_increase} USD\n")
        filewriter.write(f"Greatest Decrease in Revenue: {greatest_decreased_month} {greatest_pl_decrease} USD\n")
        filewriter.write("")

        # Close file
        filewriter.close()