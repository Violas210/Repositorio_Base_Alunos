from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.


@app.route('/soma')
def soma ():
    valor1 = request.args.get('valor1')
    valor2 = request.args.get('valor2')
    return f'{valor1} + {valor2} = {int(valor1)+int(valor2)}'

@app.route('/subtrair')
def subitrair ():
    valor1 = request.args.get('valor1')
    valor2 = request.args.get('valor2')
    return f'{valor1} - {valor2} = {int(valor1)-int(valor2)}'



@app.route('/multiplicar')
def multiplicar ():
    valor1 = request.args.get('valor1')
    valor2 = request.args.get('valor2')
    return f'{valor1} * {valor2} = {int(valor1)*int(valor2)}'

@app.route('/dividir')
def dividir ():
    
    valor1 = int(request.args.get('valor1'))
    valor2 = int(request.args.get('valor2'))
    if valor2 == 0:
        return {"erro": "Divisão por zero não é permitida"}
    
    else:
        return f'{valor1} / {valor2} = {(valor1)/(valor2)}'



if __name__ == "__main__":
    app.run(debug=True)