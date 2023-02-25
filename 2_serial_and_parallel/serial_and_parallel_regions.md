 
```python
vector_1[0] = 1;
vector_1[1] = 1;

# part a
for i in 2 ... 1000:
	vector_1[i] = vector_1[i-1] + vector_1[i-2];

# part b
for i in 0 ... 1000:
	vector_2[i] = i;

# part c
for i in 0 ... 1000:
	vector_3[i] = vector_2[i] + vector_1[i];
	print("the sum of the vectors is.", vector_3[i]);
```

Part (a) requires access from the previous data sample - this cannot be parallelized. Part (b) can be run in parallel since it is not dependent on any other data - the same is true for part (c) given that (a) and (b) have been computed. Of course, part (b) is trivial and can be incorporated in part (c).

