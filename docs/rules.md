# Rules

Every rule typically consists of three parts:
- fetching the required information from the previous time step
- computing the new value for the current time step
- adding the new value to the simulation log (the states)

## Define Rules

```python
def calculating_middle(states, t):

    # this is how we get the previous time step containing all previous predicates
    previous_state = states[t - 1]
    
    # now let's fetch the values we need. We need input 1, 2 and 3
    # we typically use a for loop since there may be multiple agents that have this predicate and they all need to be processed. 
    for agent1, agent2, input1 in previous_state.get_predicate("input1"):
        
        # we don't actually need agent2 but its good to show how it works, you could also print it
        # print(agent2)

        # now we have the first input we nee to make sure that the following searches are by the same agent
        # this searches a predicate named input2 which contains arnie as first agent
        for _,_, input2 in previous_state.get_predicate_by_agent("input2", agent1, 0):
            
            # the for loops are nested because otherwise we would lose our previous variables. 
            # we also use the _ to ignore the values in those places because we already have them
            for _,_,input3 in previous_state.get_predicate_by_agent("input3", agent1, 0):
                
                
                # finally we can calculate our new value according to our semi-formal rule (that we definitely did not change after realizing it was initially impossible to calculate with code)
                new_middle = input1 - input2 - input3
                
                
                # now that we did all that we can finally make a new predicate and return it to our state 
                # think carefully about in which for loop this bit should be
                # wowee i sure hope i did not make any mistakes
                new_predicate = Predicate("middle", [agent1], new_middle)
                states[t].add_predicate_to_state(new_predicate)
```