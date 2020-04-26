'''
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
'''

from flask import Flask, render_template, request, redirect, send_file
from ro import get_jobs as ro_jobs
from so import get_jobs as so_jobs
from wwr import get_jobs as wwr_jobs
from writer import save_as_csv
import random

db = {}
app = Flask('RemoteJobs')
terms = [
    'python', 'ruby', 'aws', 'django', 'go', 'docker', 'kubernetes',
    'frontend', 'backend', 'react', 'git', 'sql', 'nosql', 'c++', 'c',
    'tensorflow', 'linux', 'windows', 'scala', 'java', 'flask', 'database',
    'node.js', 'agile', 'hadooop', 'swift', 'qt', 'mongodb', 'algorithm',
    'embedded', 'cloud', 'kotlin'
]


@app.route('/')
def home():
    random.shuffle(terms)
    return render_template('home.html', terms=terms)


@app.route('/search')
def search():
    term = request.args.get('term')
    if not term: return redirect('/')
    term = term.lower()
    if term not in db:
        db[term] = so_jobs(term) + wwr_jobs(term) + ro_jobs(term)
    jobs = db[term]
    save_as_csv(term, jobs)
    return render_template(
        'search.html', term=term, job_count=len(jobs), jobs=jobs)


@app.route('/export')
def export():
    term = request.args.get('term')
    return send_file(f'./csv/{term}.csv', as_attachment=True)


app.run(host='0.0.0.0')
