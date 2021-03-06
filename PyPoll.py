# the date we need to retrieve. 
# 1. The total number of votes cast
# 2. A complete lis of candidates who recieved votes
# 3. The percentae of votes each candidate won
# 4. The total number of votes each candiate won
# 5. The winer of the election based on popular vote
# import the datetime class from datime module
import datetime as dt
# Use the now()attribute on the datime class to get the present time now
now = dt.datetime.now()
#print the presernt time 
print("the time right now is ", now)
# # Assign a variable  for the file to load and the path
# file_to_load ='Downloads/election_results.csv'
# # open the elections resurlt and read the file. 
# with open(file_to_load) as election_data:
#     #To do: perfrom analysis.
#     print(election_data)
# # Close the file. 
# election_data.close() 
import csv
import os
# #assign a cariable for the file to laod and the path. 
file_to_load = os.path.join("Downloads", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    #print(election_data) 
# craet a file name variable to direct or indirect path 
#file_to_save = os.path.join("Downloads/Election_Analysis/analysis", "election_analysis.txt")
#open(file_to_save, "w")
#    txt_file.write("Arapahoe\n Denver\n Jefferson")
file_to_save = os.path.join("Downloads/Election_Analysis/analysis", "election_analysis.txt")
# 1. intialize a total vote cotnuer 
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #print each row in CSV file. 
    headers = next(file_reader)
    #print each row in the CSV file 
    for row in file_reader:
        total_votes += 1
        #print the candidate dae for each row 
        candidate_name = row[2]
        # if the candidate does not match any existing candidte
        if candidate_name not in candidate_options:
        #add the candidate nad to the dandidate list 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    election_results = (f"\nElections Results\n" f"----------------\n" f"Total Votes: {total_votes:,}\n" f"------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    #candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #print(candidate_results)
    #txt_file.write(candidate_results)
# interare though the candidate list
    for candidate_name in candidate_votes:
        # retrieve vote counte of a candidate.
        votes = candidate_votes[candidate_name]
        #calc the %
        vote_percentage = float(votes)/ float(total_votes)* 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes> winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (f"----------------------------\n" f"Winner: {winning_candidate}\n" f"Winning Vote Count: {winning_count:,}\n" f"Winning Percentage: {winning_percentage: .1f}5\n" f"-------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    #pritn the candidates name and  4 of votes 
   # print(f"{candidate_name}: recieved {vote_percentage}% of the vote")
#print(total_votes) 
#print(candidate_options)
#print(candidate_votes)
