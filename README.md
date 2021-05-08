# Election-Analysis

## Project Overview
This analysis is an audit of the results of a recent local congressional election, prepared at the request of the Colorado Board of Elections. The goal of the analysis is to determine the total votes cast in the election, the percentage received by each candidate, the breakdown of voter turnout by county, and the winner of the race.

## Process
The process of preparing this report involved:
1. Calculating the total votes cast in the election.
2. Creating a complete list of the candidates who received votes.
3. Determining the total votes cast for each candidate.
4. Determining each candidate's percentage of the total votes cast.
5. Identifying the winner of the race, based on the popular vote.

## Resources
The dataset: election_results.csv

Software used in this analysis: Python, VS Code

## Summary of Findings
Through this analysis, we determined:
* **The total votes cast in the election:** 369,711
* **List of candidates who received votes:**
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane
* **Breakdown of votes by candidate:**
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)
* **Election winner:**
  * Diana DeGette won the election with 73.8% of the vote and 272,892 votes in total.

## Project Conclusion
By using Python and VS Code, we were able to quickly parse the 369,712-line data file and extract the requested information with much less effort than such analysis would require in Excel. These tools offer greater computational efficiency and more complex analysis, which make them invaluable for a modern data analyst. 
In order to provide the Election Board additional analytical flexibility, the script for this analysis is easily adaptable for parsing other election data sets. The key modifications that would need to be made would be:
1. Adjusting the index value for `candidate_name = row[2]` based on the column in which candidate names are listed in the particular dataset, and
2. Similarly adjusting the `county_name = row[1]`. Note that index values begin with 0, meaning the first column in the dataset has an index value of 0, the second column has a value of 1, etc.
