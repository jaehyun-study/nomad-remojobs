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
    'frontend', 'backend', 'react', 'git', 'sql', 'nosql', 'c++', 'c', 'linux',
    'windows', 'scala', 'java', 'flask', 'database', 'node.js', 'agile',
    'hadoop', 'swift', 'qt', 'mongodb', 'algorithm', 'embedded', 'cloud',
    'kotlin'
]


@app.route('/')
def home():
    random.shuffle(terms)
    return render_template('home.html', terms=terms)


@app.route('/search')
def search():
    # term
    term = request.args.get('term')
    if not term: return redirect('/')
    term = term.lower()
    # jobs
    if term not in db:
        db[term] = so_jobs(term) + wwr_jobs(term) + ro_jobs(term)
    jobs = db[term]
    save_as_csv(term, jobs)
    job_count = len(jobs)
    # pagination
    page = {}
    jobs_per_page = 10
    page_btn_cnt = 5
    page['count'] = job_count // jobs_per_page
    if job_count % jobs_per_page: page['count'] += 1
    try:
        page['curr'] = int(request.args.get('page'))
    except:
        page['curr'] = 1
    if not (0 < page['curr'] <= page['count']):
        page['curr'] = 1
    page['start'] = max(1, page['curr'] - (page_btn_cnt // 2))
    if page['count'] >= page_btn_cnt:
        page['start'] = min(page['count'] - page_btn_cnt + 1, page['start'])
    page['end'] = min(page['count'] + 1, page['start'] + page_btn_cnt)
    # jobs slicing
    start_index = (page['curr'] - 1) * jobs_per_page
    jobs = jobs[start_index:start_index + jobs_per_page]
    # render
    return render_template(
        'search.html', term=term, job_count=job_count, jobs=jobs, page=page)


@app.route('/export')
def export():
    term = request.args.get('term')
    return send_file(f'./csv/{term}.csv', as_attachment=True)


app.run(host='0.0.0.0')
