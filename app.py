from flask import Flask, render_template, request, url_for, redirect
from traduz_morse_texto import morse_to_text
from traduz_texto_morse import text_to_morse

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=["POST", "GET"])
def index():
  return render_template('index.html')


@app.route("/send_morse", methods=["POST"])
def send_morse():
  resultado = None
  codigo = request.form['codigo']
  if codigo != '':
    try:
      print(codigo)
      resultado = morse_to_text(codigo + '/')
      return render_template('index.html', resultado=resultado)
    except:
      resultado = 'Erro ao traduzir. A sequência de símbolos não corresponde a nenhum caractere válido.'
      return render_template('index.html', resultado=resultado)


@app.route("/send_text", methods=["POST"])
def send_text():
  resultado = None
  codigo = request.form['codigo']
  if codigo != '':
    try:
      print(codigo)
      resultado = morse_to_text(codigo)
      return render_template('index.html', resultado=resultado)
    except:
      resultado = 'Erro ao traduzir. A sequência de símbolos não corresponde a nenhum caractere válido.'
      return render_template('index.html', resultado=resultado)


if __name__ == '__main__':
  app.run(debug=True, port=5000)