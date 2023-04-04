# ask for input email
# split the email from @
# ist part is username, seond part would become the domain
# split by . too (.com)

def main():
    print('This is an email splitter')
    print('')

    ask = input('Please enter your email: ')

    (username, domain) = ask.split('@')
    (domain, extension) = domain.split('.')

    print('Username: ', username)
    print('Domain: ', domain)
    print('Extension: ', extension) 

if __name__ == '__main__':
    main()
