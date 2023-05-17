import random


def main():
    word_list = ['повітря', 'швидкість', 'вікно', 'спроба', 'книга', 'шухлядка']
    chosen_word = random.choice(word_list)
    encrypted_word = '*'*len(chosen_word)
    quantity_selected = False
    number_of_attempts = 0
    while not quantity_selected:
        number_of_attempts = input('Скільки буде спроб?: ')
        if number_of_attempts.isdecimal() and int(number_of_attempts) > 0:
            quantity_selected = True
            number_of_attempts = int(number_of_attempts)
        else:
            print('Треба вказати ціле число більше 0')
    while number_of_attempts:
        attempt = input('Вкажи букву чи слово: ').lower()
        if len(attempt) == 1:
            letter_count = chosen_word.count(attempt)
            if letter_count:
                new_encrypted_word = ''
                for i in range(0, len(chosen_word)):
                    new_encrypted_word += chosen_word[i] if chosen_word[i] == attempt else encrypted_word[i]
                encrypted_word = new_encrypted_word
                print('Вгадав!')
                if encrypted_word == chosen_word:
                    print('Ви відгадали слово!')
                    print(encrypted_word)
                    return
            else:
                print('Не вгадав!')
        else:
            if chosen_word == attempt:
                print('Ви відгадали слово!')
                return
            else:
                print('Не вгадав!')

        print(encrypted_word)
        number_of_attempts -= 1
    print('Кількість спроб закінчилися!')

if __name__ == '__main__':
    main()


