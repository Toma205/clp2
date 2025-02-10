def count_word_occurrences(text):
    words = text.split()  
    word_count = {}

    for word in words:
        word = word.lower().strip('.,!?')  
        word_count[word] = word_count.get(word, 0) + 1  

    return word_count


text = "Hello world! Hello Python. Welcome to the world of Python."
word_occurrences = count_word_occurrences(text)

for word, count in word_occurrences.items():
    print(f"{word}: {count}")