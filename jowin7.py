#WAP using Iterator to generate the squence from 11 to 15

class Generator_data:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.start = 10
        return self

    def __next__(self):
        if self.start >= self.limit:
            raise StopIteration

        else:
            self.start = self.start+1
            return self.start


if __name__ == '__main__':
    limit = int(input('Enter the limit\t: '))
    iter_object = Generator_data(limit = 20)

    for data in iter_object:
        print(data)
        

