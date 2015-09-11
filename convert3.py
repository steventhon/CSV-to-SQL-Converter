delimiter = input("Enter delimiter: ")
table = input("Enter name of table and columns: ")
numCols = int(input("Enter number of columns: "))
numRows = int(input("Enter number of entries: "))
data = input("Enter data:\n")

data = data.split(delimiter)

rows = 0
while (rows < numRows):
  print("INSERT INTO " + table)
  vals = "VALUES ("
  curr = 0
  while (curr < numCols - 1):
    vals += data[curr] + ", "
    curr += 1
  print(vals + data[curr + 1] + ");")
  rows += 1
