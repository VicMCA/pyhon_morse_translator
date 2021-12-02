from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
  message = '-./---//--/./.../.../.-/--././'
  if request.method == "POST":
    pass

  print(morse(message))

  return "<p>Hello World!<br/>Hot-reload on!</p>"


def morse(codigo):
  '''
  Contém o dicionário e realiza a tradução do input 
  recebido, de código-morse para ASCII em maiúsculas.
  
  Pontuação e acentos não inclusos.
  '''
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

  caractere = ''
  lista_caracteres = []
  caracteres_traduzidos = ''
  caractere_anterior = ''
  
  for x in codigo:
    if x == '.' or x == '-':
      caractere += x
    elif x == '/':
      if caractere != '':
        lista_caracteres.append(tabela_morse_to_char[f'{caractere}'])
      if caractere_anterior == '/':
        lista_caracteres.append(' ')
      else:
        # lista_caracteres.append('')
        pass
      caractere = ''
    caractere_anterior = x

  return ''.join(lista_caracteres)


if __name__ == '__main__':
  app.run(debug=True)