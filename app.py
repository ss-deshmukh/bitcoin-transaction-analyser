#application created to query the btc address database

from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_address_data(address):
    conn = psycopg2.connect("dbname=test user=postgres password=secret")
    cur = conn.cursor()
    cur.execute("SELECT * FROM btc_addresses WHERE address = %s", (address,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

@app.route('/getaddress', methods=['GET'])
def address():
    address = request.args.get('address')
    data = get_address_data(address)
    if data:
        return jsonify({
            "address": data[0],
            "times_in_mixer": data[1],
            "criminal_activities": data[2],
            "high_volume_transactions": data[3],
            "last_active_date": str(data[4])
        })
    else:
        return "Address not found", 404

if __name__ == '__main__':
    app.run(debug=True)
