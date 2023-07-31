from flask import Flask, render_template, request, jsonify, url_for, redirect
from PIL import Image
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import requests
import pytesseract
import io
import base58
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import *
from verify_crypto import *
import csv



app = Flask(__name__)
rpc_user = 'your_rpc_username'
rpc_password = 'your_rpc_password'
rpc_port = '8332'
app.config["SECRET_KEY"] = 'HEY'
bootstrap = Bootstrap(app)


@app.route('/')
def home():
    return render_template("index.html")


class PrivPub(FlaskForm):
    priv = StringField("Private key: ", validators = [validators.DataRequired()])
    pub = StringField("Public key: ", validators = [validators.DataRequired()])
    submit = SubmitField('submit')


class TXform(FlaskForm):
    txhash = StringField("Transaction hash: ", validators = [validators.DataRequired()])
    submit = SubmitField('submit')


@app.route('/PrivPub', methods=['GET', 'POST'])
def match():
    form = PrivPub()
    if form.validate_on_submit():
        priv = request.form['priv']
        pub = request.form['pub']
        crypto = detect_cryptocurrency(pub,priv)
        with open('cryptos.csv', 'a', newline='') as csv_file:
            csv_file.write(f"{priv},{pub},{crypto} \n")

        return redirect(url_for('crypto_solution'))
    return render_template("match.html", form = form)


@app.route("/solution", methods=['GET', 'POST'])
def crypto_solution():
    cryptos = open('cryptos.csv','r')
    crypt = cryptos.readlines()[-1].split(',')
    cryptos.close()
    return render_template("solution.html",priv = crypt[0],pub=crypt[1],crypto=crypt[2])


@app.route('/bitcoinTX', methods=['GET', 'POST'])
def txverify():
    tx_form = TXform()
    if tx_form.validate_on_submit():
        tx = request.form['txhash']
        with open(r'C:\Users\Ahmed\Desktop\indisafehackathon_part2\verify_transactions.csv', 'a', newline='') as csv_file:
            csv_file.write(f"{tx},{verify_tx(tx)} \n")
            return redirect(url_for('transaction_solution'))
    return render_template("txverify.html", tx_form = tx_form)


@app.route("/tx_solution", methods= ["GET","POST"])
def transaction_solution():
    txn = open(r'C:\Users\Ahmed\Desktop\indisafehackathon_part2\verify_transactions.csv', 'r')
    txns = txn.readlines()[-1].split(',')
    txn.close()
    return render_template("tx.html",tx = txns[0],tx_verified=txns[1])


@app.route('/requirement_2', methods=['GET','POST'])
def requirement_2():
    return render_template("requirement_2.html")



def ocr():
    # Get the uploaded image file from the POST request
    uploaded_file = request.files['file']
    image_data = uploaded_file.read()

    # Use the 'Image' module to open the image data
    image = Image.open(io.BytesIO(image_data))

    # Use Tesseract OCR to extract text from the image
    # The 'path' variable should be replaced with the path to your Tesseract executable
    path = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # Example path for Windows
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 6', executable=path)

    # Return the extracted text as a response
    return text


if __name__ == '__main__':
    app.run(debug = True)
