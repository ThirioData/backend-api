from flask_restful import Resource, reqparse
from models.user import UserModel
import pandas as pd
import boto3
import csv

# s3 = boto3.client(
#     's3',
#     aws_access_key_id="AKIAJ4TFZGA2OEV7J37A",
#     aws_secret_access_key="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"
# )

# Let's use Amazon S3
# s3 = boto3.resource('s3')
# bucket_name = "thirio-csv"
# csv_file_name = "user_features.csv"

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="Username is required"
                        )
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="Password is also required"
                        )
    parser.add_argument("email",
                        type=str,
                        required=True,
                        help="Email is also required"
                        )
    parser.add_argument("firstname",
                        type=str
                        )
    parser.add_argument("lastname",
                        type=str
                        )
    parser.add_argument("age",
                        type=int
                        )
    parser.add_argument("sex",
                        type=int
                        )
    parser.add_argument("location",
                        type=int
                        )
    parser.add_argument("non_veg",
                        type=int
                        )
    parser.add_argument("mobileno",
                        type=str    
                        )
    # parser.add_argument("calories",
    #                     type=int
    #                     )
    # parser.add_argument("meal_size_rating",
    #                     type=int
    #                     ),
    # parser.add_argument("previous_meal_size",
    #                     type=int
    #                     ),
    parser.add_argument("user_guid",
                        type=int
                        )

    def read_csv():
        data = UserRegister.parser.parse_args()
        fields = [data['age'], 100, data['location'], data['non_veg'], data['sex'], 1, 1, data['user_guid']]


    def post(self):
        data = UserRegister.parser.parse_args()
        # data['calories'] = 100
        if UserModel.find_by_username(data['username']):
            return {
                "message": "A user already exists with this username %s".format(data['username']) 
            }, 400

        user = UserModel(**data)
        # save to user_features
        fields = [data['age'], 100, data['location'], data['non_veg'], data['sex'], 1, 1, data['user_guid']]
        with open('../user_features.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

        # open connection to s3
        # fileobj = s3.Object(bucket_name, csv_file_name).get(['Body'])
        # for x in range(5):
        #     yield fileobj.read(1)
        # obj = s3.get_object(Bucket=bucket_name, Key=csv_file_name)
        # initial_df = pd.read_csv(obj['Body']) # 'Body' is a key word
        user.save_to_db()
        # print(initi)
        return {
            "message": "successfully signed up"
        }, 201
