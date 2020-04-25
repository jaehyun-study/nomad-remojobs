'''
stackoverflow
'''

import requests
from bs4 import BeautifulSoup


def get_html(term, page_num):
    try:
        url = f'https://stackoverflow.com/jobs?r=true&q={term}&pg={page_num+1}'
        return requests.get(url).text
    except:
        print('Error: get_html', page_num)
        return ''


def get_last_page_num(term):
    try:
        html = get_html(term, 0)
        soup = BeautifulSoup(html, 'html.parser')
        pagination = soup.find('div', class_='s-pagination')
        page_list = pagination.find_all('a')
        return int(page_list[-2].text)
    except:
        print('Error: get_last_page_num')
        return 0


def extract_job(job_soup):
    try:
        title = job_soup.find('h2').text.strip()
        company = job_soup.h3.span.text.strip()
        link_id = job_soup['data-jobid'].strip()
        return {
            'title': title,
            'company': company,
            'url': f'https://stackoverflow.com/jobs/{link_id}',
        }
    except:
        return None


def extract_jobs(term, last_page):
    jobs = []
    try:
        for page_num in range(0, last_page):
            print(f'extract_jobs page {page_num+1}/{last_page}')
            html = get_html(term, page_num)
            soup = BeautifulSoup(html, 'html.parser')
            job_list_soup = soup.find_all('div', class_='-job')
            for job_soup in job_list_soup:
                job = extract_job(job_soup)
                if job is None: continue
                jobs.append(job)
    except:
        pass
    return jobs


def get_jobs(term):
    print('get_jobs from stackoverflow')
    last_page = get_last_page_num(term)
    return extract_jobs(term, last_page)
