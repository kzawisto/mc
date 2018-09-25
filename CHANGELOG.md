
## 0.1.0

- fixed bug in List __add__, added test
- added Dict addition and Set addition
- one can add iterable of pairs to Dict and get Dict.
- added mux function to multiplex callables
```python 
    mc.mux(min, max, sum)([1,2,3]) # (1, 3, 6)
```

- added chain function to chain callables
```python 
    mc.chain(lambda i: i + 1, str)(3) # "3"
```
- added predefined reducers for addition and multiplication
