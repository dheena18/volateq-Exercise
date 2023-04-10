from datetime import datetime, timezone
from enum import Enum

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
    def get(self, format_type: FormatType = FormatType.iso.value):
        dt = datetime.now(timezone.utc)

        if format_type == FormatType.iso.value:
            formatted_dt = dt.isoformat()
        elif format_type == FormatType.rfc.value:
            formatted_dt = dt.strftime("%a, %d %b %Y %H:%M:%S GMT")
        elif format_type == FormatType.short.value:
            formatted_dt = dt.strftime("%m/%d/%Y")
        elif format_type == FormatType.long.value:
            formatted_dt = dt.strftime("%B %d, %Y %H:%M:%S UTC")
        else:
            return {"message": "Invalid format type"}, 400

        return {"datetime": formatted_dt}


api.add_resource(DateTime, "/datetime", "/datetime/<string:format_type>")

if __name__ == "__main__":
    app.run(debug=True)
