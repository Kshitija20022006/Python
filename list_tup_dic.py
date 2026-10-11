# ###---11
# import re
# # Function to validate email
# def validate_email(email):
#     pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$'

#     if re.match(pattern, email):
#         return True
#     else:
#         return False


# # Take email input from user
# email = input("Enter your email address: ")

# # Check email
# if validate_email(email):
#     print("Valid email address")
# else:
#     print("Invalid email address")



#####----12---
# import re
# # Function to extract phone numbers
# def extract_phone_numbers(text):
#     pattern = r'(?:\(\d{3}\)\s*\d{3}[-.]?\d{4}|\b\d{3}[-.]\d{3}[-.]\d{4}\b|\b\d{10}\b)'

#     phone_numbers = re.findall(pattern, text)

#     return phone_numbers

# # Take text input from user
# text = input("Enter a block of text: ")

# # Extract phone numbers
# numbers = extract_phone_numbers(text)

# # Display the result
# print("\nPhone numbers found:")

# if numbers:
#     for number in numbers:
#         print(number)
# else:
#     print("No phone numbers found.")


# ####-----13---
# import re

# # Function to extract URLs
# def extract_urls(html):
#     pattern = r'(?:https?://|www\.)[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[A-Za-z0-9._~:/?#\[\]@!$&\'()*+,;=%-]*)?'
#     urls = re.findall(pattern, html)
#     return urls
# # Take HTML input from user
# html = input("Enter HTML content: ")

# # Extract URLs
# urls = extract_urls(html)

# # Display URLs
# print("\nExtracted URLs:")

# if urls:
#     for url in urls:
#         print(url)
# else:
#     print("No URLs found.")


# ###---14---
# import re
# # Function to check password strength
# def check_password(password):

#     # Check minimum 8 characters
#     if len(password) < 8:
#         return False

#     # Check uppercase letter
#     if not re.search(r'[A-Z]', password):
#         return False

#     # Check lowercase letter
#     if not re.search(r'[a-z]', password):
#         return False

#     # Check digit
#     if not re.search(r'[0-9]', password):
#         return False

#     # Check special character
#     if not re.search(r'[!@#$%^&*()_\-]', password):
#         return False
    
#     return True

# # Take password input from user
# password = input("Enter your password: ")

# # Check password
# if check_password(password):
#     print("Strong password")
# else:
#     print("Weak password")


# ####---15---(one output is show)
# import re
# from datetime import datetime

# # Function to extract and convert dates
# def extract_dates(text):
#     dates = []

#     # Regular expression for different date formats
#     pattern = r'\b(?:\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|\d{4}\.\d{2}\.\d{2}|(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})\b'

#     matches = re.findall(pattern, text)

#     for date in matches:

#         try:
#             # DD/MM/YYYY
#             if "/" in date:
#                 new_date = datetime.strptime(date, "%d/%m/%Y")

#             # MM-DD-YYYY
#             elif "-" in date:
#                 new_date = datetime.strptime(date, "%m-%d-%Y")

#             # YYYY.MM.DD
#             elif "." in date:
#                 new_date = datetime.strptime(date, "%Y.%m.%d")

#             # Month Day, Year
#             else:
#                 new_date = datetime.strptime(date, "%B %d, %Y")

#             # Convert to YYYY-MM-DD
#             dates.append(new_date.strftime("%Y-%m-%d"))

#         except ValueError:
#             # Ignore invalid dates
#             pass

#     return dates

# # Take input from user
# text = input("Enter a block of text: ")

# # Extract dates
# result = extract_dates(text)

# # Display result
# print("\nDates in YYYY-MM-DD format:")

# if result:
#     for date in result:
#         print(date)
# else:
#     print("No valid dates found.")



# ####----16
# import re

# # Function to remove HTML tags
# def remove_html_tags(html):
#     # Regular expression to find HTML tags
#     pattern = r'<[^>]*>'

#     # Remove HTML tags
#     clean_text = re.sub(pattern, '', html)

#     return clean_text


# # Take HTML input from user
# html = input("Enter HTML content: ")

# # Remove HTML tags
# result = remove_html_tags(html)

# # Display cleaned text
# print("\nCleaned Text:")
# print(result)


# ####-----17
# import re

# # Function to extract hashtags
# def extract_hashtags(text):
#     pattern = r'#[A-Za-z0-9_]+'

#     hashtags = re.findall(pattern, text)

#     return hashtags


# # Take input from user
# text = input("Enter a social media post: ")

# # Extract hashtags
# result = extract_hashtags(text)

# # Display hashtags
# print("\nExtracted Hashtags:")

# if result:
#     for hashtag in result:
#         print(hashtag)
# else:
#     print("No hashtags found.")


# ###----18
# import re

# # Function to extract and count file extensions
# def count_extensions(filenames):
#     extension_count = {}

#     for filename in filenames:
#         # Find file extension
#         match = re.search(r'(\.[A-Za-z0-9]+)$', filename)

#         if match:
#             extension = match.group(1).lower()

#             if extension in extension_count:
#                 extension_count[extension] += 1
#             else:
#                 extension_count[extension] = 1

#     return extension_count

# # Take number of files from user
# n = int(input("Enter number of files: "))

# filenames = []

# # Take filenames as input
# for i in range(n):
#     filename = input("Enter filename " + str(i + 1) + ": ")
#     filenames.append(filename)

# # Count extensions
# result = count_extensions(filenames)

# # Display result
# print("\nFile Extension Count:")
# print(result)


# ###----19---
# import re

# # Function to validate IP address
# def validate_ip(ip):
    
#     # IPv4 pattern
#     ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'

#     # IPv6 pattern
#     ipv6_pattern = r'^([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}$'

#     # Check IPv4
#     if re.match(ipv4_pattern, ip):
#         return True

#     # Check IPv6
#     if re.match(ipv6_pattern, ip):
#         return True

#     return False

# # Take IP address from user
# ip = input("Enter an IP address: ")

# # Validate IP address
# if validate_ip(ip):
#     print("Valid IP address")
# else:
#     print("Invalid IP address")


###----20--
