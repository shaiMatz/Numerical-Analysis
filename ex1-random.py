import random

EladSapir = "000000000"
ShaiMatzliach = "111111111"
TomerRaitsis = "222222222"
subjects=["Solve linear equations","Finding roots" ,"Approximations","integration"]

x, y, z = random.randint(0, 8), random.randint(0, 8), random.randint(0, 8)
result = int(EladSapir[x]) + int(ShaiMatzliach[y]) + int(TomerRaitsis[z])
result = result % 4
print(result, "-" , subjects[result])


