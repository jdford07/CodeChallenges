url1 = list("Mr John Smith") # size 13

count = len(url1)
for i in range(count):
    if url1[i] == " ":
        url1[i] = "%"
        url1.insert(i+1, "2")
        url1.insert(i+2, "0")
        i += 3

print("".join(url1))