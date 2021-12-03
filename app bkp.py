from flask import Flask, render_template, request, url_for, redirect
from traduz_morse_texto import morse_to_text
from traduz_texto_morse import text_to_morse

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


"""Tabelas de tradução"""
tabela_morse_to_char = {
  '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', 
  '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
  '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
  '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
  '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', 
  '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', 
  '...--': '3', '....-': '4', '.....': '5', '-....': '6', 
  '--...': '7', '---..': '8', '----.': '9', 'c': '', 'space': ' ',
}

tabela_char_to_morse = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
  'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
  'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
  'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
  '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
  '7': '--...', '8': '---..', '9': '----.', 'c': '', 'space': ' ',
}


@app.route("/", methods=["POST", "GET"])
def index():
  resultado = None
  if request.method == "POST":
    codigo = request.form['codigo']
    if codigo != '':
      try:
        print(codigo)
        resultado = morse_to_text(codigo + '/')
        return render_template('index.html', resultado=resultado)
      except:
        resultado = 'Erro ao traduzir. A sequência de símbolos não corresponde a nenhum caractere válido.'
        return render_template('index.html', resultado=resultado)
  else:
    return render_template('index.html', resultado=resultado)
  

def morse_to_text(codigo):
  '''
  Realiza a tradução do input recebido, de código-morse para ASCII em maiúsculas.
  Pontuação e acentos não inclusos.
  '''
  caracteres_aceitos = ['.', '-', '/']
  caractere = ''
  lista_caracteres = []
  caractere_anterior = ''

  for char in codigo:
    if char not in caracteres_aceitos:
      return "O código enviado possui caracteres não-aceitos."
  else:
    for x in codigo:
      if x == '.' or x == '-':
        caractere += x
      elif x == '/':
        if caractere != '':
          lista_caracteres.append(tabela_morse_to_char[f'{caractere}'])
        if caractere_anterior == '/':
          lista_caracteres.append(' ')
        else:
          pass
        caractere = ''
      caractere_anterior = x
    
    return ''.join(lista_caracteres)


if __name__ == '__main__':
  app.run(debug=True, port=5000)