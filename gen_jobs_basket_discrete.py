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

for size in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000]:
    f = file('jobs.%d.basket.discrete_classes.tab' % size, 'w')
    f.write('Title\tSalary\n')
    f.write('basket\td\n')
    f.write('\tclass\n')
    for i in xrange(size):
        job_type = random.choice(job_types)
        title = job_type['title']
        salary = job_type['salary']
        f.write('%s\t%d\n' % (title, salary))
    f.close()