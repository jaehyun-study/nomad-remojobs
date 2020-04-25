"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from flask import Flask, render_template, request, redirect

app = Flask('RemoteJobs')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search')
def search():
    term = request.args.get('term')
    if not term: return redirect('/')
    term = term.lower()
    jobs = []
    return render_template(
        'search.html', term=term, job_count=len(jobs), jobs=jobs)


app.run(host='0.0.0.0')
