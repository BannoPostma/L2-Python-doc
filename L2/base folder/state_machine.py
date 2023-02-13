""" state_machine.py
    The state_machine is the force behind creating and defining each state
    """

from state import Predicate
from state import State
from visualization import run_visualization
import re


class StateMachine:
    def __init__(self, predicates, sorts, scenario, max_t, rules):
        """
            scenario = the scenario defined by the user
            max_t = the maximum time step the StateMachine will run to
            states = pre-made list of empty states
        """
        self.max_t = max_t
        self.rules = rules
        self.predicates = self.create_predicate_dict(predicates)
        self.sorts = self.sort_sorts(sorts)
        self.states = self.create_states()
        self.fill_states(scenario)

    @staticmethod
    def filter_predicate_sorts(predicate):
        """
            retrieve the values the sort can have
        """
        predicate = re.search("{([^}]+)}", predicate)
        predicate_sorts = predicate.group(1).split(",")
        predicate_sorts = [value.strip() for value in predicate_sorts]
        return predicate_sorts

    def create_predicate_dict(self, predicates):
        """
            create a dictionary for the predicates from the predicates file
        """
        predicates = open(predicates, "r").read().splitlines()
        predicates = [line for line in predicates if line != ""]
        predicate_dic = {}
        for predicate in predicates:
            predicate = predicate.split(";")
            predicate_name = predicate[0]
            predicate_sorts = self.filter_predicate_sorts(predicate[1])
            predicate_dic[predicate_name] = predicate_sorts
        return predicate_dic

    @staticmethod
    def filter_sort_values(sort):
        """
            retrieve the values the sort can have
        """
        sort = re.search("{([^}]+)}", sort)
        sort_values = sort.group(1).split(",")
        sort_values = [value.strip() for value in sort_values]
        return sort_values

    def sort_sorts(self, sorts):
        """
            create a dictionary of sorts from the sorts file
        """
        sorts = open(sorts, "r").read().splitlines()
        sorts = [line for line in sorts if line != ""]
        sorts_dic = {}
        for sort in sorts:
            sort = sort.split(";")
            sort_name = sort[0]
            sort_values = self.filter_sort_values(sort[1])
            sorts_dic[sort_name] = sort_values
        return sorts_dic

    def create_states(self):
        """
            create "max_t" number of empty states
            State(i + 1), because it ranges from 0 - max_t, but states start from 1
        """
        states = []
        for i in range(self.max_t):
            states.append(State(i + 1, self.predicates, self.sorts))
        return states

    def check_validity_pred(self, predicate_name, agent, value):
        """
            check the validity of the predicate, based on the predicate name and the sorts
        """
        if predicate_name[0] not in self.predicates:
            print("The predicate \"%s\" is not a valid predicate (when loading the scenario file)." % predicate_name)
            print("The valid predicates are: ", end="")
            print(", ".join(self.predicates))
            return
        if len(predicate_name) > 1:
            # check which sorts should be in the nested predicate (to check for the agents)
            sorts_of_pred = self.predicates[predicate_name[-1]]
            if predicate_name[-1] not in self.predicates:
                print(
                    "The predicate \"%s\" is not a valid predicate within the predicate %s (when loading the scenario"
                    " file)." % (predicate_name[-1], predicate_name[0]))
                print("The valid predicates are: ", end="")
                print(", ".join(self.predicates))
                return
        else:
            sorts_of_pred = self.predicates[predicate_name[0]]
        # check validity agents
        for i in range(len(agent)):
            if sorts_of_pred[i] != "AGENT":
                print("Expected sort: AGENT, got sort: sort %s, for predicate %s on place %d, "
                      "when loading the scenario file" % (sorts_of_pred[i], predicate_name, i + 1))
            elif agent[i] not in self.sorts[sorts_of_pred[i]]:
                print("Agent %s does not seem to exist in the AGENT sorts, when loading the scenario file" % agent[i])
        if len(predicate_name) == 1:
            # check validity value of the sort (only if it is not nested)
            if sorts_of_pred[-1] == "BOOLEAN":
                if type(value) != bool:
                    print("Expected sort: BOOLEAN, got a different sort (with value %s), for predicate %s, "
                          "when loading the scenario file" % (value, predicate_name))
            elif sorts_of_pred[-1] == "REAL":
                if not ((type(value) == int) ^ (type(value) == float)):
                    print("Expected sort: REAL, got a different sort (with value %s), for predicate %s, "
                          "when loading the scenario file" % (value, predicate_name))
            elif value not in self.sorts[sorts_of_pred[-1]]:
                print("Expected sort: %s, got a different sort (with value %s), for predicate %s, "
                      "when loading the scenario file" % (sorts_of_pred[-1], value, predicate_name))

    def fill_states(self, scenario):
        """
            fill states based on solely the scenario file
        """
        scenario = open(scenario, "r").read().splitlines()
        scenario = [line for line in scenario if line != ""]
        for predicate in scenario:
            predicate = predicate.split(";")
            time_steps = predicate[-1]
            predicate = predicate[0]
            if predicate[-2:] == "}}":
                predicate, agent, value = self.filter_nested_predicate_info(predicate)
            else:
                predicate, agent, value = self.filter_predicate_info(predicate)
            start_time, end_time = self.filter_predicate_time(time_steps)
            self.check_validity_pred(predicate, agent, value)
            self.insert_predicate(predicate, agent, value, start_time, end_time)

    def show_debug_info(self):
        """
            print debug information (defined sorts & defined predicates)
        """
        print("##################Debug mode activated##################")
        print("The StateMachine contains the following defined sorts, besides BOOLEAN and REAL: ")
        print("\t" + ", ".join(self.sorts) + "\n")
        print("The StateMachine contains the predicates with their corresponding sorts: ")
        for predicate in self.predicates:
            print("\tPredicate name: %s, predicate sorts (index dependent): " % predicate, end="")
            print(self.predicates[predicate])
        print("##################Debug report per state##################\n")

    def run(self, debug_mode=False):
        """
            run all rules that are inside the rules.py file
        """
        if debug_mode:
            self.show_debug_info()
            self.states[0].show_info()
        for t in range(1, self.max_t):
            # execute all rules and create all predicates for state t
            for rule in self.rules:
                rule(self.states[:t + 1], t)
            if debug_mode:
                self.states[t].show_info()

    def filter_nested_predicate_info(self, predicate):
        """
            filters predicate information from a predicate from the scenarios file
        """
        predicate_re = re.search("{([^}]+)}", predicate)
        predicate_re = predicate_re.group(1).split(",")
        # delete whitespaces in names of agents in case of multiple agents
        agent_and_value = [inf.strip() for inf in predicate_re]
        nested_pred = agent_and_value[0].split("{")[0]
        # agents are till the last item
        agent_and_value[0] = agent_and_value[0].split("{")[1]
        agents = [agent for agent in agent_and_value if agent in self.sorts["AGENT"]]
        values = [value for value in agent_and_value if value not in agents]
        agents = [agent.strip() for agent in agents]
        name_predicate = predicate.split("{")[0]
        # if the value is a boolean / real number, make it a float, in order to use it in the rules
        for i in range(len(values)):
            try:
                values[i] = float(values[i])
            except ValueError:
                # check if the value is a Boolean. If so --> change it
                if values[i].lower() == "true":
                    values[i] = True
                elif values[i].lower() == "false":
                    values[i] = False
        name_predicate = [name_predicate, nested_pred]
        if len(values) == 1:
            values = values[0]
        return [name_predicate, agents, values]

    @staticmethod
    def filter_predicate_info(predicate):
        """
            filters predicate information from a predicate from the scenarios file
        """
        predicate_re = re.search("{([^}]+)}", predicate)
        predicate_re = predicate_re.group(1).split(",")
        # delete whitespaces in names of agents in case of multiple agents
        agent_and_value = [inf.strip() for inf in predicate_re]
        # agents are till the last item
        agents = agent_and_value[:-1]
        agents = [agent.strip() for agent in agents]
        # value is the last item
        values = agent_and_value[-1].split()
        name_predicate = predicate.split("{")[0]
        # if the value is a boolean / real number, make it a float, in order to use it in the rules
        for i in range(len(values)):
            try:
                values[i] = float(values[i])
            except ValueError:
                # check if the value is a Boolean. If so --> change it
                if values[i].lower() == "true":
                    values[i] = True
                elif values[i].lower() == "false":
                    values[i] = False
        name_predicate = [name_predicate]
        if len(values) == 1:
            values = values[0]
        return [name_predicate, agents, values]

    def filter_predicate_time(self, time):
        """
            filters predicate duration from a predicate from the scenarios file
            start_time = start_time - 1, since index starts from 0
        """
        time = time.split("[")
        time = (time[1].split("]"))[0]
        if len(time) == 1:
            # just 1 time point
            start_time, end_time = int(time[0]) - 1, int(time[0])
        else:
            # range of time points
            time = time.split(":")
            start_time = int(time[0]) - 1
            if time[-1].lower() == "inf":
                end_time = self.max_t
            else:
                end_time = int(int(time[-1]))
        return [start_time, end_time]

    def insert_single_predicate(self, predicate, agent, value, start_time, end_time):
        for i in range(start_time, end_time):
            # single predicate
            if predicate in self.states[i].predicates:
                # if the key is already in the dictionary, add a list of the agent + value to the key
                self.states[i].predicates[predicate].append(Predicate(predicate, agent, value))
            else:
                # if the key is not in the dictionary, create a list and add a list of the agent + value to the key
                self.states[i].predicates[predicate] = [Predicate(predicate, agent, value)]

    def insert_nested_predicate(self, nest_name, agent, value, start_time, end_time):
        nested_pred = nest_name[0]
        predicate_name = nest_name[-1]
        to_add_pred = Predicate(predicate_name, agent, value)
        for i in range(start_time, end_time):
            if nested_pred in self.states[i].predicates:
                if predicate_name in self.states[i].predicates[nested_pred]:
                    self.states[i].predicates[nested_pred][predicate_name].append(to_add_pred)
                else:
                    self.states[i].predicates[nested_pred][predicate_name] = [to_add_pred]
            else:
                self.states[i].predicates[nested_pred] = {}
                self.states[i].predicates[nested_pred][predicate_name] = [to_add_pred]

    def insert_predicate(self, predicate, agent, value, start_time, end_time):
        """
            insert the predicate to the corresponding states
        """
        sorts_of_pred = self.predicates[predicate[0]]
        if sorts_of_pred[-1] != "PREDICATE":
            self.insert_single_predicate(predicate[0], agent, value, start_time, end_time)
        else:
            self.insert_nested_predicate(predicate, agent, value, start_time, end_time)