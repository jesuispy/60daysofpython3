id = "Cloud"
print(id.upper())
print(id.lower())

greeting = "Hello " + id +   " How are you!"
print(greeting)

#length of string converted to string
print(str(len(greeting)) + " Is the lenght of the greeting")

#if function 
if id in greeting:
    print("The id is contained in the greeting!")
else: 
    print("The id is hidden")

print(f"The first character of the id is {id[0]}")

scream = id * 5
greeting = "I'm gonna repeat it " + scream +   " How are you!"
print(f"My name is {scream}")
print(greeting)
