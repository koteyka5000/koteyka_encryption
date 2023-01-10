from koteyka_encryption import encrypt, decrypt
from colorama import init, Fore
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
init(autoreset=True)
# print(f'{Fore.CYAN}Init')
text_to_encrypt = 'а'
times_err = 0
TIMES_CHECK = 100_000

output = {}

alphabet = "ю", "в", "з", "й", "м", "с", "т", "у", "ь", "ж", "л", "э", "ф", "б", "х", "г", "я", " ", "и", "к", "ъ", "ы", "ё", "о", "ц", "ч", "ш", "щ", "р", "н", "а", "п", "д", "е"

# print(f'{Fore.GREEN}Run')
# for letter in alphabet:
#     print('>', Fore.YELLOW + letter)
#     for i in range(TIMES_CHECK):
#         if not decrypt(encrypt(letter)) == letter:
#             times_err += 1
#     output[letter] = times_err / TIMES_CHECK

# p = 0
# for key, value in output.items():
#     if p == 3:
#         print(f"          {Fore.BLUE}{key} -> {Fore.YELLOW}{value*100:.{1}f}%")
#         p = False
#     else:
#         print(f"          {Fore.BLUE}{key} -> {Fore.YELLOW}{value*100:.{1}f}%", end='')
#         p += 1

class Loader:
    def __init__(self, desc="Загрузка...", end="Готово!", timeout=0.07):
        """
        Анимация загрузки в строке

        Аргументы:
            desc (str, optional): Описание загрузки ( Что делаем ? )
            end (str, optional): Вывод по окончании загрузки
            timeout (float, optional): Ожидание между обновлением анимации
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}    ", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        self.stop()

q = []
with Loader(end=''):
    for i in range(2000000):
        q.append(encrypt('аа'))
print(len(q))
print(len(set(q)))