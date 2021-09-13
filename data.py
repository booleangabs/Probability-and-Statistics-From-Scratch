import regex as re
import numpy as np

class DataCsv:
    def __init__(self, path: str= None):
        self.data = parseCsv(path)
        self.header = list(self.data.keys())
     
    def __repr__(self):
        to_print = ', '.join(self.header) + '\n'
        to_print_vals = list(zip(*[self.data[i] for i in self.header]))
        for i in to_print_vals:
            to_print += ', '.join([str(j) for j in i]) + '\n'
        return to_print
    
    def __getitem__(self, item):
         return self.data[item]
     
    def __setitem__(self, name, item):
         self.data[name] = item
         
    def sort(self, name: str):
        idxs = np.argsort(self[name])
        for i in self.header:
            self[i] = np.array(self[i])
            self[i] = self[i][idxs]
            self[i] = list(self[i])
     
class TimeSeries(DataCsv):
    pass

       
def parseCsv(path: str) -> dict:
    file = open(path)
    data = {}
    headers = [i for i in file.readline().strip('\n').split(',')]
    for i in headers:
        data[i] = []
    while True:
        line = file.readline()
        if line == '':
            break
        line = parseLine(line)
        for i, h in enumerate(headers):
            data[h].append(line[i])
            
    return data
        
def parseLine(line: str, ) -> list:
    line = [i for i in line.strip('\n').split(',')]
    line_parsed = []
    for substring in line:
        rfloat = re.compile('[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?', re.VERBOSE)
        if bool(rfloat.match(substring)):
            if substring.isdigit():
                substring = int(substring)
            else:
                substring = float(substring)
        elif substring in ['True', 'False']:
            substring = int(bool(substring))
        line_parsed.append(substring)
    return line_parsed
        
        
        