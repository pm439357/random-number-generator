from flask import Flask, render_template_string
import random

app = Flask(__name__)

# HTML-шаблон для генератора случайных чисел
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Random Number Generator</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        h1 { color: #333; }
        button { padding: 10px 20px; font-size: 16px; }
    </style>
</head>
<body>
    <h1></h1>
    <p id="number"></p>
    <button onclick="generateNumber()">Generate</button>
    <script>
        function generateNumber() {
            fetch('/random')
                .then(response => response.text())
                .then(data => {
                    document.getElementById('number').innerText = "Random Number: " + data;
                });
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

@app.route("/random")
def random_number():
    return str(random.randint(1, 100))
