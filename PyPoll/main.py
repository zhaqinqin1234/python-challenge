# Dependencies
import os, csv, numpy as np
csv_path = os.path.join("..","Resources", "election_data.csv")

# Lists to store data
voter_ID = []
county = []
candidate = []
candidate_name = []
candidate_counts = []


# Read in the CSV file
with open(csv_path, newline='', encoding="utf-8") as election_file:
    # Split the data on columns
    csv_reader = csv.reader(election_file, delimiter =",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        # Add voter_ID
        voter_ID.append(row[0])
        # Add county 
        county.append(row[1])
        # Add candidate
        candidate.append(row[2])
    # count total votes 
    total_votes = len(candidate)
    print(f"Total number of votes cast is: {total_votes}")


    # find candiates list
    unique_candidate = set(candidate)
    candidate_list = list(unique_candidate)
    print(f"A complete list of candidates are: {candidate_list}")

    # find winner
    dic = {}
    for cand in candidate:
        if cand not in dic:
            dic[cand] =1
        else: 
            dic[cand] = dic[cand] + 1
    print(dic)
    max_count = max(zip(dic.values(), dic.keys()))
    print(f"winner candidate is {max_count}")

    dic["total Votes "] = total_votes
    dic["winner"] = max_count
    

# write to text file   
f = open('outfile.txt', 'w')                    
writer = csv.writer(f, delimiter = '\t')
for key, value in dic.items():
    writer.writerow([key] + [value])

    