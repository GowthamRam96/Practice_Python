# Code
```py
import numpy as np
import matplotlib.pyplot as plt
from deap import algorithms, base, benchmarks, \
cma, creator, tools

# Function to create a toolbox
def create_toolbox(strategy):
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    toolbox = base.Toolbox()
    toolbox.register("evaluate", benchmarks.rastrigin)
    # Seed the random number generator
    np.random.seed(7)

    toolbox.register("generate", strategy.generate,
                     creator.Individual)
    toolbox.register("update", strategy.update)
    return toolbox

if __name__ == "__main__":
    # Problem size
    num_individuals = 10
    num_generations = 125

    # Create a strategy using CMA-ES algorithm
    strategy = cma.Strategy(centroid=[5.0] * num_individuals, sigma=5.0,
                            lambda_=20 * num_individuals)

    # Create toolbox based on the above strategy
    toolbox = create_toolbox(strategy)

    # Create hall of fame object
    hall_of_fame = tools.HallOfFame(1)

    # Register the relevant stats
    stats = tools.Statistics(lambda x: x.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    logbook = tools.Logbook()
    logbook.header = "gen", "evals", "std", "min", "avg", "max"

    # Objects that will compile the data
    sigma = np.ndarray((num_generations, 1))
    axis_ratio = np.ndarray((num_generations, 1))
    diagD = np.ndarray((num_generations, num_individuals))
    fbest = np.ndarray((num_generations, 1))
    best = np.ndarray((num_generations, num_individuals))
    std = np.ndarray((num_generations, num_individuals))

    for gen in range(num_generations):
        # Generate a new population
        population = toolbox.generate()
        # Evaluate the individuals
        fitnesses = toolbox.map(toolbox.evaluate, population)
        for ind, fit in zip(population, fitnesses):
            ind.fitness.values = fit
        # Update the strategy with the evaluated individuals
        toolbox.update(population)

        # Update the hall of fame and the statistics with the
        # currently evaluated population
        hall_of_fame.update(population)
        record = stats.compile(population)
        logbook.record(evals=len(population), gen=gen, **record)
        print(logbook.stream)

        # Save more data along the evolution for plotting
        sigma[gen] = strategy.sigma
        axis_ratio[gen] = max(strategy.diagD) ** 2 / min(strategy.diagD) ** 2
        diagD[gen, :num_individuals] = strategy.diagD ** 2
        fbest[gen] = hall_of_fame[0].fitness.values
        best[gen, :num_individuals] = hall_of_fame[0]
        std[gen, :num_individuals] = np.std(population, axis=0)

    # The x-axis will be the number of evaluations
    x = list(range(0, strategy.lambda_ * num_generations,
                   strategy.lambda_))
    avg, max_, min_ = logbook.select("avg", "max", "min")
    plt.figure()
    plt.semilogy(x, avg, "--b")
    plt.semilogy(x, max_, "--b")
    plt.semilogy(x, min_, "-b")
    plt.semilogy(x, fbest, "-c")
    plt.semilogy(x, sigma, "-g")
    plt.semilogy(x, axis_ratio, "-r")
    plt.grid(True)
    plt.title("blue: f-values, green: sigma, red: axis ratio")

    plt.figure()
    plt.plot(x, best)
    plt.grid(True)
    plt.title("Object Variables")
    plt.figure()
    plt.semilogy(x, diagD)
    plt.grid(True)
    plt.title("Scaling (All Main Axes)")
    plt.figure()
    plt.semilogy(x, std)
    plt.grid(True)
    plt.title("Standard Deviations in All Coordinates")
    plt.show()

```
# Results
```
gen	| evals	| std |     min  |      avg  |  max |   
0  	|200  |	188.36	|217.082 |  576.281	|1199.71|
1  	|200  |	250.543|	196.583|	659.389|	1869.02|
2  	|200  |	273.081|	199.455|	683.641|	1770.65|
3  	|200  |	215.326|	111.298|	503.933|	1579.3 |
4  	|200  |	133.046|	149.47 |	373.124|	790.899|
5  	|200  |	75.4405|	131.117|	274.092|	585.433|
6  	|200  |	61.2622|	91.7121|	232.624|	426.666|
7  	|200  |	49.8303|	88.8185|	201.117|	373.543|
8  	|200  |	39.9533|	85.0531|	178.645|	326.209|
9  	|200  |	31.3781|	87.4824|	159.211|	261.132|
10 	|200  |	31.3488|	54.0743|	144.561|	274.877|
11 	|200  |	30.8796|	63.6032|	136.791|	240.739|
12 	|200  |	24.1975|	70.4913|	125.691|	190.684|
13 	|200  |	21.2274|	50.6409|	122.293|	177.483|
14 	|200  |	25.4931|	67.9873|	124.132|	199.296|
15 	|200  |	26.9804|	46.3411|	119.295|	205.331|
16 	|200  |	24.8993|	56.0033|	115.614|	176.702|
17 	|200  |	21.9789|	61.4999|	113.417|	170.156|
18 	|200  |	21.2823|	50.2455|	112.419|	190.677|
19 	|200  |	22.5016|	48.153 |	111.543|	166.2  |
20 	|200  |	21.1602|	32.1864|	106.044|	171.899|
21 	|200  |	23.3864|	52.8601|	107.301|	163.617|
22 	|200  |	23.1008|	51.1226|	109.628|	185.777|
23 	|200  |	22.0836|	51.3058|	106.402|	179.673|
24 	|200  |	21.6711|	43.7379|	108.874|	176.912|
25 	|200  |	22.1262|	39.1044|	107.418|	157.952|
26 	|200  |	23.2654|	44.458 |	103.777|	159.32 |
27 	|200  |	21.8611|	55.216 |	107.235|	155.289|
28 	|200  |	23.0877|	42.1851|	105.999|	172.972|
29 	|200  |	22.8362|	41.4296|	104.366|	154.051|
30 	|200  |	21.6695|	57.128 |	102.926|	157.211|
31 	|200  |	20.805 |	49.8769|	106.218|	158.955|
32 	|200  |	20.6291|	44.542 |	100.111|	154.066|
33 	|200  |	23.7262|	46.8485|	102.205|	159.631|
34 	|200  |	25.4287|	40.3176|	98.1871|	161.217|
35 	|200  |	23.4826|	41.7417|	99.2177|	156.218|
36 	|200  |	21.8911|	29.2574|	99.6218|	156.164|
37 	|200  |	22.3132|	42.6462|	96.5396|	147.5  |
38 	|200  |	22.3333|	37.2513|	95.8662|	175.645|
39 	|200  |	21.4681|	43.7601|	94.7775|	161.015|
40 	|200  |	22.0902|	37.189 |	89.2357|	143.142|
41 	|200  |	21.2951|	27.6268|	84.4612|	135.569|
42 	|200  |	21.1002|	24.7394|	77.7523|	141.516|
43 	|200  |	18.2397|	16.1219|	65.3421|	111.586|
44 	|200  |	17.0689|	23.0472|	59.4038|	112.187|
45 	|200  |	15.7116|	18.4409|	53.3594|	96.9458|
46 	|200  |	14.1788|	15.6986|	45.544 |	90.4037|
47 	|200  |	14.0675|	13.5535|	42.6935|	83.1408|
48 	|200  |	13.7313|	9.98353|	37.9762|	89.3393|
49 	|200  |	10.3671|	8.1742 |	30.9458|	63.3374|
50 	|200  |	12.2796|	4.38929|	29.8394|	66.89  |
51 	|200  |	11.1358|	4.90423|	27.3507|	78.2447|
52 	|200  |	9.80632|	1.49144|	23.3165|	51.1713|
53 	|200  |	8.59435|	3.33225|	20.2306|	52.2095|
54 	|200  |	7.65374|	1.62632|	16.7318|	36.8411|
55 	|200  |	6.66501|	2.04   |	13.8645|	33.0381|
56 	|200  |	5.96102|	2.1138 |	11.017 |	31.9201|
57 	|200  |	4.25872|	0.827481|	7.88416|	29.497| 
58 	|200  |	3.61782|	1.22496| 	5.91817|	18.5905|
59 	|200  |	2.07606|	0.760155|	3.90396|	13.2943|
60 	|200  |	1.35583|	0.491193	2.43455|	7.47713|
61 	|200  |	0.742762|	0.31884 	1.52808|	5.4474| 
62 	|200  |	0.667678|	0.281471	|1.19323|	4.68609|
63 	|200  |	0.326356|	0.154596	|0.697761|	2.42983|
64 	|200  |	0.243054|	0.126554	|0.525933|	1.44597|
65 	|200  |	0.191034|	0.0710941	|0.412517|	1.3232 |
66 	|200  |	0.138682|	0.0450325	|0.301216	|0.793144|
67 	|200  |	0.10265| 	0.0460312	|0.200996	|0.61223 |
68 	|200  |	0.0579847|	0.0368484	|0.131184	|0.35222| 
69 	|200  |	0.0412192|	0.02229  	|0.0963417	|0.233402 |
70 	|200  |	0.0313367|	0.0138116	|0.0627599	|0.233222 |
71 	|200  |	0.0226773|	0.00876078	|0.044346 	|0.158384 |
72 	|200  |	0.0150391|	0.00814129	|0.0324236	|0.134   |
73 	|200  |	0.00957893|	0.00460441	|0.0220713	|0.049323 |
74 	|200  |	0.00737102|	0.00310443	|0.0155654	|0.0462904 |
75 	|200  |	0.00472435| 0.00242127	|0.0100571	|0.0295158 |
76 	|200  |	0.00307246|	0.00119198	|0.00678096	|0.017253 |
77 	|200  |	0.00183693|	0.000708929	|0.00432647	|0.0105079 |
78 	|200  |	0.00121884|	0.000455251	|0.00277348	|0.00695589 |
79 	|200  |	0.000826155|	0.000389592|	0.00176792|	0.00559699 |
80 	|200  |	0.000585931|	0.000335389|	0.00128037|	0.00386601 |
81 	|200  |	0.000429632|	9.911e-05  |	0.000849252|	0.00285739 |
82 	|200  |	0.000246462|	7.8131e-05 |	0.000529938|	0.00137593 |
83 	|200  |	0.000162157|	4.21666e-05|	0.000345107|	0.000869259 |
84 	|200  |	0.000111079|	4.01871e-05|	0.000222001|	0.000650251 |
85 	|200  |	7.35413e-05|	4.15435e-05|	0.000157564|	0.000377442 |
86 	|200  |	4.75334e-05|	2.27226e-05|	9.43132e-05|	0.000273214 |
87 	|200  |	3.14724e-05|	1.90096e-05|	7.06404e-05|	0.000166621 |
88 	|200  |	2.06396e-05|	1.09665e-05|	4.5784e-05 	|0.000127969 |
89 	|200  |	1.56703e-05|	8.46726e-06|	3.38256e-05	|0.000125051 |
90 	|200  |	9.82441e-06|	3.69234e-06|	2.16204e-05	|6.00548e-05 |
91 	|200  |	7.63651e-06|	3.92889e-06|	1.62779e-05	|5.53005e-05 |
92 	|200  |	5.25144e-06|	2.13612e-06|	1.0918e-05 	|2.90733e-05 |
93 	|200  |	3.05229e-06|	1.46242e-06|	7.34596e-06| 1.85028e-05 |
94 	|200  |	2.69715e-06|	1.12081e-06|	5.58773e-06| 1.74894e-05 |
95 	|200  |	1.82983e-06|	7.26304e-07|	4.01013e-06| 9.73041e-06 |
96 	|200  |	1.01811e-06|	6.03807e-07|	2.39782e-06| 8.21269e-06 |
97 	|200  |	7.13563e-07|	3.86061e-07|	1.57891e-06| 4.35743e-06 |
98 	|200  |	5.17517e-07|	1.60515e-07|	1.08331e-06| 3.43492e-06 | |
99 	|200  |	3.63183e-07|	1.715e-07  |	7.94257e-07| 2.58839e-06 |  
100	|200  |	2.42371e-07|	1.36725e-07|	5.15987e-07| 1.19228e-06 |
101	|200  |	1.54049e-07|	4.69571e-08|	3.38713e-07| 9.0053e-07  |
102	|200  |	1.15277e-07|	3.18943e-08|	2.53913e-07| 8.14231e-07 |
103	|200  |	9.05727e-08|	2.94641e-08|	1.82214e-07| 5.79947e-07 |
104	|200  |	5.09824e-08|	2.13545e-08|	1.10195e-07| 2.51502e-07 |
105	|200  |	4.56307e-08|	1.52451e-08|	8.64983e-08| 2.66064e-07 |
106	|200  |	2.49424e-08|	1.18998e-08|	5.88332e-08| 1.59796e-07 |
107	|200  |	1.70462e-08|	7.08934e-09|	3.5188e-08 | 1.01745e-07 |
108	|200  |	9.89045e-09|	5.74676e-09|	2.18801e-08| 5.78322e-08 |
109	|200  |	6.71803e-09|	3.65401e-09|	1.43638e-08| 4.35225e-08 |
110	|200  |	4.39307e-09|	1.48775e-09|	1.02335e-08| 2.68797e-08 |
111	|200  |	3.26246e-09|	1.397e-09  |	6.92347e-09| 1.97411e-08 |
112	|200  |	2.21481e-09|	1.04214e-09|	5.14959e-09| 1.31746e-08 |
113	|200  |	1.96222e-09|	6.24141e-10|	4.12443e-09| 1.01623e-08 |
114	|200  |	1.15578e-09|	4.03659e-10|	2.45078e-09| 7.9977e-09  |
115	|200  |	8.63667e-10|	1.62174e-10|	1.80088e-09| 5.95105e-09 |
116	|200  |	5.00298e-10|	3.11019e-10|	1.19956e-09| 2.91089e-09 |
117	|200  |	3.43539e-10|	1.41625e-10|	6.81353e-10| 1.63566e-09 |
118	|200  |	2.22699e-10|	1.47097e-10|	5.08937e-10| 1.26482e-09 |
119	|200  |	1.62103e-10|	6.08082e-11|	3.51655e-10| 9.74396e-10 |
120	|200  |	9.20864e-11|	4.12967e-11|	2.05411e-10| 6.0605e-10  |
121	|200  |	6.52617e-11|	4.28884e-11|	1.57709e-10| 4.09869e-10 |
122	|200  |	4.71043e-11|	2.37179e-11|	1.0917e-10 | 2.92573e-10 |
123	|200  |	3.70369e-11|	2.05773e-11|	8.07213e-11| 2.10605e-10 |
124	|200  |	2.71108e-11|	1.01608e-11|	5.75073e-11| 1.58209e-10 |
```

![image](https://user-images.githubusercontent.com/84629235/162464171-9e4f4361-48c4-4420-8a60-f7b1074145cb.png)

![image](https://user-images.githubusercontent.com/84629235/162464230-25c02b14-733d-4081-a80a-da2eff3e0183.png)

![image](https://user-images.githubusercontent.com/84629235/162464306-f0fd9c9d-0ca5-4934-b22d-a94ac20dcdbc.png)

![image](https://user-images.githubusercontent.com/84629235/162464372-9b5f5b4b-3863-4fd8-a1dc-280a70d9cb0b.png)

