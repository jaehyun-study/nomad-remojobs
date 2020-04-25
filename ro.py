'''
remoteok
'''

import requests
from bs4 import BeautifulSoup


def get_html(term):
    try:
        url = f'https://remoteok.io/remote-dev+{term}-jobs'
        return requests.get(url).text
    except:
        print('Error: get_html')
        return ''


def extract_job(job_soup):
    try:
        title = job_soup.find('h2', {'itemprop': 'title'}).text
        company = job_soup.find('h3', {'itemprop': 'name'}).text
        link_id = job_soup['data-id']
        return {
            'title': title,
            'company': company,
            'url': f'https://remoteok.io/remote-jobs/{link_id}',
        }
    except:
        return None


def extract_jobs(term):
    jobs = []
    try:
        html = get_html(term)
        soup = BeautifulSoup(html, 'html.parser')
        jobs_table = soup.find('table', id='jobsboard')
        job_list_soup = jobs_table.find_all('tr')
        for job_soup in job_list_soup:
            job = extract_job(job_soup)
            if job is None: continue
            jobs.append(job)
    except:
        pass
    return jobs


def get_jobs(term):
    print('get_jobs from remoteok')
    return extract_jobs(term)
