from flask import Flask, render_template, request
import mpmath
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_pi')
def calculate_pi():
    start_time = time.time()
    
    precision = int(request.args.get('precision', 100))
    mpmath.mp.dps = precision
    pi_value = str(mpmath.mp.pi)
    
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    
    return render_template('result.html', pi_value=pi_value, precision=precision, elapsed_time=elapsed_time)

if __name__ == '__main__':
    app.run(debug=True)