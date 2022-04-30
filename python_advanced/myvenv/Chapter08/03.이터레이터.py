
for i in "123":
    print(i)

for i in [10, 20, 30]:
    print(i)

print(dir([10, 20, 30]))
print(type([10, 20, 30].__iter__))
print([10, 20, 30].__iter__)

iter_obj = [10, 20, 30].__iter__()
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())


class seasons:
    def __init__(self):
        self.season_list = ['spring', 'summer', 'autumn', 'winter']
        self.idx = 0
        self.max_num = 4

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx < self.max_num:
            curr_idx = self.idx
            self.idx += 1
            return self.season_list[curr_idx]
        else:
            raise StopIteration

for i in seasons():
    print(i)

iter_obj = seasons().__iter__()
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())