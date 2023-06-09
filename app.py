from dbhelpers import run_statement
from apihelpers import check_data
from flask import Flask, request
import json

app = Flask(__name__)

@app.get('/api/philosopher')
def get_philosophers():
    results = run_statement('call get_philosophers()')
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Something is wrong"

@app.post('/api/philosopher')
def insert_philosopher():
    error = check_data(request.json, ['name', 'bio', 'date_of_birth', 'date_of_death', 'image_url'])
    if(error != None):
        return error
    results = run_statement('call insert_philosopher(?,?,?,?,?)', [request.json.get('name'), request.json.get('bio'), request.json.get('date_of_birth'), request.json.get('date_of_death'), request.json.get('image_url')])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Something is wrong"

@app.get('/api/quote')
def get_quotes_from_philosopher():
    error = check_data(request.args, ['philosopher_id'])
    if(error != None):
        return error
    results = run_statement('call get_quotes_from_philosopher(?)', [request.args.get('philosopher_id')])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Something is wrong"

@app.post('/api/quote')
def insert_quote():
    error = check_data(request.json, ['philosopher_id', 'content'])
    if(error != None):
        return error
    results = run_statement('call insert_quote(?,?)', [request.json.get('philosopher_id'), request.json.get('content')])
    if(type(results) == list):
        return json.dumps(results, default=str)
    else:
        return "Something is wrong"

app.run(debug=True)
