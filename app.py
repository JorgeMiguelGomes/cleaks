# -*- coding: utf-8 -*-
# author: JGomes_EU

# Import libraries

import pandas as pd 



# txt is a version of meddLog.json where all { and } were deleted
# and all blank lines were deleted as well

# Create list 
# For each for lines of the text file create an entry
# Splitting by ":"

with open("conti_merged_txt.txt") as f:                            
    batch = {}                                                      
    result = []
    for line in f:
        #print(f,line)
        key, value = line.rstrip().split(":", maxsplit=1)
        batch[key.strip('" ')] = value.strip('" ')
        if len(batch) == 4:
            result.append(batch)
            #print(result)
            batch = {}

# Create dataframe with the result 

df = pd.DataFrame(result)

# Get rid of the trailing ", characters in the ts, to, from columns 

df['ts'] = df['ts'].apply(lambda x: x.rstrip('",'))
df['to'] = df['to'].apply(lambda x: x.rstrip('",'))
df['from'] = df['from'].apply(lambda x: x.rstrip('",'))


# Save to txt file 
df.to_csv('conti_merged_csv.csv')

# Save to a new valid json file
df.to_json('conti_merged_valid_json.json')



# Create Dataframe by groupinhg to and from and counting how many messages
df_sankey = df.groupby(["from","to"], as_index=False)["body"].count().rename(columns={"from":"sender","to":"receiver","body":"message"})
# Save to csv file 
df_sankey.to_csv("conti_new_sankey.csv")

# END APP 
