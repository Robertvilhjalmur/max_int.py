n = int(input("Enter the length of the sequence: ")) # Do not change this line
first = 1
second = 2
third = 3
print(first)
print(second)
print(third)

for i in range(1,n-2):
    tala = first + second + third
    print(tala)
    first = second
    second = third
    third = tala 


# næsta tala er alltaf fyrri þrjár plúsaðar saman.