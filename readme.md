# Desafio: Tradutor de Código Morse

## Índice

1. [Descrição](https://github.com/VicMCA/python_morse_translator#1-descri%C3%A7%C3%A3o)
2. [Configuração](https://github.com/VicMCA/python_morse_translator#2-configura%C3%A7%C3%A3o)
3. [Requisitos](https://github.com/VicMCA/python_morse_translator#3-requisitos)
4. [Progresso Atual](https://github.com/VicMCA/python_morse_translator#4-progresso-atual)
5. [Briefing do Projeto](https://github.com/VicMCA/python_morse_translator#5-briefing-do-projeto)
6. [Tabela de Referência para Código Morse](https://github.com/VicMCA/python_morse_translator#6-tabela-de-refer%C3%AAncia-para-c%C3%B3digo-morse)

## 1. Descrição 

Este é um tradutor de código morse para alfabeto. Reconhece todas as 26 letras do alfabeto mais os algarismos de '0' à '9'. Os inputs reconhecidos são:  

<pre>
`.`  para 'dots'  
`-`  para 'dashes'  
`/`  para delimitação de caracteres  
`//` para espaço entre palavras  
</pre>

Acentuações, pontuações e caracteres especiais não são reconhecidos. Todos os caracteres serão retornados como maiúscula quando aplicável.  
Passo a passo de instalação e configuração:
## 2. Configuração  

Pacotes utilizados:  

1. Python 3.8
2. Python 3.8 Virtual Environment (venv)
3. Pip
4. Flask

Passo a passo de instalação e configuração:

1. Clonar este repositório `git clone https://github.com/VicMCA/python_morse_translator.git`  
2. Dentro da pasta raíz, crie recrie o ambiente virtual `python3 -m venv venv`  
3. Ativar o ambiente virtual `. venv/bin/activate` (Linux e MacOS) `venv\Scripts\activate` (Windows)  
4. Instalar o Flask no ambiente virtual `pip3 install flask`  
5. Rodar a aplicação com `python3 app.py`  
6. O frontend ficará acessível em `http://localhost:5000`  

## 3. Requisitos

O App deve:  
<br/>
1. Possuir um campo para inserção de código morse
2. Enviar o código para o servidor
3. Retornar o código traduzido para os caracteres ASCII disponíveis
4. Impedir a inserção de caracteres inválidos
5. Retornar um erro caso o código informado possua:  
&nbsp;&nbsp; - Caracteres inválidos  
&nbsp;&nbsp; - Combinações de caracteres não reconhecidas  
6. Permitir a limpeza dos campos de código e do resultado
7. Possuir uma tabela de referência para a digitação do código morse

## 4. Progresso Atual 

Lista de requisitos:  

- [x] HTML contendo todas as informações para o usuário
- [x] Formulário de input com campos de envio e reset
- [x] Campo para exibição do resultado com opção de limpeza do mesmo
- [x] Tratamento de erros para inputs inválidos no backend
- [x] Tratamento de erros para inputs inválidos no frontend
- [x] Tornar o programa acessível através de uma API
- [x] Conectar a API à um frontend básico
- [x] Modularizar o código (scripts de tradução separados das rotas do servidor)
- [x] Criação de endpoints reservados para o envio dos códigos a traduzir
- [ ] CSS
- [x] Tabela de letras, números e códigos correspondentes
- [ ] Testes de carga
- [ ] Página de "sobre" do projeto
- [ ] Link para repositório no GitHub

## 5. Briefing do Projeto 
## Definição do desafio:
Precisamos que você crie um repositório no github ou gitlab e depois inicie um projeto que tenha o objetivo de criar uma tradução de código morse. A ideia é uma solução baseada em socket que recebe um código morse e converte ele em texto. Imagine que o cliente vai enviar "." e "-" e o servidor vai receber estas informações e interpretar o que aquele código morse representa. 

Não é necessário você se preocupar com gramática, concordância, frases complexas, este não é o objetivo do desafio. 

O objetivo do desafio é você definir uma arquitetura que resolva a solução utilizando o código morse como protocolo de comunicação e pensando em como esta solução poderia ser criada de forma que fosse o mais escalável possível.

Reflita sobre a arquitetura que você gostaria de usar, que serviços teria e como eles iriam se comunicar. Se você achar interessante usar RabbitMQ, Celery, Redis ou qualquer outra tecnologia similar, sinta-se à vontade para fazer. Se você preferir usar só Python com Django ou Flask, também é possível. Você é livre para criar a arquitetura que você achar mais interessante.

É importante para a gente você descrever o que motivou suas decisões e caso você tivesse mais tempo como seria a evolução desta arquitetura/produto.
<br/><br/>

## 6. Tabela de Referência para Código Morse 
### Morse Code heat sheet:

```
A = .-      B = -...    C = -.-.    D = -..     E = .       F = ..-.
G = --.     H = ....    I = ..      J = .---    K = -.-     L = .-..
M = --      N = -.      O = ---     P = .--.    Q = --.-    R = .-.
S = ...     T = -       U = ..-     V = ...-    W = .--     X = -..-
Y = -.--    Z = --..

0 = -----   1 = .----   2 = ..---   3 = ...--   4 = ....-   5 = .....
6 = -....   7 = --...   8 = ---..   9 = ----.
```

### Exemplo
MORSE CODE = `--/---/.-./..././/-.-./---/-../.`