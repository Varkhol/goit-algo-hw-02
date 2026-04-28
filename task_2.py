from collections import deque

def is_palindrome(string):
    normalized = string.replace(" ", "").lower()

    queue = deque(normalized)

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False

    return True


while True:
    text = input("Введіть текст для перевірки або 'exit' для виходу: ")

    if text.lower() == 'exit':
        break

    if is_palindrome(text):
        print(f"'{text}' — це паліндром\n")
    else:
        print(f"'{text}' — це не є паліндромом.\n")