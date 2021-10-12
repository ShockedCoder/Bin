stairSize = 3

top = "###"
bottom = "# #"
topend = "##"
bottomend = " #"

for i in range(stairSize):
    print(top + topend*i)
    print(bottom + bottomend*i)

print(top + topend*i)