import requests
import json
from flask import request
from flask_restplus import Resource

from . import config

import logging
logger = logging.getLogger(__name__)

class PushAppFireBase(Resource):
    def _send_firebase(self, data):

        result = requests.put(config.FIREBASE_HOST, data=json.dumps(data))

        pass

    def post(self):
        args = request.args
        data = {
            'nivelMetal': args['nivelMetal'],
            'nivelPapel': args['nivelPapel'],
            'nivelPlastico': args['nivelPlastico'],
            'nivelVidro': args['nivelVidro']
        }

        self._send_firebase(data)




