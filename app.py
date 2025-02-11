import os
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def calculate_bazi(birth_date, birth_time, place):
    """
    Dummy function to calculate a Bazi chart.
    Replace this logic with your actual calculations.
    """
    # Dummy data for demonstration purposes:
    return {
        'year': {'stem': '甲', 'branch': '子'},
        'month': {'stem': '乙', 'branch': '丑'},
        'day': {'stem': '丙', 'branch': '寅'},
        'hour': {'stem': '丁', 'branch': '卯'}
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs from the form
        birth_date_str = request.form.get('birth_date')
        birth_time_str = request.form.get('birth_time')
        place = request.form.get('place')

        # Parse the birth date and time
        try:
            birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
        except (ValueError, TypeError):
            error_message = "Invalid birth date format. Use YYYY-MM-DD."
            return render_template('index.html', error=error_message)

        try:
            # The input type "time" provides HH:MM format
            birth_time = datetime.strptime(birth_time_str, '%H:%M').time()
        except (ValueError, TypeError):
            error_message = "Invalid birth time format. Use HH:MM."
            return render_template('index.html', error=error_message)

        # Calculate the Bazi chart (replace with real calculation logic)
        bazi_chart = calculate_bazi(birth_date, birth_time, place)

        # Render the results page with the calculated chart
        return render_template('result.html',
                               bazi=bazi_chart,
                               place=place,
                               birth_date=birth_date,
                               birth_time=birth_time)

    # GET request: display the form
    return render_template('index.html')

if __name__ == '__main__':
    # Bind to PORT environment variable if available (useful for Heroku)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
