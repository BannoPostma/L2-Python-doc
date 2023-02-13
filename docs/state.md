# State

<p>
    The state.py file consists of two classes: the State Class and the Predicate Class. You do not have to change anything
    in the state.py file.
</p>

<h2>The State Class</h2>
<p>
    The State Class contains all information about a state at a certain timepoint in the simulation. This Class consists
    of several variables and functions, typical for the State. When initializing a state, the timepoint of the state,
    the possible predicates, and the sorts should be passed as arguments.
</p>
<h3>Functions</h3>
<ul>
  <li>check_predicate(self, predicate)</li>
    <p>
        This function checks whether the passed predicate is already in the state. For example, if the function is called with
        as argument "has_age" and the state contains the predicate has_age(Bernie, 21), the function returns True. This function
        is used when adding predicates to a state.
    </p>
  <li>get_predicate(self, predicate)</li>
    <p>
        This function returns the predicate (instance of Class Predicate) with the name of the passed argument. If this predicate
        does not exist, it will print a warning message. A list of instances of the Class Predicate will be returned.
    </p>
  <li>get_predicate_by_agent(self, predicate, agent, index=0)</li>
    <p>
        This function returns a list of all possible predicates with name *predicate*, having agent *agent* at index
        *index*. If the index is not specified, 0 is used. If there are no such predicates, None is returned. A list of
        instances of the Class Predicate will be returned.
    </p>
  <li>check_validity_pred(self, predicate_name, agent, value, func_name)</li>
    <p>
        This function checks the validity of a predicate with predicate name *predicate_name*. It checks whether the agent
        corresponding to the predicate is a valid agent and whether the sorts used in the predicate are valid sorts. This
        function will print warning messages if there are inconsistencies. The name of the function, *func_name*, is passed
        as argument to, in order to know which rule causes the warning messages.
    </p>
  <li>add_predicate_to_state(self, predicate, func_name)</li>
    <p>
        This function adds a predicate (*predicate*) to the state. The func_name (name of rule) should be passed as argument,
        since the check_validity_pred function will first be executed.
    </p>
  <li>add_nested_predicate_to_state(self, nest_name, predicate_name, predicate)</li>
    <p>
        This function adds a nested predicate (e.g., observed) to the state. The nest_name is the overarching predicate
        (e.g., observed), the predicate_name is the name of the nested predicate (e.g., has_age), and predicate is an instance
        of the Class Predicate, containing the regular information of the predicate (and hence, not the overarching predicate).
    </p>
  <li>retrieve_observations(self)</li>
    <p>
        This function retrieves all observations that are in a State. A dictionary will be returned, with as keys the name
        of the observed predicate and as key a list of instances of Class Predicate.
    </p>
  <li>retrieve_beliefs(self)</li>
    <p>
        This function retrieves all beliefs that are in a State. A dictionary will be returned, with as keys the name
        of the believed predicate and as key a list of instances of Class Predicate.
    </p>
  <li>retrieve_assessments(self)</li>
    <p>
        This function retrieves all assessments that are in a State. A dictionary will be returned, with as keys the name
        of the assessed predicate and as key a list of instances of Class Predicate.
    </p>
  <li>get_nested_predicate(self, nest_name, pred_name)</li>
    <p>
        This function retrieves the predicates with as overarching name *nest_name* and as predicate name *pred_name*. It
        returns a list of instances of Class Predicate.
    </p>
  <li>get_nested_predicate_by_name(self, nest, predicate_name, agent, index=0)</li>
    <p>
        This function retrieves the predicates with as overarching name *nest_name*, as predicate name *pred_name* and
        having agent *agent* on place *index*. If no index is specified, 0 will be chosen. A list of the corresponding
        predicates (instances of Class Predicate) will be returned.
    </p>
  <li>check_belief_in_beliefs(self, predicate_name)</li>
    <p>
        This function checks whether the state contains a belief about the predicate with predicate name *predicate_name*.
    </p>
  <li>check_nested_pred(self, nest_name, pred_name)</li>
    <p>
        This function checks whether there is an overarching predicate with name *nest_name*, which contains the predicate
        with name *pred_name*. For example, check_nested_pred("belief", "has_age") checks whether there are beliefs about
        the predicate has_age (regardless of the information about the values and agents).
    </p>
  <li>show_pred_info(predicate)</li>
    <p>
        This function prints information about the predicate with name *predicate*. This function is used for debugging
        purposes.
    </p>
  <li>show_info(self)</li>
    <p>
        This function prints the information about all predicates that are in a state. This function is used for debugging
        purposes.
    </p>
</ul>

<h3>Variables</h3>

<ul>
    <li>t</li>
        <p>
            The timepoint of the state.
        </p>
    <li>predicates</li>
        <p>
            A dictionary, containing all predicates of a certain state.
        </p>
    <li>possible_predicates</li>
        <p>
            All possible predicates, defined in <a href="text_files.html">predicates.txt</a>
        </p>
    <li>sorts</li>
        <p>
            All possible sorts and their corresponding values (except for Real and Boolean), defined in <a href="text_files.html">sorts.txt</a>
        </p>
</ul>

<h2>The Predicate Class</h2>
<p>The Predicate Class contains all necessary information about a predicate. In addition, it contains some useful functions.</p>

<h3>Functions</h3>
<ul>
    <li>get_name_agent(self, index=0)</li>
    <p>
        This function returns the name of the agent at index *index*. If no index is indicated, 0 will be used.
    </p>
    <li>get_value(self)</li>
    <p>
        This function returns the value(s) of the predicate.
    </p>
    <li>print(self)</li>
    <p>
        This function prints the agents and and value of the predicate.
    </p>
</ul>


<h3>Variables</h3>
<ul>
    <li>name</li>
    <p>
        This variable contains the name of the predicate.
    </p>
    <li>agents</li>
    <p>
        This variable contains the agent(s) of the predicate.
    </p>
    <li>value</li>
    <p>
        This variable contains the value of the predicate.
    </p>
</ul>
