#I was recently doing a challenge that had a ton of reversed strings in the 'strings' output, so I wrote the two examples below to work with such data. Be sure to comment out whichever one you're not using.

#Reverse a single string.
str1 = "cesrebycpat@/moc.ebutuoy.www//:sptth@"
print(str1[::-1])
Output should print: @https://www.youtube.com/@tapcybersec



#Read a file with reversed strings on their own lines to create a new file with them in proper format.
#Open file to read
with open('PATH\\TO\\READ\\FILE\strings.txt', 'r') as f:
    #Open file to write
    with open('PATH\\TO\\WRITE\\FILE\\stringsrev.txt', 'w') as f_out:
        # Loop through each line of the input file
        for line in f:
            #Reverse the each line and write it to the output file.
            f_out.write(line[::-1])
