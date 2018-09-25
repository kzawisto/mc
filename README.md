# MC 
## Monads with fluet API for python

```python
import mc

mc.List([1, 2, 3, 4]).map(lambda x: x * x # [1, 4, 9, 16]
    ).map(str # ["1", "4", "9", "16"]
    ).filter(lambda x: len(x)< 2 # ["1", "4", "9"]
    ).group_by(lambda x: int(x) % 2 # {0: ["4"], 1: ["1", "9"]}
    ).map_vals(lambda key, value: "_".join(value) # {0: "4", 1: "1_9"}
    ).map_keys(lambda key, value: {0:"even", 1:"odd"}[key] #  {"even": "4", "odd": "1_9"}
    ).mk_string(";", "=>","[[","]]") # [[even=>4;odd=>1_9]]'


mc.List([0,3,5,2,5,7,3,5,3,120,4,5]
    ).filter(lambda x: x < 10  # remove outlier
    ).map(mc.mux(min=min, max=max, sum=sum)) # dict with summary statistics

number_of_occurences = filenames.map(
    mc.chain( # lazy evaluation
        read_file,
        lambda line: "text to search" in line,
        len
    )
).reduce(mc.add)

```
## Requirements:
Python, package was tested with 2.7.10 and 3.4.3 on Linux environment.

Optionals:
Pathos required for multiprocess_map.
Nose and PyHamcrest are required for testing.

## Installation

Using pip:
```bash
pip install git+http://github.com/kzawisto/mc#0.1.1
```
Using git and setuptools
```bash
git clone http://github.com/kzawisto/mc
cd mc
git checkout 0.1.1
python install setup.py
```

## Tests

Clone repo, checkout desired version and install package (virtual environment recommended) as described above.
Then:
```
cd mc/tests
nosetests
```
Nose and PyHamcrest are required. Nosetests executable binary required in PATH
