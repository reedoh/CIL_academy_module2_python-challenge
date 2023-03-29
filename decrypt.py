import random, time


def decrypt(ciphertext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ciphertext[:: key + 1]
    return plaintext


def action_button():
    action_list = ["yes", "y", "no", "n"]
    button = input('Enter "yes" to decrypt more or "no" to exit : ').lower()
    while not (button in action_list):
        print("invalid Response!  input  in the below format")
        button = input('Enter "yes" to decrypt more or "no" to exit : ').lower()
    if button == "yes" or button == "y":
        main_loop()
    elif button == "no" or button == "n":
        exit()


def main_loop():
    ciphertext = input("Enter a message to decrypt (ciphertext)")
    key = int(input("Input a key as a number between 1 and 10 : "))
    while not (key >= 1 and key <= 10):
        print("Invalid key, try again!")
        key = int(input("Input a key as a number between 1 and 10 : "))

    print("Decrypting plaintext...")
    time.sleep(1)
    print(f"Your cipher : {ciphertext}, and key : {key}")
    plaintext = decrypt(ciphertext, key)
    print("Done !")
    print(f"Your Plaintext : {plaintext}")
    time.sleep(1)
    action_button()


main_loop()
