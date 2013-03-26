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

sample_input2 = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [0, 0, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    [22, 0, 0, 25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 0, 0, 37, 38, 39, 40, 41, 42, 43],
    [44, 45, 46, 0, 0, 49, 50, 51, 52, 53, 54],
    [55, 56, 57, 58, 0, 0, 61, 62, 63, 64, 65],
    [66, 67, 68, 69, 70, 0, 0, 73, 74, 75, 76],
    [77, 78, 79, 80, 81, 82, 0, 0, 85, 86, 87],
    [88, 89, 90, 91, 92, 93, 94, 0, 0, 97, 98],
    [99, 100, 101, 102, 103, 104, 105, 106, 0, 0, 109],
    [110, 111, 112, 113, 114, 115, 116, 117, 118, 0, 0]
 ]


def build_route(wstep_indexes, w_maxstep=5, h_maxstep=5):
    ret = ['d'] * (w_maxstep + h_maxstep)
    for pos in wstep_indexes:
        ret[pos] = 'r'
    return ret


def best_route(dataset, w_maxstep=0, h_maxstep=0, proc_fun=sum):
    last = None

    if not w_maxstep:
        w_maxstep = len(dataset[0]) - 1

    if not h_maxstep:
        h_maxstep = len(dataset) - 1

    for wstep_indexes in itertools.combinations(xrange(w_maxstep + h_maxstep), w_maxstep):
        w = Walker(build_route(wstep_indexes, w_maxstep=w_maxstep, h_maxstep=h_maxstep), dataset)
        w.collect()
        r = proc_fun(w.series)

        if not last:
            last = (w, r)
        else:
            last = min(last, (w, r), key=lambda a: a[1])

    return last


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


def benchmark():
    r1, diff1 = memusage_before_n_after(best_route, sample_input)
    r2, diff2 = memusage_before_n_after(best_route, sample_input2)

    print r1[1], r1[0].route
    print r2[1], r2[0].route


def sample_matrix(width, height, dataset=[]):
    start = 0
    end = width
    ret = []
    if not dataset:
        dataset = range(width * height)
    while end <= len(dataset):
        ret.append(dataset[start:end])
        start += width
        end += width

    return ret


def memusage_before_n_after(fun, *args, **kwargs):
    from pympler import muppy
    from pympler import summary
    from datetime import datetime

    before = summary.summarize(muppy.get_objects())
    before_time = datetime.now()
    fun_ret = fun(*args, **kwargs)
    after_time = datetime.now()
    after = summary.summarize(muppy.get_objects())
    diff = summary.get_diff(before, after)
    print "execution time: ", after_time - before_time
    summary.print_(diff)

    return fun_ret, diff
