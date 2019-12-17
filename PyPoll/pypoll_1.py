# import and read data

import os
import csv

election_data = os.path.join("PyPoll\Resources\\election_data.csv")


with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    votes = []
    candidates = []

# identify columns
    for column in csvreader:
        votes.append(column[0])
        candidates.append(column[2])

# of total votes
total_votes = (len(votes))
print(total_votes)

#Count each number of candidates in the candidates list
Khan = int(candidates.count("Khan"))
Correy = int(candidates.count("Correy"))
Li = int(candidates.count("Li"))
O_Tooley = int(candidates.count("O'Tooley"))

#candidates percentage of vote
Khan_perc = round((Khan/total_votes) * 100)
Correy_perc = round((Correy/total_votes) * 100)
Li_perc = round((Li/total_votes) * 100)
O_Tooley_perc = round((O_Tooley/total_votes) * 100)

#If statement to pick winner

if Khan > Correy > Li > O_Tooley:
        Winner = "Khan"
elif Correy > Khan > Li > O_Tooley:
       Winner = "Correy"
elif Li > Khan > Correy > O_Tooley:
       Winner = "Li"
elif O_Tooley > Khan > Correy > Li:
       Winner = "O'Tooley"


#print to terminal
print("Election Results")
print("------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Khan: + {Khan_perc} + {Khan}")
print(f"Li: + {Li_perc} + {Li}")
print(f"Correy: + {Correy_perc} + {Correy}")
print(f"O_Tooley: + {Khan_perc} + {Khan}")
print("----------------------------")
print (f"Winner: {Winner}")
print("----------------------------")

#Output to text file
text_file = open("pypoll.txt", "w")
text_file.write("Election Analysis")
text_file.write("------------------------ + \n")
text_file.write("Total Votes: " + str (total_votes) + "\n")
text_file.write("Khan: " + str (Khan_perc) + str (Khan) + "\n")
text_file.write("Li: " + str (Li) +  str(Li) + "\n")
text_file.write("Correy: " + str (Correy_perc) + str (Correy) + "\n")
text_file.write("O_Tooley: " + str (O_Tooley_perc) + str (O_Tooley) + "\n")
text_file.write("Winner: str {Winner}")
text_file.close()