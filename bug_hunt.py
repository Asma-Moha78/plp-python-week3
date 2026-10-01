count = 1
total = 0

# BUG: The while statement was missing a colon, so I added one.
# BUG: The loop stopped before 5, so I changed < to <= to include 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: total is an integer, so I converted it to a string before joining it to the text.
print("Sum of 1 to 5 is: " + str(total))
