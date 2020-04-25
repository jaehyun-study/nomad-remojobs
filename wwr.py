'''
weworkremotely
'''

import requests
from bs4 import BeautifulSoup


def get_html(term):
    try:
        url = f'https://weworkremotely.com/remote-jobs/search?term={term}'
        return requests.get(url).text
    except:
        print('Error: get_html')
        return ''


def extract_job(job_soup):
    try:
        anchor = job_soup.find('a', recursive=False)
        title = anchor.find('span', class_='title').text
        company = anchor.find('span', class_='company').text
        link = anchor['href']
        return {
            'title': title,
            'company': company,
            'url': f'https://weworkremotely.com{link}',
        }
    except:
        return None


def extract_jobs(term):
    jobs = []
    html = get_html(term)
    soup = BeautifulSoup(html, 'html.parser')
    jobs_container = soup.find('div', class_='jobs-container')
    job_list_soup = jobs_container.find_all('li')
    for job_soup in job_list_soup:
        job = extract_job(job_soup)
        if job is None: continue
        jobs.append(job)
    return jobs


def get_jobs(term):
    print('get_jobs from weworkremotely')
    return extract_jobs(term)
