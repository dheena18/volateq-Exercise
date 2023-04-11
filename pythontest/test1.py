from datetime import datetime
from flask import Flask, request , abort
from babel.dates import format_datetime
from urllib.parse import unquote, quote
from pytz import timezone

app = Flask(__name__)

@app.route('/clock')
def date_and_time():
    lang = request.args.get('lang', 'en')
    date_order = request.args.get('dateorder', 'Y/m/d H:M')
    date_order = unquote(date_order)
    encoded_date_order = quote(date_order)
    current = datetime.utcnow()
    timezone_name = request.args.get('timezone', 'UTC')
    timezone_obj = timezone(timezone_name)
    current_time = datetime.now(timezone_obj)

    if 'time' in request.args:
        time_format = request.args.get('time')
        try:
            datetime_changed = format_datetime(current_time, format=time_format, locale=lang)
        except ValueError:
            return abort(400, f'Invalid time format "{time_format}"')
    else:
        datetime_changed = format_datetime(current, format='dd MMMM y', locale=lang)

    return datetime_changed

if __name__ == '__main__':
    app.run(debug=True)


    #http://localhost:5000/clock?lang=fr
# 10 avr. 2023
#
# http://localhost:5000/clock?lang=es&time=%H:%M:%S
# 12:08:27
#
# http://localhost:5000/clock?lang=ja&time=%Y年%m月%d日%a%H時%M分%S秒&timezone=Asia/Tokyo
# 2023年04月11日月曜日10時19分32秒
# /clock?lang=en - returns the date and time in English (default)
# /clock?lang=fr - returns the date and time in French
# /clock?lang=es - returns the date and time in Spanish
# /clock?lang=de - returns the date and time in German
# /clock?lang=it - returns the date and time in Italian
# /clock?lang=pt_BR - returns the date and time in Brazilian Portuguese
# /clock?lang=ru - returns the date and time in Russian
# /clock?lang=ja - returns the date and time in Japanese
# /clock?lang=zh_Hans - returns the date and time in simplified Chinese
# /clock?lang=ar - returns the date and time in Arabic