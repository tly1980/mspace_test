Test for mspace.

Wasn't the daily issues I am facing everyday.

Took me a while to find out the right metaphor or model for this issue:

1.) The problem did not state how the distance is calculated.
So I need to verify every possible routes. Before I can verified, I need to get all the routes.

2.) Because the robot moves either right or down, so the I found a perfect way to get the combinations of 'r' steps indexes in a route by using:
itertools.combinations(range(width+height), width)

3.) use build_route to construct the routes based on 'r' steps indexes

4.) Verification with sample input/output: 
	run batch_with_sum and batch_with_distance, and I found batch_with_sum gives me the result aligns to the sample output given out by the question. 

	Actually batch_with_distance makes more sense to me, because I thought the hex number stands for the altitude of the terrain. 