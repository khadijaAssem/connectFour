from tree import plot
from gameAlgorithm import game


class Minimax_Class:

    def __init__(self, num_row, num_col, k_levels, opponent, agent, default):
        # assume index from 0 to < n.
        self.num_row = num_row
        self.num_col = num_col
        self.opponent = opponent #'2'
        self.agent = agent #'1'
        self.default = default
        self.max_value = 10000
        self.min_value = -10000
        self.alpha = -10000
        self.beta = 10000
        self.k_levels = k_levels
        self.evaluation = game(num_row, num_col, opponent, agent, default)
        return

    def replace_char_at_index(self, org_str, index, replacement):
        ''' Replace character at index in string org_str with the
        given replacement character.'''
        new_str = org_str
        if index < len(org_str):
            new_str = org_str[0:index] + replacement + org_str[index + 1:]
        return new_str

    def printer(self, state):
        for i in range (self.num_row):
            temp = ""
            for j in range(self.num_col):
                temp += state[j+i*self.num_col]
            print(temp)
        print("\n")

    def expand_children(self, state, lastRow, is_agent):
        children_list = []
        for i in range((self.num_col - 1), -1, -1):
            j = abs(int(lastRow[i]) - self.num_row + 1)
            if(j < self.num_row and state[j*self.num_col + i] == self.default):
                new_state = state[:]
                if (is_agent):  # in this step agent is play.
                    new_state = self.replace_char_at_index(new_state, j*self.num_col + i, self.agent)
                    lastRow = lastRow[0:i] + str(int(lastRow[i]) + 1) + lastRow[i + 1:] 
                else:
                    new_state = self.replace_char_at_index(new_state, j*self.num_col + i, self.opponent)
                    lastRow = lastRow[0:i] + str(int(lastRow[i]) + 1) + lastRow[i + 1:] 
                children_list.append((new_state,(j,i),lastRow))
        return children_list

    def evaluate(self, state, turn):
        # print(turn ,end = ' ')
        # self.printer(state)
        fn = self.evaluation.getHeuristic(state ,turn)
        # print(fn)
        return fn

    def getStep(self, states):
        res, row, col = self.minimax(0, 0, True, states, self.k_levels, {})
        return row, col

    # is_max : alternate between max & min levels.
    # current_depth : indicate which level we are in in each point.


    def minimax (self, current_depth, nodeIndex, is_max, states, k_levels, tree, alpha = None, beta=None):
        if alpha == None:
            alpha = self.alpha
            beta = self.beta
        # base case : targetDepth reached
        if (current_depth == k_levels):  # call Heuristic
            return self.evaluate(states[nodeIndex][0], is_max),-1,-1 #states[nodeIndex] Call heuristic with state states[nodeIndex][0]
        i = j = 0

        if (is_max):
            result_max = -10000
            new_list = self.expand_children(states[nodeIndex][0], states[nodeIndex][2], True)

            tree[states[nodeIndex][0]] = [i[0] for i in new_list]
            num_node_prev_level = len(states)
            states.extend(new_list)
            for element in range(len(new_list)):
                x = num_node_prev_level + element
                temp_max,w,z = self.minimax(current_depth + 1, x, False, states, k_levels, tree, alpha, beta)
                if temp_max > result_max:
                    result_max = max(result_max, temp_max)
                    i,j = states[x][1]

                    alpha = max(temp_max, alpha)
                    if alpha >= beta:
                        break

            return result_max,i,j
        else:
            result_min = 10000
            new_list = self.expand_children(states[nodeIndex][0], states[nodeIndex][2], False)
            tree[states[nodeIndex][0]] = [i[0] for i in new_list]
            num_node_prev_level = len(states)
            states.extend(new_list)

            for element in range(len(new_list)):
                x = num_node_prev_level + element
                temp_min,w,z = self.minimax(current_depth + 1, x, True, states, k_levels, tree, alpha, beta)
                if temp_min < result_min:
                    result_min = min(result_min, temp_min)
                    i,j = states[x][1]

                beta = min(temp_min, beta)
                if alpha >= beta:
                    break

            return result_min,i,j