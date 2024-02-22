# Sorts

Sorts describe the types of values you can use in your model. Is recommended to define these first when creating your model since predicates and scenarios depend on these existing.

## Define Sorts
Sorts are defined as a dictionary `Dict[str: List[str]]`:

```python
state_machine.sorts = {
    "SORT_NAME": ["value_name1", "value_name2"]
}
```