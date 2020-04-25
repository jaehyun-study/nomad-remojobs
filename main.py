'''
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
'''

from flask import Flask, render_template, request, redirect
from ro import get_jobs as ro_jobs
from so import get_jobs as so_jobs
from wwr import get_jobs as wwr_jobs

app = Flask('RemoteJobs')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search')
def search():
    term = request.args.get('term')
    if not term: return redirect('/')
    term = term.lower()
    jobs = so_jobs(term) + wwr_jobs(term) + ro_jobs(term)
    return render_template(
        'search.html', term=term, job_count=len(jobs), jobs=jobs)


app.run(host='0.0.0.0')
