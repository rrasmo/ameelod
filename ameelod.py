from flask import Flask
from flask import render_template, url_for, request
import requests


API_KEY = ''
API_SECRET = ''
API_COMPANIES_URL = 'https://www.amee.com/api/companies'
API_COMPANY_URL = 'https://www.amee.com/api/company'


app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    q = request.args.get('q')
    companies = None
    if q:
        res = requests.get(API_COMPANIES_URL, auth=(API_KEY, API_SECRET), params={'company_name': q})
        if res.ok:
            companies = res.json()['companies']
    return render_template('index.html', companies=companies)


@app.route('/company/<cro>')
def company(cro):
    company = None
    return render_template('company.html', company=company)


if __name__ == '__main__':
    app.run(debug=True)

