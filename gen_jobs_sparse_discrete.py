"""
Generates a list of job titles and their salary ranges
"""

import random

job_types = [
    {'title': 'Software Engineer', 'salary': 2}, \
    {'title': 'Junior Software Engineer', 'salary': 1}, \
    {'title': 'Senior Software Engineer', 'salary': 3}, \
    {'title': 'Principal Software Engineer', 'salary': 4}, \
]

title_keywords = list(set([ keyword for job_type in job_types for keyword in job_type['title'].split(' ') ]))

for size in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000]:
    f = file('jobs.%d.sparse.discrete_classes.tab' % size, 'w')
    
    # Generate headers
    for keyword in title_keywords:
        f.write(keyword + '\t')
    f.write('Salary\n')
    for keyword in title_keywords:
        f.write('d\t')
    f.write('d\n')
    for keyword in title_keywords:
        f.write('\t')
    f.write('class\n')
    
    # Begin generating data
    for i in xrange(size):
        job_type = random.choice(job_types)
        for keyword in title_keywords:
            value = '0'
            if keyword in job_type['title'].split(' '):
                value = '1'
            f.write(value + '\t')
        salary = job_type['salary']
        f.write('%d\n' % (salary))
    f.close()