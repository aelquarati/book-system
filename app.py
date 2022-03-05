from flask  import Flask, request
from flask_restful import Resource, Api
from recommender.recom import Recom

app = Flask(__name__)

#CORS(app)

api  = Api(app)

@app.route("/health")
def health():
    return '{"response":"ok"}'

class Input_data(Resource):

    def post (self):
        content = request.get_json(silent=True)
        recom = Recom(content['book_name'])
        output = recom.KNN_model()
        return(output) 

api.add_resource(Input_data,"/call")


if __name__ == '__main__':
    app.run()