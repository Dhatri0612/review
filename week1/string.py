text="python programming"
vowels="aeiouAEIOU"
vowel_count=0
cons_count=0
upper_count=0
for ch in text:
    if ch.isalpha():
        if ch in vowels:
            vowel_count+=1
        else :
            cons_count+=1
    if ch.isupper():
        upper_count+=1
with open("string.txt",'w')as f:
    f.write(f"Input: {text}\n")
    f.write(f"Vowels: {vowel_count}\n")
    f.write(f"Consonants: {cons_count}\n")
    f.write(f"Uppercase: {upper_count}\n")

with open("string.txt",'r')as f:
    data=f.read()
    print(data)