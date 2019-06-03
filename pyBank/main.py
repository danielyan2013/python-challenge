import csv
import statistics

with open('budget_data.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    next(csvfile)
    dates = []
    profits = []
    profitChanges = []
    for row in readCSV:
        date = row[0]
        profit = row[1]

        dates.append(date)
        profits.append(profit)

    #print(dates)
    #print(profits)

    numberOfMonth = len(dates)
    #print(numberOfMonth)
    profits = list(map(int, profits))
    totalProfits = sum(profits)
    #print(totalProfits)

    for i in range(1, len(profits)):
        currentProfit = profits[i]
        lastProfit = profits[i - 1]
        profitChange = currentProfit - lastProfit
        profitChanges.append(profitChange)

    averageChangeOfProfits = statistics.mean(profitChanges)
    #print(averageChangeOfProfits)
    #print(max(profitChanges))
    #print(min(profitChanges))
    #print(profitChanges)
    greatestIncreaseDate = profitChanges.index(max(profitChanges)) + 1
    greatestDecreaseDate = profitChanges.index(min(profitChanges)) + 1
    #print(dates[greatestIncreaseDate + 1])
    #print(dates[greatestDecreaseDate + 1])

    print("Financial Analysis")
    print("---------------------------")
    print("Total Months:",numberOfMonth)
    print("Total: $",totalProfits)
    print("Average Change: $",averageChangeOfProfits)
    print("Greatest Increase in Profits:",dates[greatestIncreaseDate],"$",\
    max(profitChanges))
    print("Greatest Decrease in Profits:",dates[greatestDecreaseDate],"$",\
    min(profitChanges))
