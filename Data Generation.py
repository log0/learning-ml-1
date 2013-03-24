"""
Generates a list of job titles and their salary ranges
"""

import random

job_types = [
    {'title': 'Software Engineer', 'salary': (100000, 120000)}, \
    # {'title': 'Software Analyst', 'salary': (90000, 110000)}, \
    # {'title': 'Software Developer', 'salary': (100000, 120000)}, \
    # {'title': 'Software Programmer', 'salary': (80000, 110000)}, \
    {'title': 'Junior Software Engineer', 'salary': (80000, 100000)}, \
    # {'title': 'Junior Software Analyst', 'salary': (70000, 90000)}, \
    # {'title': 'Junior Software Developer', 'salary': (80000, 100000)}, \
    # {'title': 'Junior Software Programmer', 'salary': (60000, 90000)}, \
    {'title': 'Senior Software Engineer', 'salary': (140000, 220000)}, \
    # {'title': 'Senior Software Analyst', 'salary': (130000, 200000)}, \
    # {'title': 'Senior Software Developer', 'salary': (140000, 200000)}, \
    # {'title': 'Senior Software Programmer', 'salary': (120000, 190000)}, \
    {'title': 'Principal Software Engineer', 'salary': (220000, 320000)}, \
    # {'title': 'Principal Software Analyst', 'salary': (180000, 300000)}, \
    # {'title': 'Principal Software Developer', 'salary': (200000, 300000)}, \
    # {'title': 'Principal Software Programmer', 'salary': (170000, 270000)}, \
]

f = file('jobs.data', 'w')

f.write('Title    Salary' + '\n')
for i in xrange(10):
    job_type = random.choice(job_types)
    title = job_type['title']
    salary_range = job_type['salary']
    salary = round(random.randint(salary_range[0], salary_range[1]), -3) # Round to 123456 to 123000K
    
    # Print the results out
    f.write('"%s"    %d\n' % (title, salary))