from koteyka_encryption import encrypt, decrypt
from colorama import init, Fore
init(autoreset=True)
print(f'{Fore.CYAN}Init')
text_to_encrypt = 'а'
times_err = 0
TIMES_CHECK = 400_000

output = {}

alphabet = "ю", "в", "з", "й", "м", "с", "т", "у", "ь", "ж", "л", "э", "ф", "б", "х", "г", "я", " ", "и", "к", "ъ", "ы", "ё", "о", "ц", "ч", "ш", "щ", "р", "н", "а", "п", "д", "е"

print(f'{Fore.GREEN}Run')
for letter in alphabet:
    print('>', Fore.YELLOW + letter)
    for i in range(TIMES_CHECK):
        if not decrypt(encrypt('о')) == 'о':
            times_err += 1
    output[letter] = times_err / TIMES_CHECK

p = 0
for key, value in output.items():
    if p == 3:
        print(f"          {Fore.BLUE}{key} -> {Fore.YELLOW}{value*100:.{1}f}%")
        p = False
    else:
        print(f"          {Fore.BLUE}{key} -> {Fore.YELLOW}{value*100:.{1}f}%", end='')
        p += 1