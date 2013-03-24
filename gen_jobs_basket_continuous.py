"""
Generates a list of job titles and their salary ranges
"""

import random

job_types = [
    {'title': 'Software Engineer', 'salary': (100000, 120000)}, \
    {'title': 'Junior Software Engineer', 'salary': (80000, 100000)}, \
    {'title': 'Senior Software Engineer', 'salary': (140000, 220000)}, \
    {'title': 'Principal Software Engineer', 'salary': (220000, 320000)}, \
]

for size in [10, 100, 1000]:
    f = file('jobs.%d.basket.continuous_classes.tab' % size, 'w')
    f.write('Title\tSalary\n')
    f.write('basket\tc\n')
    f.write('\tclass\n')
    for i in xrange(size):
        job_type = random.choice(job_types)
        title = job_type['title']
        salary_range = job_type['salary']
        salary = round(random.randint(salary_range[0], salary_range[1]), -3) # Round to 123456 to 123000K
        f.write('%s\t%d\n' % (title, salary))
    f.close()