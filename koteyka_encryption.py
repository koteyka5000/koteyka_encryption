# from elevate import elevate
# elevate()
# import subprocess
# result = subprocess.run(['netsh', '-ano', '|', 'findstr', ':10000'], stdout=subprocess.PIPE, shell=True)
# print(result.stdout.decode('utf-8'))

from random import randint
alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", 
                "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " ","а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", 
                "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]


def encrypt(txt):
    encrypted = ''
    move_keys = []

    for letter in txt:
        move = randint(0, 33) # На сколько сдвигаем
        index = alphabet.index(letter) # Индекс буквы
        move_keys.append(move) # Добавляем "на сколько сдвигаем" в словарь
        new_index = index + move # Индекс в алфавите для зашифрованой буквы
        encrypted += alphabet[new_index] # Добавляем букву с этим индексом в строку

    move_keys_letters = ''                 # \
    for key in move_keys:                  #  | Записываем каждую цифру как букву с этим индексом, чтобы получить букву из числа
        move_keys_letters += alphabet[key] # / 

    print(f'encrypted = {encrypted}')
    print(f'move_keys_letters = {move_keys_letters}')

    new_encrypted = ''  
    for letter in encrypted:                       # \
        new_encrypted += letter                    #  | Добавляем через каждую букву случайную букву, чтобы усложнить иотговую комбинацию
        new_encrypted += alphabet[randint(0, 33)]  # /

    encrypted_ready_send = new_encrypted + move_keys_letters # Итогая строка это соединение шифра и ключа к нему
    return encrypted_ready_send 

def decrypt(encrypted):
    print('==================')
    encrypted_ready = encrypted
    enc_len = len(encrypted_ready) # Длинна шифра будет 2\3, а ключ 1\3, тк мы добавляли через каждую букву случайную букву, получается
    enc_len = enc_len // 3         # что длинна шифра будет в 2 раза больше, чем ключ к шифру           (Тут получаем 1\3 длинны строки)
    encrypted = encrypted_ready[:enc_len + enc_len][::2]  # Срезаем первые две части, получая зашифрованый текст без ключа, потом убираем
                                                          # каждую вторую букву, чтобы получить исходный шифр
    move_keys_letters = encrypted_ready[enc_len:]    # срезаем 2\3 c конца (я хз как по другому) 
    move_keys_letters = move_keys_letters[enc_len:]  # срезаем еще половину (1\2), получая 1\3, где и находится ключ
    print(f'{encrypted}    :    {move_keys_letters}')

    decrypted = ''
    counter = 0
    for letter in encrypted:
        move = move_keys_letters[counter] # Символ в ключе как буква
        move = alphabet.index(move)       # Переделываем в цифру, под которой эта буква в алфавите

        index_enc = alphabet.index(letter) # Индекс в алфавите зашифрованой буквы
        new_index = index_enc - move       # Вычитаем прошлый сдвиг, чтобы получить индекс исходной буквы
        decrypted += alphabet[new_index]   # Ищем букву с этим индексом и добавляем её в итоговый вывод
        counter += 1
    return decrypted

txt = "кот е й   ка"
encrypted = encrypt(txt)
print(f'Зашифрованное сообщение: {encrypted}')

decrypted = decrypt(encrypted)
print(f'Расшифрованное сообщение: {decrypted}')