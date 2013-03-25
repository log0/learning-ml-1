"""
Project: learning-ml-1
Author: log0
Date: 3/24/2013

Generate job data for machine learning.

Job title: Tokenized into a set of keywords. All keywords that appeared will be represented by a sparse vector
with 1 denoting the keyword appeared in the job title and 0 denoting the keyword did not appear in the
job title.

Salary: Real number between a range for a particular title.

Format an Orange tab file (Data.Table), will be roughly as follows:
|----------+----------+-----+--------|
| Keyword1 | Keyword2 | ... | Salary |
|----------+----------+-----+--------|
| 1        | 0        | ... | 57000  |
| 0        | 1        | ... | 100000 |
| 0        | 0        | ... | 80000  |
|----------+----------+-----+--------|
"""

import random
import common

job_types = [
    {'title': 'Software Engineer', 'salary': (100000, 120000)}, \
    {'title': 'Junior Software Engineer', 'salary': (80000, 100000)}, \
    {'title': 'Senior Software Engineer', 'salary': (140000, 220000)}, \
    {'title': 'Principal Software Engineer', 'salary': (220000, 320000)}, \
]

# Unique and tokenize all keywords in title
title_keywords = list(set([ keyword for job_type in job_types for keyword in job_type['title'].split(' ') ]))

for size in common.set_sizes:
    f = file('jobs.%d.sparse.continuous_classes.tab' % size, 'w')
    
    # Generate the three lines of header for Orange files
    for keyword in title_keywords:
        f.write(keyword + '\t')
    f.write('Salary\n')
    for keyword in title_keywords:
        f.write('d\t')
    f.write('c\n')
    for keyword in title_keywords:
        f.write('\t')
    f.write('class\n')
    
    # Generate "size" instances of jobs randomly
    for i in xrange(size):
        job_type = random.choice(job_types)
        for keyword in title_keywords:
            value = '0'
            if keyword in job_type['title'].split(' '):
                value = '1'
            f.write(value + '\t')
        salary_range = job_type['salary']
        salary = round(random.randint(salary_range[0], salary_range[1]), -3) # Round to 123456 to 123000K
        f.write('%d\n' % (salary))
    f.close()