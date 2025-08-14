fruits=['apple','banana','orange','grape','kiwi','strawberry','melon']

for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)

Random_char=input("Hay nhap mot ki tu bat ki: ")
for fruit in fruits:
    if Random_char in fruit:
        print(fruit)

for fruit in fruits:
    if fruit == fruit[::-1]: 
        print(fruit)