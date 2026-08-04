f = open("test.txt", "rt")

print(f.read(8))
print(f.readline())

for x in f:
    print(x)

# help(f.readline)
# help(f.read)
f.close()