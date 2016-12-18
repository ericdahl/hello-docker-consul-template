import flask
import os
import redis

app = flask.Flask(__name__)
@app.route('/')
def hello_world():

    redis_handle = redis.StrictRedis(host='redis', port=6379, db=0)
    c = redis_handle.incr('counter')

    r = 'hello from {} (count is {})\n'.format(os.environ['HOSTNAME'], str(c))
    resp = flask.make_response(r)
    resp.headers['Cache-Control'] = 'public, max-age=5'
    return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
