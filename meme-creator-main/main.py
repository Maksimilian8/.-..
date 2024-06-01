#Импорт
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# Результаты формы
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # получаем выбранное изображение
        selected_image = request.form.get('image-selector')

        # Получаем текст
        text_top = request.form.get('textTop')
        text_bottom = request.form.get('textBottom')

        # Получаем расположение текста
        text_top_y = request.form.get('textTop_y')
        text_bottom_y = request.form.get('textBottom_y')

        # Получаем цвет текста
        selected_color = request.form.get('color-selector')

        return render_template('index.html', 
                               selected_image=selected_image, 
                               text_top=text_top,
                               text_bottom=text_bottom,
                               text_top_y=text_top_y,
                               text_bottom_y=text_bottom_y,
                               selected_color=selected_color)
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index.html', 
                               selected_image='logo.svg',
                               text_top='',
                               text_bottom='',
                               text_top_y='0',
                               text_bottom_y='0',
                               selected_color='white')

@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

if __name__ == '__main__':
    app.run(debug=True)