import Orange
from Orange.evaluation import testing, scoring

jobs = Orange.data.Table("jobs.1000.sparse.discrete_classes.tab")

learner = Orange.classification.svm.SVMLearner()
results = testing.cross_validation([learner], jobs, folds=5)

print "CA:  %.4f" % scoring.CA(results)[0]
# print "AUC: %.4f" % scoring.AUC(results)[0]