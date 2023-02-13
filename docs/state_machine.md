
# State Machine


<p>
    The state_machine.py file contains the engine behind the simulation, namely the StateMachine Class. When initializing
    the StateMachine, the predicates, sorts, scenario, max_t, and rules should be specified. After initializing the
    StateMachine, the StateMachine can be run. This is done by performing the .run() function --> StateMachine.run().
    If you want to enable Debug mode, "True" should be passed as argument. The StateMachine Class contains several functions
    and variables, which will be described underneath.
</p>

<h2>Functions</h2>
<ul>
    <li>filter_predicate_sorts(predicate)</li>
    <p>
        This function filters all the sorts of the predicate.
    </p>
    <li>create_predicate_dict(self, predicates)</li>
    <p>
        This function creates a dictionary from the <a href="../text_files/">predicates.txt file</a> of all predicates.
    </p>
    <li>filter_sort_values(sort)</li>
    <p>
        This function retrieves all possible values a sort can have.
    </p>
    <li>sort_sorts(self, sorts)</li>
    <p>
        This function creates a dictionary from the <a href="../text_files/">sorts.txt file</a> of all sorts.
    </p>
    <li>create_states(self)</li>
    <p>
        This function creates a fixed number of empty states (dependent on the max_t) and stores them to the self.states list.
    </p>
    <li>check_validity_pred(self, predicate_name, agent, value)</li>
    <p>
        This function checks the validity of a predicate with predicate name *predicate_name*. It checks whether the agent
        corresponding to the predicate is a valid agent and whether the sorts used in the predicate are valid sorts. This
        function will print warning messages if there are inconsistencies. The name of the function, *func_name*, is passed
        as argument to, in order to know which rule causes the warning messages.
    </p>
    <li>fill_states(self, scenario)</li>
    <p>
        This function fills the states, solely on the basis of the <a href="../text_files/">scenarios.txt file</a>
    </p>
    <li>show_debug_info(self)</li>
    <p>
        This function prints the debug information about all sorts and all predicates.
    </p>
    <li>run</li>
    <p>
        This function runs the StateMachine (and hence the simulation). All rules that are defined are executed for each
        timestep, starting from 1, till the max_t.
    </p>
    <li>filter_nested_predicate_info(self, predicate)</li>
    <p>
        This function filters information about a nested predicate from the scenarios file. It returns the name of the
        predicate, the agent(s), and the value(s)
    </p>
    <li>filter_predicate_info(predicate)</li>
    <p>
        This function filters information about a predicate from the scenarios file. It returns the name of the
        predicate, the agent(s), and the value(s)
    </p>
    <li>filter_predicate_time(self, time)</li>
    <p>
        This function filters the time relevant information of a predicate from the scenarios file. It returns the
        start -and end time.
    </p>
    <li>insert_single_predicate(self, predicate, agent, value, start_time, end_time)</li>
    <p>
        This functions creates an instance of Class Predicate with information *predicate* (name of the predicate),
        *agent*, and *value*, and inserts it in the states between the *start_time* and *end_time*.
    </p>
    <li>insert_nested_predicate(self, nest_name, agent, value, start_time, end_time)</li>
    <p>
        This functions creates an instance of Class Predicate with information *predicate* (name of the (overarching) predicate),
        *agent*, and *value*, and inserts it as nested predicate in the states between the *start_time* and *end_time*.
    </p>
    <li>insert_predicate(self, predicate, agent, value, start_time, end_time)</li>
    <p>
        This function either calls insert_single_predicate or insert_nested_predicate (based on whether the predicate is
        a nested predicate or not).
    </p>
</ul>

<h2>Variables</h2>

<ul>
    <li>max_t</li>
    <p>
        The max_t indicates for how many timesteps the simulation should run (max_t is the maximum t --> end t).
    </p>
    <li>rules</li>
    <p>
        A list of functions which are executed for every timestep. The rules are defined in the <a href="../jupyter/">Jupyter Notebook</a>.
    </p>
    <li>predicates</li>
    <p>
        A dictionary of all possible predicates. The key is the name of the predicate and the value is a list of the corresponding sorts.
    </p>
    <li>sorts</li>
    <p>
        A dictionary of all sorts. The key is the name of the sort and the value is a list of all possible values for that sort.
        The sorts Boolean and Real are not included.
    </p>
    <li>states</li>
    <p>
        A list of all states, ranging from state 1 till state max_t.
    </p>
</ul>