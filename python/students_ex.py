#!/usr/bin/env python
class Student(object):
    import sys


    name = ''
    grades = {'labs': [], 'exam': 0}
    conf = {}

    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        # Creating appropriate number of elements in labs list
        for num_labs in range(self.conf['lab_num']):
            self.grades['labs'].append(0)


    def make_lab(self, m, n=None):
        if (m > self.conf['lab_max']):
            m = self.conf['lab_max']
        if n == None:
            for i in range(len(self.grades['labs'])):
                if self.grades['labs'][i] == 0:
                    self.grades['labs'][i] = m
                    break
        elif n >= 0 and n < len(self.grades['labs']):
            self.grades['labs'][n] =  m
        return self


    def make_exam(self, m):
        if m <= self.conf['exam_max']:
            self.grades['exam'] = m
        else:
            self.grades['exam'] = self.conf['exam_max']
        return self


    def is_certified(self):
        maximum = self.conf['exam_max'] + (self.conf['lab_max'] * self.conf['lab_num'])
        sum_of_labs = sum(self.grades['labs'])
        overall_sum = (float(sum_of_labs) + float(self.grades['exam']))
        if float(self.conf['k']) <= (overall_sum / float(maximum)):
            return (overall_sum, True)
        else:
            return (overall_sum,  False)

conf = {'exam_max': 30, 'lab_max': 7, 'lab_num': 10,'k': 0.61}
oleg = Student('Oleg', conf)
oleg.make_lab(1)
oleg.make_lab(8,0)
oleg.make_lab(1)
oleg.make_lab(10,7)
oleg.make_lab(4,1)
oleg.make_lab(5)
oleg.make_lab(6.5)
oleg.make_exam(32) 
print(oleg.is_certified())
oleg.make_lab(7,1) 
print(oleg.is_certified())


