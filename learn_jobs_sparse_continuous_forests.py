import Orange
from Orange.evaluation import testing, scoring

jobs = Orange.data.Table("jobs.10000.sparse.continuous_classes.tab")
jobs_test = Orange.data.Table("jobs.100.sparse.continuous_classes.tab")

learner = Orange.ensemble.forest.RandomForestLearner(trees=30, name="forest")

classifier = learner(jobs)

accurate = 0
for job in jobs_test:
    expected_class = job.getclass()
    actual_class = classifier(job)
    if abs(actual_class - expected_class) < 10000:
        accurate += 1
        print expected_class, actual_class
        
print '%s' % (accurate/float(len(jobs_test)))