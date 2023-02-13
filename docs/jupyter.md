Jupyter Notebook
================

<p>
    The Jupyter Notebook is the file that you should edit. In this file, you both do the theoretical part of the
    assignment, as well as the programming part of the assignment. After doing assignment 3, you should be able to
    program parts of the code yourself. The theoretical part speaks for itself. A short elaboration on the programming
    part of the assignment will be given below.
</p>

## Elaboration on the programming part of the assignment
<p>
    Most of the information about the programming part is already in the Jupyter Notebook itself. However, to give you
    something to go on, the sequence and different parts will be shortly discussed.
</p>

<h3>Imports</h3>
<p>
    Before you start coding, you have to run the cell with the imports. You will get errors if you do NOT do this...
</p>

<h3>Sorts</h3>
<p>
    Before you define any sorts, you should write the line "%%writefile sorts.txt" (this should already be there). After
    writing this line, you should define a sort per line, using the manner described <a href="../text_files/">here</a>.
</p>

<h3>Predicates</h3>
<p>
    Before you define any predicate, you should write the line "%%writefile sorts.txt" (this should already be there). After
    writing this line, you should define a predicate per line, using the manner described <a href="../text_files/">here</a>.
</p>

<h3>Scenario</h3>

<p>
    Before you define any predicate, you should write the line "%%writefile scenarios.txt" (this should already be there). After
    writing this line, you should define a predicate per line, using the manner described <a href="../text_files/">here</a>.
</p>

<h3>Rules</h3>
<p>
    Please create one rule per code cell (in order to keep the overview). In addition, it is highly suggested to have a
    Markdown cell before each code cell, describing the rule you are writing. <br><br>
    When you are done writing the rules, please make a list, called "rules" and add the name of the rules (NOT as strings)
    to this list.
</p>

<h3>Run</h3>

<p>
    First, import the StateMachine Class and run_visualization function. Next, define a MAX_T, and define the name of the
    .txt files for the scenario, predicates, and sorts file. Hereafter, initialize the Statemachine:
    StateMachine = StateMachine(predicates, sorts, scenario, MAX_T, rules). Please note that the predicates, sorts, and scenario
    arguments are Strings, containing the names of the .txt files. <br><br>
    To run the StateMachine, simply perform the .run() function --> StateMachine.run(). If you want to enable Debug mode:
    StateMachine.run(True). <br><br>
    To run the visualization, simply run the run_visualization function and add the StateMachine as argument -->
    run_visualization(StateMachine). If you want to exclude any predicate from the visualization, you should add a list
    as argument, containing the names of the predicates. For example --> run_visualization(StateMachine, ["has_age",
    "belief_like_carrot"]).
</p>
