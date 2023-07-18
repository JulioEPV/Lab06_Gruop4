# Julio Enrique Pinzon Vargas

#functions
def encode(password):
    enc_password = ''

    for i in password:
        if i == '0':
            i='3'
            enc_password = enc_password + i
        elif i == '1':
            i='4'
            enc_password = enc_password + i
        elif i == '2':
            i='5'
            enc_password = enc_password + i
        elif i == '3':
            i='6'
            enc_password = enc_password + i
        elif i == '4':
            i='7'
            enc_password = enc_password + i
        elif i == '5':
            i='8'
            enc_password = enc_password + i
        elif i == '6':
            i='9'
            enc_password = enc_password + i
        elif i == '7':
            i='0'
            enc_password = enc_password + i
        elif i == '8':
            i='1'
            enc_password = enc_password + i
        elif i == '9':
            i='2'
            enc_password = enc_password + i
    return enc_password

def decode(enc_password):
    dcd_password = ''
    for num in enc_password:
        if int(num) < 3:
            pass_val = int(num) + 7
            dcd_password += str(pass_val)
        else:
            pass_val = int(num) - 3
            dcd_password += str(pass_val)
    return dcd_password


def main():
    # Variables - Initial values
    program_on = True
    enc_password = None

    while program_on == True:
        # Display the menu
        print('Menu \n------------- \n1. Encode \n2. Decode \n3. Quit')

        # User option
        user_option = int(input('Please enter an option:'))

        if user_option == 1:
            password = str(input('Please enter your password to encode:'))
            enc_password = encode(password)
            print(enc_password)

        if user_option == 2:
            dcd_password = decode(enc_password)
            print(f"The encoded password is {enc_password}, and the original password is {dcd_password}.")

        if user_option == 3:
            program_on = False


if __name__ == "__main__":
    main()
