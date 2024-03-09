Module 3 Challenge:

This repository contains an analysis of two csv files that was done using python as the programming language. The PyBank folder includes a csv file of monetary profit or loss of a company throughout a period of time. The python script in main.py runs through this csv file to determine the total amount of money gained and the number of months in which this data was compiled. It also looks at the change of profits through each time point given to determine when there was the greatest increase and greatest decrease in profits. These results can be found in the analysis folder.

The PyPoll folder contains a csv file containg all of the submitted votes in an election between three candidates. The python script for this csv file is able too iterate through all of the votes and determine the total votes and overall vote percentage each candidate gained. Then from these results the winner of the election was determined. These findings can be found in the analysis folder as well.


For these two python scripts, this website was referenced to skip the headers of the data file before beginning analysis. 

https://stackoverflow.com/questions/14257373/how-to-skip-the-headers-when-processing-a-csv-file-using-python:

with open("tmob_notcleaned.csv", "rb") as infile, open("tmob_cleaned.csv", "wb") as outfile:
   reader = csv.reader(infile)
   next(reader, None)  # skip the headers

   
