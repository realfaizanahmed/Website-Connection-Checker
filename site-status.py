import urllib.request as urllib

def main(url):
    print("Checking Connectivity")
    response = urllib.urlopen(url)
    print("Connected to",url,"successfully")
    print("The response code was:", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Enter the URL of the site: ")
main(input_url)