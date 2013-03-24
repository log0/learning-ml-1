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

title_keywords = list(set([ keyword for job_type in job_types for keyword in job_type['title'].split(' ') ]))
# title_keywords.remove('Software')
# title_keywords.remove('Engineer')

for size in [10, 100, 1000, 10000, 100000]:
    f = file('jobs.%d.sparse.continuous_classes.tab' % size, 'w')
    
    # Generate headers
    for keyword in title_keywords:
        f.write(keyword + '\t')
    f.write('Salary\n')
    for keyword in title_keywords:
        f.write('d\t')
    f.write('c\n')
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
        salary_range = job_type['salary']
        salary = round(random.randint(salary_range[0], salary_range[1]), -3) # Round to 123456 to 123000K
        # salary = job_type['salary'][0]
        f.write('%d\n' % (salary))
    f.close()