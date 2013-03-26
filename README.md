Test for mspace.

Wasn't the daily issues I am facing everyday.
Took me a while to find out the right metaphor or model for this issue:

1.) The question does not state how the distance is calculated.
So I need to verify every possible routes. Before I can verified, I need to get all the routes.

2.) Because the robot moves either right or down, so the I found a perfect way to get the combinations of 'r' steps indexes in a route by using:
itertools.combinations(range(width+height), width)

3.) use build_route to construct the routes based on 'r' steps indexes

4.) Verification with sample input/output: 
run batch_with_sum and batch_with_distance, and I found batch_with_sum gives me the result aligns to the sample output given out by the question. 
Actually batch_with_distance makes more sense to me, because I thought the hex number stands for the altitude of the terrain. 


Code refactoring - for performance & memory usage
remove all_routes, add a new function called best_route.
performance / mem-usage optimization
best_route now can fit into any size matrix, and you don't have to provide the width / height of matrix.
Please take a look at tests.py

```
w, r = route_planner.best_route([
    [0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0]
])
self.assertEqual(r, 0)
self.assertEqual(w.route, ['r', 'd', 'r', 'r', 'r', 'r'])

w, r = route_planner.best_route([
    [0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0]
])
self.assertEqual(r, 0)
self.assertEqual(w.route, ['r', 'd', 'd', 'r', 'r', 'r', 'r'])


w, r = route_planner.best_route([
    [0, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0]
])
self.assertEqual(r, 0)
self.assertEqual(w.route, ['r', 'd', 'r', 'd', 'r', 'd', 'r', 'r'])
	
```


