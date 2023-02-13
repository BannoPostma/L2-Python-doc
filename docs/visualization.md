
# Visualization



<p>
    The visualization.py file is used to make the graphs and thereby "visualizing" the simulation. The visualization is
    started by calling the run_visualization function. This function should be called after the StateMachine has run. The
    executed StateMachine should be passed as argument to this function. A possible argument is the so-called "predicate_to_remove"
    argument. The predicates you do not want to show should be placed inside a list and be passed as second argument. If you
    do not want to remove any predicate, only pass the StateMachine. If you want to remove a nested predicate (e.g., a
    belief about has_age), you should add the overarching predicate name with a dash before the predicate name. To remove
    the example predicate: ["belief_has_age"].<br>
    The run_visualization first starts to create a dictionary containing all information from the states, which can be
    easily translated to a graph. If a predicate misses information (e.g., no information yet at t=1), None is added as
    value. Finally, for every key in the dictionary (for every predicate), a separate graph is made. <br>
    There two different types of plots: 1. a line graph for numerical plots and 2. a bar graph for non-numerical plots.
</p>

<h2>Functions</h2>
<ul>
    <li>make_visualization_dic(state_machine)</li>
    <p>
        This function makes the dictionary containing all information from the states.
    </p>
    <li>add_non_nested_predicate(predicate, predicate_name, visualization_dic, t)</li>
    <p>
        This function adds a non nested predicate to the dictionary, which contains all information from the states. This
        function is also used to add nested predicates (after breaking down the nested predicate in the overarching predicate
        and the "regular" predicate).
    </p>
    <li>add_predicate_visualization(agent, value, predicate_name, visual_dic, t)</li>
    <p>
        This function is a helper function for the add_non_nested_predicate function. It shapes the key-value pair per
        predicate.
    </p>
    <li>check_completeness(visual_dic, StateMachine)</li>
    <p>
        This function checks the completeness of the dictionary, which contains all information from the states. If values
        are missing for timesteps, None is filled in.
    </p>
    <li>retrieve_nested_sort(StateMachine, nested_pred)</li>
    <p>
        This function retrieves the sort of a nested predicate, in order to determine which graph should be made.
    </p>
    <li>make_type_of_plot_dic(StateMachine, visualization_dic)</li>
    <p>
        This function makes a dictionary containing information about which type of plot is created for each predicate.
    </p>
    <li>make_numerical_plot(predicate_name, predicates)</li>
    <p>
        This function creates a numerical plot for the predicate with name *predicate_name* (*predicates* contains the
        information to plot).
    </p>
    <li>make_bar_plot(predicate_name, predicates, sort, sorts)</li>
    <p>
        This function creates a bar plot for the predicate with name *predicate_name* (*predicates* contains the
        information to plot, and *sort* and *sorts* are used to create the legend).
    </p>
    <li>make_bar_plot_list(predicate_name, predicates)</li>
    <p>
        This function creates a bar plot for the predicate with name *predicate_name* (*predicates* contains the
        information to plot). This function is different from the make_bar_plot function, since there are multiple values
        per predicate.
    </p>
    <li>visualize(visualization_dic, type_of_plot_dic, sorts)</li>
    <p>
        This function creates a plot for each predicate in the visualization_dic, based on the type_of_plot_dic and sorts.
    </p>
    <li>run_visualization(StateMachine, predicate_to_remove=None)</li>
    <p>
        This is the main function to call. The StateMachine should be passed, the predicate_to_remove argument is optional.
    </p>
</ul>