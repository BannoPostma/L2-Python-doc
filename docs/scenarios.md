# Scenarios

Scenarios allow you to define the value of predicates on certain time steps. You can imagine this as the starting state of your model. After a scenario is defined the model can be run to calculate which predicates will follow from these starting predicates.

## Define Scenarios
Scenarios are defined as a list `List[Tuple[str, List[str], List[int]]`:

```python
state_machine.scenario = (
    ("predicate_name", ["SORT1", "SORT2"], [start_time, end_time]
)
```