def count_word(my_string):
    word_list = my_string.split()
    print(word_list)
    count = len(word_list)

    return count

result = count_word("How was your day ?")
print(result)