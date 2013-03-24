"""import Orange

jobs = Orange.data.Table("jobs.tab")

learner = Orange.classification.bayes.NaiveLearner()

train_cutoff = len(jobs)*2/3
train_set = jobs[:train_cutoff]
test_set = jobs[train_cutoff:]

classifier = learner(train_set)

for job in test_set:
    print job.getclass(), classifier(job)
"""

import Orange
from Orange.evaluation import testing, scoring

jobs = Orange.data.Table("jobs2.tab")

learner = Orange.classification.svm.SVMLearner()

results = testing.cross_validation([learner], jobs, folds=5)


print "CA:  %.4f" % scoring.CA(results)[0]
# print "AUC: %.4f" % scoring.AUC(results)[0]