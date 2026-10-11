####----21--
# import re

# # Take text and search query from user
# text = input("Enter the text: ")
# query = input("Enter the word to search: ")

# # Count occurrences ignoring case
# count = len(re.findall(re.escape(query), text, re.IGNORECASE))

# # Highlight all occurrences
# highlighted_text = re.sub(
#     re.escape(query),
#     lambda match: "**" + match.group(0) + "**",
#     text,
#     flags=re.IGNORECASE
# )

# # Display results
# print("\nNumber of occurrences:", count)
# print("\nHighlighted text:")
# print(highlighted_text)



# ###----22--(error)
# import string

# # Predefined list of common stopwords
# stopwords = {
#     "is", "am", "are", "was", "were", "the", "a", "an",
#     "and", "or", "but", "in", "on", "at", "to", "of",
#     "for", "with", "this", "that", "it", "as", "by",
#     "from", "be", "has", "have", "had"
# }
# # Function to remove stopwords
# def remove_stopwords(text):
#     words = text.split()
#     cleaned_words = []

#     for word in words:
#         # Remove punctuation for checking the word
#         clean_word = word.strip(string.punctuation)

#         if clean_word.lower() not in stopwords:
#             cleaned_words.append(word)

#     # Join words with proper spacing
#     return " ".join(cleaned_words)

# # Take input from user
# text = input("Enter a paragraph: ")

# # Remove stopwords
# cleaned_text = remove_stopwords(text)

# # Display result
# print("\nOriginal Text:")
# print(text)

# print("\nCleaned Text:")
# print(cleaned_text)


######----23---(error)
# import re

# # Take input from user
# filename = input("Enter the input file name: ")
# target = input("Enter the word or phrase to find: ")
# replacement = input("Enter the replacement word or phrase: ")

# choice = input("Case-sensitive replacement? (yes/no): ")


# # Read the input file
# with open(filename, "r") as file:
#     text = file.read()


# # Perform find and replace
# if choice.lower() == "yes":
#     # Case-sensitive replacement
#     new_text = text.replace(target, replacement)
#     count = text.count(target)

# else:
#     # Case-insensitive replacement
#     new_text = re.sub(
#         re.escape(target),
#         replacement,
#         text,
#         flags=re.IGNORECASE
#     )

#     # Count occurrences
#     count = len(re.findall(re.escape(target), text, re.IGNORECASE))


# # Create a new output file
# output_file = "modified_" + filename

# with open(output_file, "w") as file:
#     file.write(new_text)


# # Display result
# print("\nFind-and-replace completed successfully.")
# print("Occurrences replaced:", count)
# print("Modified file saved as:", output_file)


# ####---24---
# import re

# # Function to split text into sentences
# def sentence_segmentation(text):

#     # Protect common abbreviations
#     abbreviations = {
#         "Mr.": "Mr",
#         "Mrs.": "Mrs",
#         "Ms.": "Ms",
#         "Dr.": "Dr",
#         "Prof.": "Prof",
#         "Sr.": "Sr",
#         "Jr.": "Jr",
#         "etc.": "etc"
#     }

#     for abbr, replacement in abbreviations.items():
#         text = text.replace(abbr, replacement)

#     # Split at ., !, or ? followed by whitespace
#     sentences = re.split(r'(?<=[.!?])\s+', text.strip())

#     # Restore abbreviations
#     for i in range(len(sentences)):
#         for abbr, replacement in abbreviations.items():
#             sentences[i] = sentences[i].replace(
#                 replacement, abbr
#             )

#     return sentences

# # Take input from user
# text = input("Enter a block of text: ")

# # Perform sentence segmentation
# sentences = sentence_segmentation(text)

# # Display sentences
# print("\nSentences:")

# for i, sentence in enumerate(sentences, 1):
#     print(i, ".", sentence)



# ###----25--
# import re
# from collections import Counter

# # Function to summarize text
# def summarize_text(text, num_sentences=2):

#     # Split text into sentences
#     sentences = re.split(r'(?<=[.!?])\s+', text.strip())

#     # Remove punctuation and convert words to lowercase
#     words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

#     # Common stopwords
#     stopwords = {
#         "the", "is", "a", "an", "and", "or", "of", "to",
#         "in", "on", "for", "with", "this", "that", "it",
#         "are", "was", "were", "be", "as", "by", "from"
#     }

#     # Count important words
#     word_frequency = Counter(
#         word for word in words if word not in stopwords
#     )

#     # Calculate score for each sentence
#     sentence_scores = {}

#     for sentence in sentences:
#         sentence_words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())

#         score = 0
#         for word in sentence_words:
#             score += word_frequency.get(word, 0)

#         sentence_scores[sentence] = score

#     # Select highest-scoring sentences
#     ranked_sentences = sorted(
#         sentence_scores,
#         key=sentence_scores.get,
#         reverse=True
#     )

#     summary = ranked_sentences[:num_sentences]

#     # Return summary in original order
#     summary = [sentence for sentence in sentences if sentence in summary]

#     return " ".join(summary)


# # Take text input from user
# text = input("Enter a paragraph or long text: ")

# # Take number of sentences for summary
# n = int(input("Enter number of sentences for summary: "))

# # Generate summary
# summary = summarize_text(text, n)

# # Display result
# print("\n----- SUMMARY -----")
# print(summary)



# ###---26---
# import re

# # Dictionary of common contractions
# contractions = {
#     "don't": "do not",
#     "doesn't": "does not",
#     "didn't": "did not",
#     "can't": "cannot",
#     "couldn't": "could not",
#     "won't": "will not",
#     "wouldn't": "would not",
#     "isn't": "is not",
#     "aren't": "are not",
#     "wasn't": "was not",
#     "weren't": "were not",
#     "haven't": "have not",
#     "hasn't": "has not",
#     "hadn't": "had not",
#     "I'm": "I am",
#     "you're": "you are",
#     "he's": "he is",
#     "she's": "she is",
#     "it's": "it is",
#     "we're": "we are",
#     "they're": "they are"
# }

# # Function to normalize text
# def normalize_text(text):

#     # Convert text to lowercase
#     text = text.lower()

#     # Expand contractions
#     for contraction, expansion in contractions.items():
#         text = text.replace(contraction.lower(), expansion.lower())

#     # Remove numbers
#     text = re.sub(r'\d+', '', text)

#     # Remove punctuation and special characters
#     text = re.sub(r'[^a-zA-Z\s]', '', text)

#     # Remove extra spaces
#     text = re.sub(r'\s+', ' ', text).strip()

#     return text


# # Take input from user
# text = input("Enter a block of text: ")

# # Clean the text
# cleaned_text = normalize_text(text)

# # Display result
# print("\nOriginal Text:")
# print(text)

# print("\nCleaned Text:")
# print(cleaned_text)



#####---27
# import re

# # Function to check palindrome
# def is_palindrome(text):
#     # Convert to lowercase and remove spaces/punctuation
#     normalized_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()

#     # Check forward and backward
#     if normalized_text == normalized_text[::-1]:
#         return True
#     else:
#         return False


# # Take input from user
# text = input("Enter a word or phrase: ")

# # Check palindrome
# result = is_palindrome(text)

# # Display result
# print("Is palindrome:", result)


###----28--
# import re
# from collections import Counter

# # Function to extract keywords
# def extract_keywords(text):

#     # Convert text to lowercase
#     text = text.lower()

#     # Extract words
#     words = re.findall(r'\b[a-zA-Z]+\b', text)

#     # Predefined stopwords
#     stopwords = {
#         "the", "is", "a", "an", "and", "or", "of", "to",
#         "in", "on", "for", "with", "this", "that", "it",
#         "are", "was", "were", "be", "by", "as", "from",
#         "at", "can", "has", "have", "had", "which", "their",
#         "they", "we", "our", "also", "using", "used"
#     }

#     # Remove stopwords
#     important_words = []

#     for word in words:
#         if word not in stopwords:
#             important_words.append(word)

#     # Count word frequency
#     frequency = Counter(important_words)

#     # Get top 5 keywords
#     top_keywords = frequency.most_common(5)

#     return top_keywords


# # Take input from user
# text = input("Enter research paper text: ")

# # Extract keywords
# keywords = extract_keywords(text)

# # Display result
# print("\nTop 5 Keywords:")

# for word, count in keywords:
#     print(word, ":", count)


###----29--(2 code)
# import re

# # Predefined dictionary of correctly spelled words
# dictionary = {
#     "this", "is", "a", "simple", "python", "program",
#     "to", "check", "spelling", "in", "the", "text",
#     "hello", "world", "computer", "science", "student",
#     "learning", "programming", "language", "good", "morning"
# }


# # Function to find misspelled words
# def spell_checker(text):
#     # Extract words from text
#     words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

#     misspelled = []

#     for word in words:
#         if word not in dictionary and word not in misspelled:
#             misspelled.append(word)

#     return misspelled


# # Take input from user
# text = input("Enter a block of text: ")

# # Check spelling
# result = spell_checker(text)

# # Display result
# print("\nMisspelled words:")

# if result:
#     print(result)
# else:
#     print("No misspelled words found.")



# #####---29--
# # Class to represent a Book
# class Book:

#     # Constructor
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.status = "Available"

#     # Borrow the book
#     def borrow_book(self):
#         if self.status == "Available":
#             self.status = "Borrowed"
#             print("Book borrowed successfully.")
#         else:
#             print("Book is already borrowed.")

#     # Return the book
#     def return_book(self):
#         self.status = "Available"
#         print("Book returned successfully.")

#     # Show book details
#     def show_details(self):
#         print("\n----- Book Details -----")
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Year of Publication:", self.year)
#         print("Availability:", self.status)


# # Take input from user
# title = input("Enter book title: ")
# author = input("Enter author name: ")
# year = int(input("Enter year of publication: "))

# # Create Book object
# book = Book(title, author, year)

# # Show initial details
# book.show_details()

# # Borrow the book
# book.borrow_book()
# book.show_details()

# # Return the book
# book.return_book()
# book.show_details()



# ####---30---(CTI)
# # Bank Account Program
# class BankAccount:
#     # Class-level counter for unique account numbers
#     account_counter = 1000

#     # Constructor
#     def __init__(self, account_holder):
#         self.account_holder = account_holder
#         self.balance = 0
#         BankAccount.account_counter += 1
#         self.account_number = BankAccount.account_counter

#     # Deposit money
#     def deposit(self, amount):
#         self.balance += amount
#         print(amount, "deposited successfully.")

#     # Withdraw money
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(amount, "withdrawn successfully.")
#         else:
#             print("Error: Insufficient balance.")

#     # Display balance
#     def display_balance(self):
#         print("Account Holder:", self.account_holder)
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)

#     # Transfer money
#     def transfer(self, amount, other_account):
#         if amount <= self.balance:
#             self.balance -= amount
#             other_account.balance += amount
#             print(amount, "transferred successfully to",
#                   other_account.account_holder)
#         else:
#             print("Error: Insufficient balance for transfer.")

# # Create two BankAccount objects
# account1 = BankAccount("Rahul")
# account2 = BankAccount("Priya")

# # Display initial details
# print("\n--- Initial Accounts ---")
# account1.display_balance()
# print()
# account2.display_balance()

# # Deposit money
# print("\n--- Deposits ---")
# account1.deposit(5000)
# account2.deposit(3000)

# # Display balances
# print("\n--- After Deposits ---")
# account1.display_balance()
# print()
# account2.display_balance()

# # Withdraw money
# print("\n--- Withdrawal ---")
# account1.withdraw(1000)

# # Transfer money
# print("\n--- Transfer ---")
# account1.transfer(1500, account2)

# # Final balances
# print("\n--- Final Balances ---")
# account1.display_balance()
# print()
# account2.display_balance()