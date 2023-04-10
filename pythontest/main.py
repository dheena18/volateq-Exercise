from datetime import datetime, timezone
from enum import Enum
import locale

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class FormatType(str, Enum):
    iso = "iso"
    rfc = "rfc"
    short = "short"
    long = "long"


class DateTime(Resource):
    def get(self, format_type: FormatType = FormatType.iso.value,language: str = "en_US",format_string: str = None):
        dt = datetime.now(timezone.utc)
        if language is not None:
            try:
                locale.setlocale(locale.LC_TIME, language)
            except locale.Error:
                pass

        if format_type == FormatType.iso.value:
            formatted_dt = dt.isoformat()
        elif format_type == FormatType.rfc.value:
            formatted_dt = dt.strftime("%a, %d %b %Y %H:%M:%S GMT")
        elif format_type == FormatType.short.value:
            formatted_dt = dt.strftime("%x")
        elif format_type == FormatType.long.value:
            formatted_dt = dt.strftime("%c")
        else:
            return {"message": "Invalid format type"}, 400

        return {"datetime": formatted_dt}

        if format_string is not None:
            formatted_dt = dt.strftime(format_string)


api.add_resource(DateTime, "/datetime", "/datetime/<string:format_type>", "/datetime/<string:format_type>/<string:language>", "/datetime/<string:format_type>/<string:language>/<string:format_string>") #, "/datetime/<string:format_type>" <string:format_type>/

if __name__ == "__main__":
    app.run(debug=True)
