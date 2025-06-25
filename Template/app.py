from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Function to generate password
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None  # Return None if no character types selected

    return ''.join(random.choice(characters) for _ in range(length))

# Route for password bot
@app.route('/', methods=['GET', 'POST'])
def password_bot():
    password = None
    error = None

    if request.method == 'POST':
        try:
            # Get form data
            length = int(request.form.get('length', 0))
            use_letters = 'letters' in request.form
            use_numbers = 'numbers' in request.form
            use_symbols = 'symbols' in request.form

            if length <= 0:
                raise ValueError("Length must be a positive number.")

            password = generate_password(length, use_letters, use_numbers, use_symbols)
            if password is None:
                error = "❌ Please select at least one character type."
                password = None

        except ValueError as e:
            error = f"❌ {str(e)}"

    return render_template('index.html', password=password, error=error)

# Run app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
