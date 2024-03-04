# python-challenge

https://stackoverflow.com/questions/14674275/skip-first-linefield-in-loop-using-csv-file

firstline = True
for row in kidfile:
    if firstline:    #skip first line
        firstline = False
        continue
