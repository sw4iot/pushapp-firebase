import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask
from flask import request

app = Flask(__name__)

# TODO: montar credentials usando volume
cred = credentials.Certificate('./pushapp_firebase/config/serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def _send_firebase(data):
    doc_ref = db.collection(u'app_test').document(u'user')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })

    # result = requests.put(config.FIREBASE_HOST, data=json.dumps(data))


@app.route('/update', methods=['POST'])
def post_update():
    args = request
    # data = {
    #     'nivelMetal': args['nivelMetal'],
    #     'nivelPapel': args['nivelPapel'],
    #     'nivelPlastico': args['nivelPlastico'],
    #     'nivelVidro': args['nivelVidro']
    # }

    print(args)
    # _send_firebase(data=args)
    return "OK", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
