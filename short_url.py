import random
import string
def generate_short_url(Length=5):
    characters=string.ascii_letters+string.digits
    return ''.join(random.choice(characters) for _ in range(Length))


#dictionary to store short code
url_mapping = {}
'''example: add manually one long and short code
short_code = "abc213"
long_code = "https://www.google.com"

#store the code in url_mapping
url_mapping[short_code] = long_code

#print the dictionary
print(url_mapping)
'''

#ask user for long_code
long_code = input("enter the long_code")
#generate a short code
short_code = generate_short_url()
#save in long code
url_mapping[short_code]=long_code
#show the short url
print(f"short URL is:https://short.ly{short_code}")


short_code = input("enter the short_code")
#retrieving URL using short url
short_url_input = input("Enter the short url to retrive:")
short_code_input = short_url_input.split("/")[-1]

#look for code in dictionary
if short_code_input in url_mapping:
    print(f"the original URL is : {url_mapping[short_code_input]}")
else:
    print(f"SORRY!! the url is not found")


