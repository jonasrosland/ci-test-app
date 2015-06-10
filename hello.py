import flask
import redis
import os
import urlparse
import json


app = Flask(__name__)
rediscloud_service = json.loads(os.environ['VCAP_SERVICES'])['rediscloud'][0]
credentials = rediscloud_service['credentials']
r = redis.Redis(host=credentials['hostname'], port=credentials['port'], password=credentials['password'])

@app.route('/')
def hello():
   r.incr('hits')
#   return 'Hello World!'
   return 'Hello World! I have been seen %s times.\n' % r.get('hits')


port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
