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
