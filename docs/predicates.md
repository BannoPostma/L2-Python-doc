# Predicates

Predicates are the basic unit of knowledge in your model. Defining your predicates allows you to define how knowledge is represented. 

## Define Predicates
Predicates are defined as a dictionary `Dict[str: List[str]]`:

```python
state_machine.predicates = {
    "predicate_name": ["SORT1", "SORT2"]
}
```