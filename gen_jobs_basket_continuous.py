"""
Project: learning-ml-1
Author: log0
Date: 3/24/2013

Generate job data for machine learning.

Job title: string of the title

Salary: Real number between a range for a particular title.

Format an Orange tab file (Data.Table), will be roughly as follows:
|----------+--------|
| Title    | Salary |
|----------+--------|
| 1        | 57000  |
| 0        | 100000 |
| 0        | 80000  |
|----------+--------|
"""

import random
import common

job_types = [
    {'title': 'Software Engineer', 'salary': (100000, 120000)}, \
    {'title': 'Junior Software Engineer', 'salary': (80000, 100000)}, \
    {'title': 'Senior Software Engineer', 'salary': (140000, 220000)}, \
    {'title': 'Principal Software Engineer', 'salary': (220000, 320000)}, \
]

for size in common.set_sizes:
    f = file('jobs.%d.basket.continuous_classes.tab' % size, 'w')
    
    # Generate the three lines of header for Orange files
    f.write('Title\tSalary\n')
    f.write('basket\tc\n')
    f.write('\tclass\n')
    
    # Generate "size" instances of jobs randomly
    for i in xrange(size):
        job_type = random.choice(job_types)
        title = job_type['title']
        salary_range = job_type['salary']
        salary = round(random.randint(salary_range[0], salary_range[1]), -3) # Round to 123456 to 123000K
        f.write('%s\t%d\n' % (title, salary))
    f.close()