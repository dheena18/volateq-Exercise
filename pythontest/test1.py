from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

@app.route('/clock')
def dateandtime():
    lang = request.args.get('lang', 'en')
    dateorder = request.args.get('dateorder', '%Y/%m/%d %H:%M')
    time = request.args.get('time', 'datetime')
    date = request.args.get('date', 'datetime')
    current = datetime.utcnow()

    if lang == 'en':
        datetimechanged = current.strftime(dateorder)

    if date == 'date':
        datetimechanged = datetimechanged.split(' ')[0]
    elif time == 'time':
        datetimechanged = datetimechanged.split(' ')[1]

    return datetimechanged

if __name__ == '__main__':
    app.run(debug=True)