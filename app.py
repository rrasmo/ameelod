from flask import Flask
from flask import render_template, request
import requests
import os
import sys


AMEE_API_COMPANIES_URL = 'https://www.amee.com/api/companies'
try:
    AMEE_API_KEY = os.environ['AMEE_API_KEY']
    AMEE_API_SECRET = os.environ['AMEE_API_SECRET']
except:
    print 'You must set AMEE_API_KEY and AMEE_API_SECRET'
    sys.exit()


app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    q = request.args.get('q')
    companies = []
    if q:
        res = requests.get(AMEE_API_COMPANIES_URL, auth=(AMEE_API_KEY, AMEE_API_SECRET), params={'company_name': q})
        if res.ok:
            companies = res.json()['companies']
    return render_template('index.html', companies=companies)


@app.route('/company/<cro>')
def company(cro):
    company = None
    if cro:
        res = requests.get(AMEE_API_COMPANIES_URL + '/' + cro, auth=(AMEE_API_KEY, AMEE_API_SECRET), params={'type': 'CRO'})
        if res.ok:
            company = res.json()['company']
    return render_template('company.html', company=company)


if __name__ == '__main__':
    app.run(debug=True)

