class Simpledb:
    def __init__(self, filename):
        self.filename = filename

    def __repr__(self):
        return "<Simpledb file='" + self.filename + "'>"

    def insert(self, key, value):
        f = open(self.filename, 'a')
        f.write(key + '\t' + value + '\n')
        f.close()

    def select_one(self, key):
        f = open(self.filename, 'r')
        found = False
        for row in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                print(v[:-1])
                found = True
                break
        if not found:
            print("{} is not found in the directory.".format(key))
        f.close()

    def delete(self, key):
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        found = False
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k != key:
                result.write(row)
            else:
                found = True
        if not found:
            print("{} is not found in the directory.".format(key))
        f.close()
        result.close()
        import os
        os.replace('result.txt', self.filename)

    def update(self, key):
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        found = False
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                number = input("What is the person's new number? ")
                result.write(key + '\t' + number + '\n')
                found = True
            else:
                result.write(row)
        if not found:
            print("{} is not found in the directory.".format(key))
        f.close()
        result.close()
        import os
        os.replace('result.txt', self.filename)
