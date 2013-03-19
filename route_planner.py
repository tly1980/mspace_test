import itertools

sample_input = [
    [0x46B, 0xE59,  0xEA, 0xC1F, 0x45E, 0x63],
    [0x899, 0xFFF, 0x926, 0x7AD, 0xC4E, 0xFFF],
    [0xE2E, 0x323, 0x6D2, 0x976, 0x83F, 0xC96],
    [0x9E9, 0xA8B, 0x9C1, 0x461, 0xF74, 0xD05],
    [0xEDD, 0xE94, 0x5F4, 0xD1D, 0xD03, 0xDE3],
    [0x89,  0x925, 0xCF9, 0xCA0, 0xF18, 0x4D2],
]

sample_output = [
   'r', 'r', 'd', 'd', 'r', 'd', 'd', 'r', 'r', 'd'
]


def build_route(right_indexes, width=5, height=5):
    ret = ['d'] * (width + height)
    for pos in right_indexes:
        ret[pos] = 'r'
    return ret


def all_routes(width=5, height=5):
    right_indexes_list = itertools.combinations(
        range(width+height), width)

    ret = []

    for right_indexes in right_indexes_list:
        ret.append(build_route(right_indexes))

    return ret


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)


class Walker:
    def __init__(self, route, dataset):
        self.dataset = dataset
        self.route = route
        self.result = 0
        self.series = []
        self.result = 0

    def collect(self):
        self.result = 0
        x, y = 0, 0
        a = self.dataset[y][x]
        self.series.append(a)
        for step in self.route:
            if step == 'd':
                y += 1
            else:
                x += 1
            b = self.dataset[y][x]
            a = b
            self.series.append(b)

    def run(self, serires_handler):
        self.result = serires_handler(self.series)


def batch_with_distance(routes=[], dataset=sample_input):
    ret = []
    if not routes:
        routes = all_routes()

    def distance(series):
        total = 0
        for a, b in pairwise(series):
            total += abs(a - b)
        return total

    for r in routes:
        w = Walker(r, dataset)
        w.collect()
        w.run(distance)
        ret.append((w.result, w.route))

    return sorted(ret, key=lambda tup: tup[0])


def batch_with_sum(routes=[], dataset=sample_input):
    ret = []
    if not routes:
        routes = all_routes()

    for r in routes:
        w = Walker(r, dataset)
        w.collect()
        ret.append((sum(w.series), w.route))

    return sorted(ret, key=lambda tup: tup[0])
