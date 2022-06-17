from flask import Flask, render_template, render_template_string


app = Flask(__name__)

p_title = {'index':'Главная страница'}



@app.route('/')
@app.route('/index')
def index():
    context = {}
    context['title'] = p_title[index.__name__]
    context['content'] = 'Содержимое страницы'
    context['menu'] = p_title
    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)