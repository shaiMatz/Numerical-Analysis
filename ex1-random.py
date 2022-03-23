import random

EladSapir = "209479948"
ShaiMatzliach = "206376212"
TomerRaitsis = "316160167"
subjects=["Solve linear equations","Finding roots" ,"Approximations","integration"]

x, y, z = random.randint(0, 8), random.randint(0, 8), random.randint(0, 8)
result = int(EladSapir[x]) + int(ShaiMatzliach[y]) + int(TomerRaitsis[z])
result = result % 4
print(result, "-" , subjects[result])


