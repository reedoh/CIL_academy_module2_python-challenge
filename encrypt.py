import random, time
from datetime import datetime
from prettytable import PrettyTable

rslt = PrettyTable()


def encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""

    for char in plaintext:
        # print(char)
        ciphertext += char
        keycount = 0
        while keycount < key:
            ciphertext += random.choice(alphabet)
            keycount += 1
        # print(ciphertext)
    return ciphertext


def result_table(plaintext, ciphertext, key):
    timen = datetime.now()
    datenow = timen.strftime("%d:%m:%y")
    timenow = timen.strftime("%H:%M:%S")
    rslt.add_row([datenow, timenow, plaintext, ciphertext, key])


def action_button():
    action_list = ["yes", "y", "no", "n"]
    button = input('Enter "yes" to encrypt more or "no" to exit : ').lower()
    while not (button in action_list):
        print("invalid Response!  input  in the below format")
        button = input('Enter "yes" to decrypt more or "no" to exit : ').lower()
    if button == "yes" or button == "y":
        main_loop()
    elif button == "no" or button == "n":
        exit()


def main_loop():

    # Generate result For a single & continous input from user - Uncomment this block
    plaintext = input("Enter a message to encrypt (plaintext) : ")
    key = int(input("Input a key as a number between 1 and 10 : "))
    while not (key >= 1 and key <= 10):
        print("Invalid key, try again!")
        key = int(input("Input a key as a number between 1 and 10 :"))
    ciphertext = encrypt(plaintext, key)
    print(ciphertext)
    result_table(plaintext, ciphertext, key)

    """
    # Generate result For a list of defined texts- Uncomment this block
    plaintext = [
        "Yellow submarine",
        "Hey Jude",
        "Paperback Writer",
        "Here Comes the Sun",
        "Penny Lane",
        "Cil Academy",
        "pythonista!",
    ]
    keys = [4, 7, 3, 1, 5, 4, 7]
    for text, key in zip(plaintext, keys):
        ciphertext = encrypt(text, key)
        result_table(text, ciphertext, key)
    """

    # Process...
    print("Encrypting plaintext...")
    time.sleep(1)
    file = open("Solution.txt", "w")
    file.write(str(rslt))
    file.close()
    print(rslt)
    action_button()


# Main program starts here...
rslt.field_names = ["Date", "Time", "text", "cipher", "key"]  # Generate table header
main_loop()
