'''The first day acts like adding a variability, like how we distinct male and female in a school.
Now to the second day, which is where Law of large number comes in. If the whole school's gender ratio is 50-50,
then with a large enough sample, we would also expect the same gender ratio, right? Back to the car example,
suppose first day I try to mark as many as I can (to make the estimation more reliable). When I sample in the
2nd day, and also try to sample as many as possible, I would expect the ratio of recaptured marked cars
to sampled cars is approximately the same as total marked cars to total population.
This happens because marking a car doesnt not reduce its chance of being picked in the
2nd day (suppose everything happens randomly), so every car is independent, which means the only factor
that affects their chance of being picked is the difference in proportion.

A minor note: this should happen on weekdays, maybe tuesday and wednesday, because a city is not a closed system,
people could come and go, so it's better to reduce the chance of people leaving the city by sampling fast
and not including weekends'''

import random

true_pop_size = 100000 # should be unknown
# Assign ID to each car
pop_id = list(range(1, true_pop_size+1))

# Day 1: Mark the cars
marked_car = 6000
marked_id = set(random.sample(pop_id, marked_car))

print(f"Marked cars day 1: {len(marked_id)}")

# Day 2: Recapture (or resample the population)
sample_size = 15000
sample_id = set(random.sample(pop_id, sample_size))

print(f"Sample cars day 2: {len(sample_id)}")

# Find the overlapping cars
recapture_marked = marked_id.intersection(sample_id)

print(f"Found {len(recapture_marked)} cars in the sample")

# Calculate the population (estimated)
pop_estimate = marked_car / (len(recapture_marked)/sample_size)

print(f"Estimated population is: {pop_estimate}")
