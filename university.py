import hashlib
import json
from flask import Flask, jsonify
import psycopg2
import pandas as pd

# Класс для блокчейна
class Blockchain:
    #Пустой список для хранения блокчейна а также создание блока и установки его хеша на 0
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, hashed_data='0')

    def create_block(self, proof, hashed_data):
        block = {
            'index': len(self.chain) + 1,
            'id': str(database.iloc[len(self.chain), 0]),
            'student_name': str(database.iloc[len(self.chain), 1]),
            'second_name': str(database.iloc[len(self.chain), 2]),
            'patronymic': str(database.iloc[len(self.chain), 3]),
            'university': str(database.iloc[len(self.chain), 4]),
            'study_profile': str(database.iloc[len(self.chain), 5]),
            'average_score': str(database.iloc[len(self.chain), 6]),
            'tracking_hash': hashed_data,
            'proof': proof,
        }
        self.chain.append(block)
        return block

    def print_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['tracking_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
        return True

# Функция для подключения к базе данных
def connect_db():
    conn = psycopg2.connect(dbname='New', user='postgres', password='123', host='localhost')
    cursor = conn.cursor()
    data = 'SELECT * FROM public.Students'
    cursor.execute(data)
    df = cursor.fetchall()
    df = pd.DataFrame(df, columns=['id', 'student_name', 'second_name ', 'patronymic', 'university', 'study_profile', 'average_score'])
    return df

# Получаем данные из базы данных
database = connect_db()

# Веб-приложение на Flask
app = Flask(__name__)

# Создаем объект класса blockchain
blockchain = Blockchain()

# Страница с подсказками
@app.route('/')
def index():
    return "Майнинг нового блока: /mine_block  " \
           "Отобразить блокчейн в формате json: /display_chain  " \
           "Проверка валидности блокчейна: /valid  "

# Майнинг нового блока
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.print_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'A block is MINED',
                'index': block['index'],
                'id': block['id'],
                'student_name': block['student_name'],
                'second_name ': block['second_name'],
                'patronymic': block['patronymic'],
                'university': block['university'],
                'study_profile': block['study_profile'],
                'average_score': block['average_score'],
                'proof': block['proof'],
                'tracking_hash': block['tracking_hash']}
    return jsonify(response), 200

# Отобразить блокчейн в формате json
@app.route('/display_chain', methods=['GET'])
def display_chain():
    chain = []
    for block in blockchain.chain:
        data = {
            'message': 'A block is MINED',
                'index': block['index'],
                'id': block['id'],
                'student_name': block['student_name'],
                'second_name ': block['second_name'],
                'patronymic': block['patronymic'],
                'university': block['university'],
                'study_profile ': block['study_profile'],
                'average_score': block['average_score'],
                'proof': block['proof'],
                'tracking_hash': block['tracking_hash']
        }
        chain.append(data)
    response = {'chain': chain, 'length': len(chain)}
    return jsonify(response), 200

# Проверка валидности блокчейна
@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)
    if valid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200

# Запуск сервера flask локально
if __name__ == '__main__':
    app.run(debug=True)