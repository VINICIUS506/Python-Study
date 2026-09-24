# Write a short program that prints the numbers 1 to 10 using a for loop. 
# Then, write an equivalent program that prints the numbers 1 to 10 using a while loop.
print('For version: ')
for i in range(1, 11):
    print(i)

print('While version: ')
i = 1
while True:
    print(i)
    i = i + 1
    if i > 10:
        break


