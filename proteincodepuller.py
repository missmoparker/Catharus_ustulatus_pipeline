import csv 

class Parser:
    file_name: str    
    codes = []

    def __init__(self, file_name: str):
        self.file_name = file_name

    def parse(self):
        with open(self.file_name) as f:
            rows = csv.reader(f, delimiter='\t')
            for row in rows:
                self._parse_row(row)
        #This will filter only unique values by using a 'set' type 
        #return list(set(filter(None, self.codes)))
        return self.codes
    
    def _parse_row(self, row):
        if len(row) < 10:
            return
        if row[4] == 'Aves':
            self.codes.append({ 'tcons': row[0], 'protein': row[5] })

class Writer:
    def __init__(self, file_name, data):
        self.file_name = file_name
        self.data = data

    def write(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            w = csv.DictWriter(csvfile, fieldnames=self.data[0].keys())
            w.writeheader()
            w.writerows(self.data)

if __name__ == "__main__":

    parser = Parser("Johnstonp02annotation.txt")
    data = parser.parse()
    for d in data: 
        print(d)

    writer = Writer("proteincodes_mypipeline.csv", data)
    writer.write()