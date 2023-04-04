from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("Enter the master password: ")
key =load_key()
fer = Fernet(key)

# write_key()




def add():
    name = input("Account Name: ")
    password = input("Password: ")
    with open("password.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pw = data.split("|")
            print(f"Account Name: {user}, Password: {fer.decrypt(pw.encode()).decode()}")



while True:
    do_you = input("Do you want to add a password or view (add, view), or you can press Q to quit: ").lower()
    if do_you=='q':
        break

    if do_you == "add":
        add()
    
    if do_you=="view":
        view()