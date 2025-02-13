from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

# Храним выданные билеты, чтобы избежать дубликатов
issued_tickets = set()

def generate_ticket():
    """Генерирует уникальный четырехзначный буквенный билет."""
    while True:
        ticket = ''.join(random.choices(string.ascii_uppercase, k=4))  # Генерация 4 случайных заглавных букв
        if ticket not in issued_tickets:  # Проверяем, что билет уникальный
            issued_tickets.add(ticket)  # Добавляем билет в список выданных
            return ticket

@app.route('/generate_ticket', methods=['GET'])
def create_ticket():
    """Создаёт новый билет и возвращает его клиенту."""
    new_ticket = generate_ticket()
    return jsonify({'ticket': new_ticket})

if __name__ == '__main__':
    app.run(debug=True)
