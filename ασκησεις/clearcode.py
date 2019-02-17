# Γράψτε ένα πρόγραμμα το οποίο θα αφαιρεί τα σχόλια που έχει ένας κώδικας Python 
# το οποίο τον διαβάζετε από ένα αρχείο. Χρησιμοποιείστε μόνο τα σχόλια με #.


infile = open("file1.txt","r") 
outfile = open("file2.txt","w")
linecount = ""
for line in infile:
  for char in line:
    if char != "#" :
      linecount = linecount + char
    else:
      break;
    print "Done!"      
outfile.write(linecount + "\n")
infile.close()
outfile.close() 