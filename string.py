#count the string length
# s=input()
# count=0
# for i in s:
#     count+=1
# print("Length of the string:-",count)


# # character count
# s=input()
# v=0
# c=0
# d=0
# space=0
# special_char=0
# for i in s:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' :
#         v+=1
#     elif 'a'<=i>='z' or 'A'<=i>='Z':
#         c+=1
#     elif '0'<=i<='9':
#         d+=1
#     elif i==' ':
#         space+=1
#     else :
#         special_char+=1
# print("Vowels are:-",v)
# print(c)
# print(d)
# print(space)
# print(special_char)


# #Reverse string
# s=input()
# print(s[::-1])


# #Palindrome 
# s=input()
# a=s[::-1]
# if a==s:
#     print("String is Palindrome")
# else:
#     print("String is not Palindrome")


# #Count Upercase and lowercase
# s=input()
# u=0
# a=0
# l=0
# for i in s:
#     if 'A'<=i<='Z':
#         u+=1
#     elif i==' ':
#         a+=1
#     else:
#         l+=1
# print("Upercase:-",u)
# print("Lowercase:-",l)
# print("Space:-",a)


#Replace character
# s=input()
# old=input()
# new=input()
# for i in s:
#     if i==old:
#         print(new,end=' ')
#     else:
#         print(i,end=' ')


#Remove spaces
# s=input()
# new=''
# for i in s:
#     if i!=' ':
#         new+=i
# print(new)


#Frequency of character
# s=input("Enter a string:-")
# ch=input()
# count=0
# for i in s:
#     if i==ch:
#         count+=1
# print(count)


#print 1st and last character
# s=input()
# print("First character of string:-",s[0:1])
# print("Last character of string:-",s[-1:-2:-1])


#ASCII value
# s=input()
# for i in s:
#     print(i,'-',ord(i))


#word count
# s=input().split()
# c=0
# for i in s:
#     c+=1
# print(c)


#Longest word in string
# s=input()
# w=s.split()
# long=w[0]
# for  i in w:
#     if len(i)>len(long):
#         long=i
# print("Longest word:-",long)


# Smallest word in string
# s=input()
# w=s.split()
# small=w[0]
# for  i in w:
#     if len(i)<len(small):
#         small=i
# print("Longest word:-",small)


#Convert first letter in capital
# s=input()
# word=s.split()
# result=''
# for i in word:
#     result=result+i[0].upper()+i[1:]+' '         #' ' this use for space between each words
# print(result)


#Duplicates characters
# s = input("Enter a string: ")
# for ch in set(s):
#     if s.count(ch) > 1:
#         print(ch)


#Character Frequency
# s = input("Enter a string: ")
# checked = ""
# for ch in s:
#     if ch not in checked:
#         print(ch, ":", s.count(ch))
#         checked = checked + ch

# Anagram check
# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")


# Remove Duplicate Characters
# s = input("Enter a string: ")
# result = ""
# for ch in s:
#     if ch not in result:
#         result = result + ch
# print(result)


# Substring search
# s = input("Enter main string: ")
# sub = input("Enter substring: ")
# if sub in s:
#     print("Substring found")
# else:
#     print("Substring not found")


# Count occurrences word
# sentence = input("Enter a sentence: ")
# word = input("Enter word: ")
# words = sentence.split()
# count = 0
# for w in words:
#     if w == word:
#         count = count + 1
# print("Count:", count)


# Password validation
# password=input("Enter a password:-")
# upper=False
# lower=False
# digit=False
# special=False
# for ch in password:
#     if ch.isupper():
#         upper=True
#     elif ch.lower():
#         lower=True
#     elif ch.digit():
#         digit=True
#     else:
#         special=True
# if len(password) >=8 and upper and lower and digit and special:
#     print("Password is valid")
# else:
#     print("Password is invalid")


# # Run-Length Encoding
# s = input("Enter a string: ")
# result = ""
# count = 1
# for i in range(len(s)):
#     if i + 1 < len(s) and s[i] == s[i + 1]:
#         count += 1
#     else:
#         result += s[i] + str(count)
#         count = 1
# print("Encoded string:", result)

# # String Compression
# s = input("Enter a string: ")
# compressed = ""
# count = 1
# for i in range(len(s)):
#     if i + 1 < len(s) and s[i] == s[i + 1]:
#         count += 1
#     else:
#         compressed += s[i] + str(count)
#         count = 1
# if len(compressed) < len(s):
#     print("Compressed string:", compressed)
# else:
#     print("Original string:", s)


# # Most Frequent Character
# s = input("Enter a string: ")
# frequency = {}
# for ch in s:
#     frequency[ch] = frequency.get(ch, 0) + 1
# most_frequent = max(frequency, key=frequency.get)
# print("Most frequent character:", most_frequent)
# print("Frequency:", frequency[most_frequent])


# # Second Most Frequent Character
# s = input("Enter a string: ")
# frequency = {}
# for ch in s:
#     frequency[ch] = frequency.get(ch, 0) + 1
# sorted_chars = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
# if len(sorted_chars) >= 2:
#     print("Second most frequent character:", sorted_chars[1][0])
#     print("Frequency:", sorted_chars[1][1])
# else:
#     print("Second most frequent character does not exist.")


# # Caesar Cipher
# text = input("Enter the message: ")
# shift = int(input("Enter the shift value: "))
# encrypted = ""
# for ch in text:
#     if ch.isupper():
#         encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
#     elif ch.islower():
#         encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
#     else:
#         encrypted += ch
# print("Encrypted message:", encrypted)
# decrypted = ""
# for ch in encrypted:
#     if ch.isupper():
#         decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
#     elif ch.islower():
#         decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
#     else:
#         decrypted += ch
# print("Decrypted message:", decrypted)



# # Email Validator
# email = input("Enter email address: ")
# if "@" in email and "." in email and email.index("@") < email.rindex("."):
#     print("Valid email address")
# else:
#     print("Invalid email address")


# # Word Frequency Dictionary
# paragraph = input("Enter a paragraph: ")
# words = paragraph.lower().split()
# frequency = {}
# for word in words:
#     frequency[word] = frequency.get(word, 0) + 1
# print("Word Frequency:")
# for word, count in frequency.items():
#     print(word, ":", count)


# # Word Frequency Dictionary
# paragraph = input("Enter a paragraph: ")
# words = paragraph.lower().split()
# frequency = {}
# for word in words:
#     frequency[word] = frequency.get(word, 0) + 1
# print("Word Frequency:")
# for word, count in frequency.items():
#     print(word, ":", count)



# # Sentence Reversal
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# reversed_sentence = " ".join(words[::-1])
# print("Reversed sentence:", reversed_sentence)


# # String Rotation
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# if len(str1) == len(str2) and str2 in (str1 + str1):
#     print("Yes, the second string is a rotation of the first string.")
# else:
#     print("No, the second string is not a rotation of the first string.")