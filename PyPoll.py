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
file_to_save = os.path.join("Downloads/Election_Analysis/analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #print each row in CSV file. 
    headers = next(file_reader)
    print(headers)
#    txt_file.write("Counties in the Elections\n ----------\nArapahoe\n Denver\n Jefferson")