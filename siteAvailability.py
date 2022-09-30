import urllib.request as urllib


def main(url):
    print("Checking connectivity")

    response = urllib.urlopen(url)
    print("Connected to ", url, "successfully")
    print("The response code was: ", response.getcode())


print("This is a site connectivity checker program")
input_url = input("Enter URL of site you wish to check: ")

main(input_url)
