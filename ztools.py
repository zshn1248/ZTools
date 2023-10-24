import getpass

password = "zeeshan123"
username = "zshn"

userIn = str(input("Enter username: "))
if userIn == "exit":
    exit()
while userIn != username:
    print("User not found!")
    userIn = input("Enter username: ")
    if userIn == "exit":
        exit()

passIn = getpass.getpass("Enter password: ")
if passIn == "exit":
    exit()
while passIn != password:
    if passIn == "exit":
        exit()
    print("Incorrect password!")
    passIn = getpass.getpass("Enter password: ")

print(f"User {username} logged in")
print("""
[0] Exit
[1] Generate random wordlist
""")

zcmd = input(f"{username}@zcmd> ")

if zcmd == "0":
    exit()
elif zcmd == "1":
    import random
    x = 0
    y = int(input("Number of words: "))
    wordLength = int(input("Enter word length: "))
    charmap = "asdfghjklqwertyuiopzxcvbnm"
    filename = input("Enter filename: ")

    if ".txt" not in filename:
        filename = filename + ".txt"

    file = open(filename, "a+")

    while x < y:
        random_word = ''.join(random.choice(charmap) for _ in range(wordLength))
        print(random_word)
        file.write(f"{random_word}\n")
        x += 1

    file.close()
