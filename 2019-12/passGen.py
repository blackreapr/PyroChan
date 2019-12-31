import random
import string


def password_generator(size):
    latters = ""
    for i in range(size):
        upper = random.choice(string.ascii_uppercase)
        lower = random.choice(string.ascii_lowercase)
        digit = int(random.random() * 10)
        pw = upper + lower + str(digit)
        latters = latters + random.choice(pw)
    return latters


def save_password(siteName, pwd):
    with open("passwordsGenerated.txt", "a") as pgen:
        pgen.write(siteName + ": " + pwd + "\n")
    pgen.close()


def main():
    website = input("Enter the name of the website:\n")
    size = int(input("Enter the length of your password that you want:\n"))
    password = password_generator(size)
    print(password)
    save_password(website, password)


if __name__ == "__main__":
    main()