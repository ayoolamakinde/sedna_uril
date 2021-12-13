import sqlite3
import random
import os
import string
from hashids import Hashids
from flask import Flask, jsonify, request

app = Flask(__name__)
hash_length=6
app.config['SECRET_KEY'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(hash_length))

hashids = Hashids(min_length=hash_length, salt=app.config['SECRET_KEY'])

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/s/<string:url>/', methods=['GET', 'POST'])
def shorten(url):
    conn = get_db_connection()
    url_data = conn.execute('INSERT INTO urls (original_url) VALUES (?)',
                                (url,))

    #TODO An input validator could be added here to verify is a valid URL

    conn.commit()
    conn.close()

    url_id = url_data.lastrowid
    hashid = hashids.encode(url_id)
    short_url = request.host_url + hashid

    return jsonify({'url':url,'shortened_url': short_url})

@app.route('/<id>')
def url_redirect(id):
    conn = get_db_connection()

    original_id = hashids.decode(id)
    if original_id:
        original_id = original_id[0]
        url_data = conn.execute('SELECT original_url FROM urls'
                                ' WHERE id = (?)', (original_id,)
                                ).fetchone()

        original_url = url_data['original_url']

        conn.commit()
        conn.close()
        return jsonify({'id':id,'redirect_url': original_url})
    else:
        return jsonify({id : "Invalid URL"})

if __name__ == "__main__":
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0')
