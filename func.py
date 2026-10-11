# # check valid email id
# import re
# def validate_email(email):
#     P= r'^[A-Za-z0-9._-]+@[A-Za-z0-9]+\.[A-Za-z]{2,6}$'

#     if re.match(P, email):
#         return 'Valid'
#     else:
#         return 'Invaid'
# email = input("Enter your email: ")
# print(validate_email(email))


# # check password
# import re
# def check_pass(p):
#     if len(p)<8:
#         return 'weak password'
#     if not re.search(r'[A-Z]', p):
#         return 'weak password'
#     if not re.search(r'[a-z]', p):
#             return 'weak password'
#     if not re.search(r'[0-1]', p):
#             return 'weak password'
#     if not re.search(r'[!@#$%^&*()_]', p):
#             return 'weak password'
#     return 'strong password'
# p=input("Enter a Password:-")
# print(check_pass(p))


#### Find hashtag words
# import re
# def extract_hashtags(text):
#      pattern = r'#[A-Za-z0-9_]+'
#      hashtags = re.findall(pattern, text)
#      return hashtags
# text=input("Enter social media post:-")
# print(extract_hashtags(text))



# To check valid IP address
import re
def valid_ip(IP):
    p=r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
    if re.match(p,IP):
        return 'Valid'
    else:
        return 'Invalid'
IP=input("Enter IP address:-")
print(valid_ip(IP))
    

