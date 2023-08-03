## RustyStructs

Python data structures package written in Rust.

Currently available: priority heap, deque, stack.

To use:
1. Download/clone this repo
2. Setup a venv `python3 -m venv venv`
3. Activate the venv `source ./venv/bin/activate`
4. Important: if you have a conda environment activated you must deactivate it: `conda deactivate`
5. Make sure you have Rust installed
6. `pip install maturin`
7. `maturin develop`
8. `rustystructs` should be installed in your venv as a Python package, now you can just do `import rustystructs` in your Python file and start coding.
9. See either the code in `benchmarking/` or `test/` for syntax examples on how to use the package.

For each of these you can have data types of either integer or string.

These Rust implementations perform significantly faster than their Python counterparts.

Here are some benchmarks (all numbers are in seconds):
```
Integer Stack Performance Test
Num Elements	Rust        Python
1000	        0.00127	    0.00015
10000	        0.01161	    0.00135
100000	        0.10619	    0.01270
250000	        0.26735	    0.03131
500000	        0.53174	    0.06309
1000000	        1.06654	    0.12973
```

```
Integer Heap Performance Test
Num Elements	Rust	    Python	    Heapq
1000	        0.00167	    0.00226	    0.00016
10000	        0.01927	    0.03255	    0.00217
100000	        0.21781	    0.40080	    0.02402
250000	        0.56843	    1.13016	    0.06516
500000	        1.20106	    2.52821	    0.15069
1000000	        2.53874	    5.88021	    0.32154
```

(heapq definitely beats my implementation 😢)

```
Integer Deque Performance Test
Num Elements	Rust	    Python
1000	        0.00152	    0.00044
10000	        0.01486	    0.02976
100000	        0.15156	    3.08559
250000	        0.37582	    19.3481
500000	        0.75071	    80.6142
```
