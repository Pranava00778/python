n = int(input("Enter No.: "))
tableData =""
for i in range(1,11):
    # print(n,"x", i , "=", n*i)
    #print("%d x %d = %d" % (n, i, n*i)) # String Interpolation
    tableData = tableData + "%d x %d = %d" % (n, i, n*i) +'\n'

fileTable = open("table of %s.txt" % n, "w")
fileTable.write(tableData)
fileTable.close()

fileReadTable = open("table of %s.txt" % n)
print(fileReadTable.read())