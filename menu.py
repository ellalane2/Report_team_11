from ella_encoder import encode
from decoder import decode
def menu():
    encoded_pass= ''
    og_password= ''
    True
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        print("Please enter an option:")
        option= int(input())
        if option == 1:
            og_password= str(input())
            encoded= encoder(og_password)
            print("Your password has been encoded and stored!")

        elif option == 2:
            if encoded_pass:
                password= decoder(encoded)
                print(f'The encoded password is {encoded}, and the original password is {password}.')

        elif option == 3:
            break
if __name__=="__main__":
    menu()
