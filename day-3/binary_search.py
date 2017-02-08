__author__ = 'Scott Businge'


class BinarySearch(list):

    def __init__(self, a, b):
        super(BinarySearch, self).__init__(range(0, (a*b)+1, b)[1:])
        self.length = a

    def search(self, x):
        try:
            x = int(x)  # Just incase x is a str digit
            output = {}
            count, first, last, found = 0, 0, len(self) - 1, False
            if x > self[last] or x < self[first]:
                return dict([("count", count), ("index", -1)])
            while not found and first <= last:
                centre = (first + last) // 2
                if self[last] == x:
                    found = True
                    output['index'] = last
                elif self[centre] > x:
                    last = centre - 1
                elif self[centre] < x:
                    first = centre + 1
                else:
                    found = True
                    output['index'] = centre
                if first == last:
                    found = True
                    output['index'] = -1
                output['count'] = count
                count += 1
            print(output)
            return output
        except:
            raise Exception("Error! Check your target input")
