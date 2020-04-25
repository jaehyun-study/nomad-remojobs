import csv

def save_as_csv(term, jobs):
    print('save as csv')
    file = open(f'./csv/{term}.csv', 'w')
    writer = csv.writer(file)
    writer.writerow(['Title', 'Company', 'Link'])
    for job in jobs:
        writer.writerow(list(job.values()))