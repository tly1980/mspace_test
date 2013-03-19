import unittest
import route_planner


class TestRoutePlanner(unittest.TestCase):
    def setUp(self):
        pass

    def test_build_route(self):
        # given the right_indexes is [0], width = 2, height = 2
        # should return [r, d, d, d]

        self.assertEqual(
            route_planner.build_route([0], 2, 2),
            ['r', 'd', 'd', 'd']
        ),

        self.assertEqual(
            route_planner.build_route([1], 2, 2),
            ['d', 'r', 'd', 'd']
        ),

        self.assertEqual(
            route_planner.build_route([0, 1], 2, 2),
            ['r', 'r', 'd', 'd']
        ),

        self.assertEqual(
            route_planner.build_route([0, 1, 3], 2, 2),
            ['r', 'r', 'd', 'r']
        ),

    def test_Walker(self):
        route = ['r', 'r', 'd', 'd', 'r', 'd', 'd', 'r', 'r', 'd']
        w = route_planner.Walker(route, route_planner.sample_input)
        w.collect()
        self.assertEqual(w.series, [0x46B,
                                    0xE59, 0xEA,   # r, r
                                    0x926, 0x6d2,  # d, d
                                    0x976, 0x461,  # r, d
                                    0xd1d, 0xd03,  # d, r
                                    0xde3, 0x4d2]) # r, d

    def test_batch_with_sum(self):
        routes = route_planner.all_routes(5, 5)
        ret = route_planner.batch_with_sum(routes,
            dataset=route_planner.sample_input)

        self.assertEqual(ret[0][1], route_planner.sample_output)
