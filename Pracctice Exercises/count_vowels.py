def vowel_counter(my_string):

    freq_dict = {}
    vowels = ['a','e','i','o','u']

    for char in my_string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    vowel_counter = 0

    for k,v in freq_dict.items():
        if k in vowels:
            vowel_counter += v

    return vowel_counter

result = vowel_counter("my name is baseer")
print(result)
