import regex as re
import numpy as np

class Dataset:
    '''
    Loader for csv datasets
    '''
    def __init__(self, path: str):
        '''
        

        Parameters
        ----------
        path : str, optional
            Path to csv file.

        Returns
        -------
        None.

        '''
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
         
    def sortByName(self, name: str):
        '''
        Sorts values in the data based on the values in a given column.

        Parameters
        ----------
        name : str
            Column name.

        Returns
        -------
        None.

        '''
        idxs = np.argsort(self[name])
        for i in self.header:
            self[i] = np.array(self[i])
            self[i] = self[i][idxs]
            self[i] = list(self[i])

       
def parseCsv(path: str) -> dict:
    '''
    

    Parameters
    ----------
    path : str
        Path to csv.

    Returns
    -------
    dict
        Dictionary containing parsed data.

    '''
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
        
def parseLine(line: str) -> list:
    '''
    Parses a line from csv file converting strings into the appropriate format

    Parameters
    ----------
    line : str
        


    Returns
    -------
    list
        Parsed values.

    '''
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
        
        
        