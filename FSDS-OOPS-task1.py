
# STRING TASKS

#    1 . Try to extract data from index one to index 300 with a jump of 3
#    2. Try to reverse a string without using reverse function
#    3. Finding Vowels in string

import logging
logging.basicConfig(filename='FSDS-OOPS-task1 logfile.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

class strings:

    def __init__(self,any_string):
        logging.info('string class constructor is created')
        self.any_string = any_string

    def extract(self):
        logging.info('string entered by user to extract')
        try:
            logging.info('juming 3 charc in string')
            exe = self.any_string[::3]
            return exe
        except Exception as e:
            logging.exception(e)

    def reversing(self):
        logging.info('string entered by user to reverse')
        try:
            logging.info('reversing the string')
            rev = self.any_string[::-1]
            return rev
        except Exception as e:
            logging.exception(e)

    def vowels(self):
        vow = 'aeiou'
        logging.info('string entered by user to find vowels')
        try:
            logging.info('picking up vowels from string')
            result = [i for i in self.any_string if i in vow]
            return result

        except Exception as e:
            logging.exception(e)

logging.shutdown()

test1 = strings(input('Enter a string: '))
print(test1.reversing())
print(test1.vowels())
print(test1.extract())

# lists

# 1. Try to extract only a list collection form list l
# 1. Try to extract only a tuples collection form list l
# 1. Try to extract only a set collection form list l
# 1. Try to extract only a dict collection form list l

class lists:
    def __init__(self,l):
        self.l = l

    def extract_lists(self):
        logging.info('extracting list entities')
        try:
            exe_l = [i for i in self.l if type(i) == list]
            return exe_l
        except Exception as e:
            logging.exception(e)

    def extract_tup(self):
        logging.info('extracting tuple entities')
        try:
            exe_t = [i for i in self.l if type(i) == tuple]
            return exe_t
        except Exception as e:
            logging.exception(e)

    def extract_sets(self):
        logging.info('extracting set entities')
        try:
            exe_s = [i for i in self.l if type(i) == set]
            return exe_s
        except Exception as e:
            logging.exception(e)

    def extract_dict(self):
        logging.info('extracting dict entities')
        try:
            exe_d = [i for i in self.l if type(i) == dict]
            return exe_d
        except Exception as e:
            logging.exception(e)

    def Occurence(self):
        logging.info('Counting the occurence of each item in list')
        try:
            l1 = []
            l2 = {}
            for i in self.l:
                if type(i) == int or type(i) == str:
                    l1.append(i)
                elif type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            l1.append(j)
                elif type(i) == dict:
                    for k,v in i.items():
                        l1.append(k)
                        l1.append(v)
            for i in set(l1):
                l2[i] = l1.count(i)

            return l2
        except Exception as e:
            logging.exception(e)

logging.shutdown()

test2 = lists([1,2,3,2,[50,60,50],(4,5,8,5,7,6,4,8),{4:2,5:4},3,5,{30,30,300}])
print(test2.extract_lists())
print(test2.extract_dict())
print(test2.extract_tup())
print(test2.extract_sets())
print(test2.Occurence())









