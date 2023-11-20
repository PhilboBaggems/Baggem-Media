# ui/input - This is where things that get info from the user live.

def user_credentials():
    username = input("Enter your Google account email address: ")
    password = input("Enter your Google account password: ")
    return username, password

# def flow_selection():
