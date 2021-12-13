# Election_Analysis
## Overview of Election Audit
This week we helped our friends Seth and Tom create a detailed analysis for the election commission. Through this analysis we seeked to find the answers to: 
-The total number of votes cast
-The candidates who recieved votes
-the total number of votes each canidate recieved
-the percentage of votes that each candidate recieved 
-who the winner was based on the votes. 

After extracting  this data we needed to complete the audit by: 
-Researching the turnout for each county
-the percentage of votes from each county from the total count
-the county with the largest turnout. 

## Election-Audit Results:
Using the great resource that python is we were able to deduce the following:
<img width="469" alt="Screen Shot 2021-12-12 at 8 30 56 PM" src="https://user-images.githubusercontent.com/94723290/145739402-dc6a5d19-c3da-4180-b510-a0dd90094bff.png">

Arapahoe recieved 24,801 votes (6.7%) of the county votes.
Jefferson county recieved 38,855 votes (10.5%) of the county votes.
Finally, Denver had the greaest turnout with 306,055 votes. (82.8%) of the county votes.
After looping through I was able to pull how many votes wach candidate recieved from the 3 counties. 

<img width="672" alt="Screen Shot 2021-12-12 at 8 31 28 PM" src="https://user-images.githubusercontent.com/94723290/145739419-9669d5be-ce7b-41ed-8442-e0bc19727794.png">

The number of votes for eavh candidate from each county are as followed:
Raymon Anthony Doane recieved 11,606 votes (3.1%) of the total votes. 
Charles Casper Stockham recieved 85,213 votes (23%) of the total votes.
Diana DeGette recieved 272,892 votes (73.8%) of the total votes. 
Its clear to see Diana Degette won the election with a staggering 73.1% of the votes. Talk about a landslide. 
## Audit Summary
This script used with the correct data can return the same information for selected counties and states. If I wanted  to modify the script for a larger state/location I would seperate the smaller counties from the larger counties to check if how the turnout rates stack uop agaisnt eachother. 
