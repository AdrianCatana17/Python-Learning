def main():
    email_input = input("Input your e-mail address: ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username: ", username)
    print("Domain: ",domain)
    print("Extension: ",extension)

main()