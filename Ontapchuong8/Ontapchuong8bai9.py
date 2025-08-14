Sentence=input('Nhap mot cau bat ki: ')
vowels='ueoaiUEOAI'
vowel_count=0
for char in Sentence:
    if char in vowels:
        vowel_count=vowel_count+1
print(vowel_count)