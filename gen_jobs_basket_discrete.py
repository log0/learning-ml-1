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
| 1        | 3      |
| 0        | 2      |
| 0        | 1      |
|----------+--------|
"""

import random
import common

job_types = [
    {'title': 'Software Engineer', 'salary': 2}, \
    {'title': 'Junior Software Engineer', 'salary': 1}, \
    {'title': 'Senior Software Engineer', 'salary': 3}, \
    {'title': 'Principal Software Engineer', 'salary': 4}, \
]

for size in common.set_sizes:
    f = file('jobs.%d.basket.discrete_classes.tab' % size, 'w')
    
    # Generate the three lines of header for Orange files
    f.write('Title\tSalary\n')
    f.write('basket\td\n')
    f.write('\tclass\n')
    
    # Generate "size" instances of jobs randomly
    for i in xrange(size):
        job_type = random.choice(job_types)
        title = job_type['title']
        salary = job_type['salary']
        f.write('%s\t%d\n' % (title, salary))
    f.close()