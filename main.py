import random


def update_letters(chosen_word, encrypted_word, attempt):
    new_encrypted_word = ''
    for i in range(len(chosen_word)):
        new_encrypted_word += chosen_word[i] if chosen_word[i] == attempt else encrypted_word[i]
    return new_encrypted_word


def main():
    word_list = ['повітря', 'швидкість', 'вікно', 'спроба', 'книга', 'шухлядка']
    chosen_word = random.choice(word_list)
    encrypted_word = '*'*len(chosen_word)
    number_of_attempts = 0
    while True:
        number_of_attempts = input('Скільки буде спроб?: ')
        if number_of_attempts.isdecimal() and int(number_of_attempts) > 0:
            number_of_attempts = int(number_of_attempts)
            break
        else:
            print('Треба вказати ціле число більше 0')
    while number_of_attempts > 0:
        attempt = input('Вкажи букву чи слово: ').lower()
        if len(attempt) == 1:
            letter_count = chosen_word.count(attempt)
            if letter_count:
                encrypted_word = update_letters(chosen_word, encrypted_word, attempt)
                print('Вгадав!')
                if encrypted_word == chosen_word:
                    print('Ви відгадали слово!')
                    print(encrypted_word)
                    return
            else:
                print('Не вгадав!')
                number_of_attempts -= 1
        else:
            if chosen_word == attempt:
                print('Ви відгадали слово!')
                return
            else:
                print('Не вгадав!')
                number_of_attempts -= 1
        print(encrypted_word)
    print('Кількість спроб закінчилися!')


if __name__ == '__main__':
    main()
