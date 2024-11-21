import random

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from  autoprovision import AutoProvision

import const
from log import Logger

logger = Logger.getLogger('server_requests', 'logs/server_requests')

app = Flask(__name__)
api = Api(app)

def random_ref(length):
    sample_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  # define the specific string
    # define the condition for random string
    return ''.join((random.choice(sample_string)) for x in range(length))



class Autoprovition(Resource):
    def post(self):
        ref = random_ref(15)
        data = request.get_json()
        logger.info(ref + " - " + str(request.remote_addr) + " - " + str(request.url) + " - " + str(request.headers))
        logger.info(ref + " - " + str(data))
        return  AutoProvision.autoProvCreate(data,ref)

class AutoprovitionDelete(Resource):
    def post(self):
        ref = random_ref(15)
        data = request.get_json()
        logger.info(ref + " - " + str(request.remote_addr) + " - " + str(request.url) + " - " + str(request.headers))
        logger.info(ref + " - " + str(data))
        return  AutoProvision.autoProvDelete(data,ref)



api.add_resource(Autoprovition, const.APP_ROUTE_CREATE)
api.add_resource(AutoprovitionDelete, const.APP_ROUTE_DELETE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=34485)