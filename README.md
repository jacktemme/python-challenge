Module 3 Challenge:


https://stackoverflow.com/questions/14257373/how-to-skip-the-headers-when-processing-a-csv-file-using-python:

with open("tmob_notcleaned.csv", "rb") as infile, open("tmob_cleaned.csv", "wb") as outfile:
   reader = csv.reader(infile)
   next(reader, None)  # skip the headers

   
