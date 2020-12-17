from flask import Flask, request, render_template, jsonify
import sqlite3 as sql
import pandas as pd


app = Flask(__name__)


def load_csv_to_db(csv_file_name, db_name, table_name):
    connection = sql.connect(db_name)
    c = connection.cursor()
    df = pd.read_csv(csv_file_name)
    df.to_sql(table_name, connection, if_exists='replace', index=False)
    c.close()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/data', methods=['GET'])
def get_info():
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    con = sql.connect("database.db")
    con.row_factory = dict_factory

    cur = con.cursor()
    if not date_from and not date_to:
        return 'Please reload the page and type the dates!'
    elif not date_to:
        condition = f"Date > '{date_from}'"
    elif not date_from:
        condition = f"Date < '{date_to}'"
    else:
        condition = f"Date BETWEEN '{date_from}' AND '{date_to}'"
    sql_req = '''SELECT * FROM data WHERE ''' + condition + ''';'''
    cur.execute(sql_req)
    rows = cur.fetchall()
    return jsonify(rows)


if __name__ == '__main__':
    load_csv_to_db('aapl.csv', 'database.db', 'data')
    app.run(debug=False, host='0.0.0.0', port=5000)
