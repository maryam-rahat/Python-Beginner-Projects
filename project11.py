# site checker
# urllib.req
# function that takes url
# return response

import urllib.request as urllib

def main(url):
    print("Checking connectivity ")

    response = urllib.urlopen(url)
    print("Connected to the", url, "successfully")
    print("The response code was:", response.getcode())

print("This is a site connectivity checher program")
input_url = input("Please enter the url: ")

if __name__ == '__main__':
    main(input_url)