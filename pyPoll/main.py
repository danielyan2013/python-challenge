import csv
import pandas as pd

with open("election_data.csv") as csvfile:
    readCSV = csv.reader(csvfile)
    next(readCSV)

    df = pd.DataFrame(readCSV)
    candidates = []
    totalVoteCasted = (df[0].count())
    candidates = df[2].unique()

    votes = df[2].value_counts()
    votesPercentage = df[2].value_counts(normalize = True)
    #print(votes.index(max(votes)))
    winner = votes.idxmax()

    print("Election Results")
    print("---------------------------------")
    print("Total Votes:",totalVoteCasted)
    print("---------------------------------")
    for i in range(0, len(votes)):
        print(candidates[i]+":", "%.2f"%(votesPercentage[i]*100),"%", "(", \
        votes[i],")")
    print("---------------------------------")
    print("Winner:",winner)
    print("---------------------------------")

with open("Election Results.txt", "w") as textfile:
    textfile.write("Election Results")
    textfile.write("\n")
    textfile.write("---------------------------")
    textfile.write("\n")
    textfile.write("Total Votes:"+ str(totalVoteCasted))
    textfile.write("\n")
    textfile.write("---------------------------")
    textfile.write("\n")
    for i in range(0, len(votes)):
        textfile.write(candidates[i]+":"+"%.2f"%(votesPercentage[i]*100)+ \
        "% ("+str(votes[i])+")")
        if i != len(votes):
            textfile.write("\n")
    textfile.write("---------------------------")
    textfile.write("\n")
    textfile.write("Winner: "+winner)
    textfile.write("\n")
    textfile.write("---------------------------")

    #totalVotesCast = sum(1 for row in readCSV)
    #print(totalVotesCast)

    #totalVotesCast = 0
    # totalVotesKhan = 0
    # totalVotesCorrey = 0
    # totalVotesLi = 0
    # totalVotesOTooley = 0
    # candidates = []
    # processed_so_far = 0
    # for row in readCSV:
    #     processed_so_far += 1
    #     print("processed_so_far={}".format(processed_so_far))
    #     totalVotesCast = totalVotesCast + 1
    #     if row[2] not in candidates:
    #         candidates.append([row[2], 1])
    #     else:
    #         for i in range(0, len(candidates) - 1):
    #             if row[2] == candidates[i]:
    #                 candidates[i][1] = candidates [i][1] + 1
    #
    # print(candidates)

        # if row[2] == "Khan":
        #     totalVotesKhan = totalVotesKhan + 1
        # elif row[2] == "Correy":
        # elif row[2] == "Li":
        #     totalVotesCorrey = totalVotesCorrey + 1
        #     totalVotesLi = totalVotesLi + 1
        # elif row[2] == "O'Tooley":
        #     totalVotesOTooley = totalVotesOTooley + 1

    # khanPercentage = round((totalVotesKhan*100/totalVotesCast),2)
    # liPercentage = round((totalVotesLi*100/totalVotesCast),2)
    # correyPercentage = round((totalVotesCorrey*100/totalVotesCast),2)
    # oTooleyPercentage = round((totalVotesOTooley*100/totalVotesCast),2)

    # print(totalVotesCast)
    # print(totalVotesKhan)
    # print(totalVotesLi)
    # print(totalVotesCorrey)
    # print(totalVotesOTooley)
    # print(candidates)
