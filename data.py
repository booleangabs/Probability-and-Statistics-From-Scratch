class DataFrame:
    pass

def parseCsv(path: str) -> DataFrame:
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
            
    return DataFrame(data)
        
def parseLine(line: str) -> list:
    pass
        
        
        