'''

"Why does distribution change with the increase in the number of runs for a single trial?"

    Distribution changes because when we increase the number of runs for a trial it tends
    to appropriate to the initial probability. So for a small number of runs the distribution
    will be far away from real value, but increasing runs will give us more exact answer.

'''


import getopt
import random
import sys


class Automaton:

    def __init__(self, matrix, init_state):
        self.matrix = matrix
        self.init_state = init_state
        self.current_state = init_state

    # Define step() function to move from one state to another
    def step(self):
        row = self.matrix[self.current_state]
        rnd = random.random()
        for i in range(len(row)):
            if rnd <= row[i]:
                self.current_state = i
                return
            else:
                rnd -= row[i]

    # Define run() function to run I times, each run consisting of S steps
    def run(self, steps):
        self.current_state = self.init_state
        for i in range(steps):
            self.step()
        return self.current_state

    # Define find_probability() function for computing probability of observing string given the transition matrix
    def find_probability(self, string):
        probability = 1.0
        self.current_state = int(string[0])
        for i in range(1, len(string) - 1):
            probability *= self.matrix[self.current_state][int(string[i])]
        return probability


def main(argv):

    # command line arguments
    input_file_path = ''
    output_file_path = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file_path = arg
        elif opt in ("-o", "--ofile"):
            output_file_path = arg

    # parsing file_input
    file_input = open(input_file_path, "r")
    file_output = open(output_file_path, "w")
    file_output.write("vi.rotaru@innopolis.ru\n")
    t = int(file_input.readline())  # number of test cases
    for i in range(t):
        q = int(file_input.readline())  # set of states in the automaton
        # Initializing the array of states
        array = [0] * q
        # fill in the array of states with the associated probabilities
        for k in range(q):
            array[k] = [0] * q
        for j in range(q):
            line_items = file_input.readline().split(",")
            for k in range(q):
                array[j][k] = float(line_items[k])
        q0 = int(file_input.readline())  # initial state
        I = int(file_input.readline())  # number of runs to perform
        simulations = file_input.readline().split(",")
        steps = int(file_input.readline())  # number of steps
        atm = Automaton(array, q0)
        for j in range(I):
            runs = int(simulations[j])
            results = [0] * q
            for k in range(runs):
                last_state = atm.run(steps)
                results[last_state] += 1
            for k in range(q):
                file_output.write(str(1.0 * results[k] / runs))
                if k < q - 1:
                    file_output.write(", ")
            file_output.write("\n")
        l = int(file_input.readline())  # number of test strings
        for j in range(l):
            test_string = file_input.readline()  # test strings
            # computing the probability of observing the string given the transition matrix
            probability = atm.find_probability(test_string)
            file_output.write(str(probability) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
