str = "pwwkew"
substrings = []
max_length = 0
 
for i in range(len(str)):
    for j in range(i + 1, len(str) + 1):
        # print(j)
        substrings.append(str[i:j])

for substring in substrings:
    if len(set(substring)) == len(substring):
        max_length = max(max_length, len(substring))

print(max_length)
'''

you can iterate through the string and add each char to a set, and
if the char is already in the set, return a boolean like True

or just pass the string to a set and compare that to the length of the string

iterate through the list of substrings and check if the string has repeating characters
if it does not, assign its length to a variable (if it is greater than the current value)
'''

