#Strings
S = "Gowtham"
print(S)

#String length
print(f"length: {len(S)}")

#String with index splits
print("'{}' is the last letter of word Gowtham.".format(S[-1]))

print("'{}' is the second letter of word Gowtham.".format(S[1]))

print("'{}' letters from o to a in Gowtham.".format(S[1:-1]))

#Immutability
'''S[0] = "J"
Traceback (most recent call last):
  File "C:/Users/Gowtham/PycharmProjects/dummy.py", line 16, in <module>
    S[0] = "J"
TypeError: 'str' object does not support item assignment'''

#Listed String
print(f"{list(S)} - String 'S' is split into list of characters.")

#Find
print(f"{S.find('am')} is the 'am' starting index.")

#replace
A="Gowtham"
print(f"{A.replace('am','AM')} - replaces the last two letters to Caps form of Gowtham.")

#Uppercase
print(A.upper())

#Lowercase
print(A.lower())

#Alphanumeric
print(A.isalpha())

#concatenate
print(A+"ram")
print(A.__add__('ram'))

