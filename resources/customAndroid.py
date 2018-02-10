from flask_restful import Resource, reqparse
from models.customAndroid import CustomAndroidModel

class CustomAndroid(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("mobileno",
                        type=str,
                        required=True,
                        help="Enter phone no."
                        )
    parser.add_argument("steps",
                        type=str,
                        required=True,
                        help="Enter steps id"
                        )
    parser.add_argument("timestamp",
                        type=str,
                        required=True,
                        help="Enter timestamp in milisecond"
                        )

    def post(self, mobileno, steps):
        data = CustomAndroid.parser.parse_args()
        custom = CustomAndroidModel(data['mobileno'], data['steps'], data['timestamp'])
        try :
            custom.save_to_db()
        except:
            return {
                "message": "Error saving to database"
            }, 500
        return custom.json(), 201