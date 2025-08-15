matrix=[
    [1,3,5],
    [2,4,6],
    [7,8,9,10]
]
total=0
for row in matrix:
    for num in row:
        total+=num
print(total)
print(max(row))

