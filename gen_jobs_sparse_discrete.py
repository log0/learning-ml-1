"""
Project: learning-ml-1
Author: log0
Date: 3/24/2013

Generate job data for machine learning.

Job title: Tokenized into a set of keywords. All keywords that appeared will be represented by a sparse vector
with 1 denoting the keyword appeared in the job title and 0 denoting the keyword did not appear in the
job title.

Salary: A discrete class for each title

Format an Orange tab file (Data.Table), will be roughly as follows:
|----------+----------+-----+--------|
| Keyword1 | Keyword2 | ... | Salary |
|----------+----------+-----+--------|
| 1        | 0        | ... | 3      |
| 0        | 1        | ... | 2      |
| 0        | 0        | ... | 1      |
|----------+----------+-----+--------|
"""

import random
import common

job_types = [
    {'title': 'Software Engineer', 'salary': 2}, \
    {'title': 'Junior Software Engineer', 'salary': 1}, \
    {'title': 'Senior Software Engineer', 'salary': 3}, \
    {'title': 'Principal Software Engineer', 'salary': 4}, \
]

# Unique and tokenize all keywords in title
title_keywords = list(set([ keyword for job_type in job_types for keyword in job_type['title'].split(' ') ]))

for size in common.set_sizes:
    f = file('jobs.%d.sparse.discrete_classes.tab' % size, 'w')
    
    # Generate the three lines of header for Orange files
    for keyword in title_keywords:
        f.write(keyword + '\t')
    f.write('Salary\n')
    for keyword in title_keywords:
        f.write('d\t')
    f.write('d\n')
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
        salary = job_type['salary']
        f.write('%d\n' % (salary))
    f.close()