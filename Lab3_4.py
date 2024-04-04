def process_sentence(sentence):
    print("Длина предложения:", len(sentence))

    lowercase_sentence = sentence.lower()
    print("Предложение в нижнем регистре:", lowercase_sentence)

    vowels = 'aeiou'
    vowel_count = sum(1 for char in lowercase_sentence if char in vowels)
    print("Количество гласных:", vowel_count)

    replaced_sentence = lowercase_sentence.replace("ugly", "beauty")
    print("Предложение с заменой:", replaced_sentence)

    starts_with_the = lowercase_sentence.startswith("the")
    ends_with_end = lowercase_sentence.endswith("end.")
    print("Начинается с 'The':", starts_with_the)
    print("Заканчивается на 'end':", ends_with_end)


sentences = input("Введите предложение: ").split(',')

for sentence in sentences:
    print("Исходное предложение:", sentence)
    process_sentence(sentence)