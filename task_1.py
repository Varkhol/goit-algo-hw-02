from queue import Queue

queue = Queue()

def generate_request(description):
    generate_request.counter += 1
    number = generate_request.counter
    queue.put({"number": number, "description": description})
    print(f"Заявку за номером {number} додано до черги.")

generate_request.counter = 0

def process_request(action='take'):
    if not queue.empty():
        request = queue.get()
        if action == 'take':
            print(f"Заявку за номером {request['number']} виконано: {request['description']}")
        else:
            print(f"Заявку за номером {request['number']} видалено.")
    else:
        print("Черга із заявками порожня.")

def show_queue():
    if queue.empty():
        print("Черга із заявками порожня.")
    else:
        print(f"Заявок у черзі: {queue.qsize()}")
        for item in list(queue.queue):
            print(f"  #{item['number']} — {item['description']}")

print("Головне меню сервісного центру.\n")
print("  'take'   — виконати заявку")
print("  'delete' — видалити заявку")
print("  'list'   — переглянути чергу")
print("  'exit'   — вийти")
print("  або введіть текст заявки\n")

while True:
    command = input("Команда або текст заявки: ")

    if command.lower() == 'exit':
        break
    elif command.lower() == 'take':
        process_request('take')
    elif command.lower() == 'delete':
        process_request('delete')
    elif command.lower() == 'list':
        show_queue()
    elif command.strip() == '':
        print("Заявка не може бути порожньою.")
    else:
        generate_request(command)

print("Роботу завершено.")