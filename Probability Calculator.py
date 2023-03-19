import copy
import random
# Consider using the modules imported above.


class Hat:
    # Pass a keyworded, variable-length argument list
    def __init__(self, **kwargs):
        # For key, value pair in item list, append v number of keys to list
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    # Accept number of balls to be drawn from the hat
    def draw(self, n):
        # n should be >= to the hat contents
        n = min(n, len(self.contents))
        # Remove random element from 'contents', return new 'contents' list, n number of times
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]


# Expected_balls is what we are calculating the probability of achieving. Dict format similar to kwarg
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Run experiment num_experiment number of times
    m = 0
    for _ in range(num_experiments):
        #Each iteration, use a copy of hat, with resultant balls drawn
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        # For each dict item, if number of balls drawn is greater= to number of values in expected_balls,
        # .. add 1 to the list. Balls_req is a sum of this list
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        # If balls_req = length of dict, m+=1
        m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments