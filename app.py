from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    if request.method == 'POST':
        action = request.form['action']
        message = request.form['message']
        shift = request.form.get('shift', 0, type=int)

        if not message:
            output = 'Please enter a message.'
        elif not 0 <= shift <= 25:
            output = 'Shift value must be between 0 and 25.'
        else:
            if action == 'Encrypt':
                output = caesar_encrypt(message, shift)
            elif action == 'Decrypt':
                output = caesar_decrypt(message, shift)

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)