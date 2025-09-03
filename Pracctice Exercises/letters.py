letters = list("Hello World")

sentence = list("The quick brown fox jumps over the lazy dog")

while " " in sentence:
    sentence.remove(" ")

while " " in letters:
    letters.remove(" ")

print(sentence)
print(letters)

nums = [1,2,3,4,5,6]

results = []
for i in nums:
    i = i * 2
    results.append(i)

print(results)

results_2 = [i*2 for i in nums]
print(results_2)

upper_letters = [l.upper() for l in letters]
print(upper_letters)