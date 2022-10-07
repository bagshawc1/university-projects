def repeat_test(arr, state):
    for x in arr:

        if state['left'] == x['left'] and state['right'] == x['right'] and state['boat'] == x['boat']:

            return True
    return False


def check_safe(numbers_sent, state):
    # checks to see if next state would be valid
    if state['boat'] == 0:
        if (state['left'][0] - numbers_sent[0] > state['left'][1] - numbers_sent[1] and state['left'][1] - numbers_sent[1] > 0) \
                or (state['right'][0] + numbers_sent[0] > state['right'][1] + numbers_sent[1] and state['right'][1] + numbers_sent[1] > 0)\
                or state['left'][0] - numbers_sent[0] < 0 or state['left'][1] - numbers_sent[1] < 0:
            return False
        else:
            return True
    else:
        if (state['left'][0] + numbers_sent[0] > state['left'][1] + numbers_sent[1] and state['left'][1] + numbers_sent[1] > 0) \
                or (state['right'][0] - numbers_sent[0] > state['right'][1] - numbers_sent[1] and state['right'][1] - numbers_sent[1] > 0)\
                or state['right'][0] - numbers_sent[0] < 0 or state['right'][1] - numbers_sent[1] < 0:
            return False
        else:
            return True


def goal_test(state):
    if state['right'] == [3,3]:
        return True
    else:
        return False


class Problem:
    # actions
    def send_cannibal(self, number, state):
        action_path = state['action_path'] + ['Sent ' + str(number) + ' Cannibal(s)']
        if not check_safe([number, 0], state):
            return False
        if state['boat'] == 0:
            if state['left'][0] < number:
                return False
            left = [state['left'][0] - number, state['left'][1]]
            right = [state['right'][0] + number, state['right'][1]]
            boat = 1
            return {
                "left": left,
                "right": right,
                "boat": boat,
                "action_path": action_path
            }

        else:
            if state['right'][0] < number:
                return False
            right = [state['right'][0] - number, state['right'][1]]
            left = [state['left'][0] + number, state['left'][1]]
            boat = 0
            return {
                "left": left,
                "right": right,
                "boat": boat,
                "action_path": action_path
            }

    def send_missionary(self, number, state):
        action_path = state['action_path'] + ['Sent ' + str(number) + ' Missionary(s)']
        if not check_safe([0, number], state):
            return False
        if state['boat'] == 0:
            if state['left'][1] < number:
                return False
            left = [state['left'][0], state['left'][1] - number]
            right = [state['right'][0], state['right'][1] + number]
            boat = 1
            return {
                "left": left,
                "right": right,
                "boat": boat,
                "action_path": action_path
            }

        else:
            if state['right'][1] < number:
                return False
            right = [state['right'][0], state['right'][1] - number]
            left = [state['left'][0], state['left'][1] + number]
            boat = 0
            return {
                "left": left,
                "right": right,
                "boat": boat,
                "action_path": action_path
            }

    def send_both(self, state):
        action_path = state['action_path'] + ['Sent one Cannibal and one Missionary']
        if not check_safe([1,1], state):
            return False
        if state['boat'] == 0:
            if state['left'][0] < 1 or state['left'][1] < 1:
                return False
            left = [state['left'][0] - 1, state['left'][1] - 1]
            right = [state['right'][0] + 1, state['right'][1] + 1]
            boat = 1
            return {
                "left": left,
                "right": right,
                "boat": boat,
                "action_path": action_path
            }

        else:
            if state['right'][0] < 1 or state['right'][1] < 1:
                return False
            right = [state['right'][0] - 1, state['right'][1] - 1]
            left = [state['left'][0] + 1, state['left'][1] + 1]
            boat = 0
            return {
                "left": left,
                "right": right,
                "boat": boat,
                "action_path": action_path
            }

    def send_one_cannibal(self, state):
        return self.send_cannibal(1, state)

    def send_two_cannibal(self, state):
        return self.send_cannibal(2, state)

    def send_one_missionary(self, state):
        return self.send_missionary(1, state)

    def send_two_missionary(self, state):
        return self.send_missionary(2, state)


def breadth_first_search(problem):
    initial_state = {
        'left': [3, 3],
        'right': [0, 0],
        'boat': 0,
        'action_path': []
    }
    node = initial_state
    possible_moves = [problem.send_one_cannibal, problem.send_two_cannibal,
                      problem.send_one_missionary, problem.send_two_missionary, problem.send_both]

    fringe = list()
    explored = list()
    explored.append(node)

    # build fringe
    for func in possible_moves:
        temp_node = func(node)
        if temp_node:
            fringe.append(temp_node)
    while len(fringe) > 0:
        node = fringe.pop(0)
        explored.append(node)
        for func in possible_moves:
            child = func(node)
            if child and not repeat_test(explored, child) and not repeat_test(fringe, child):
                if goal_test(child):
                    print('found the solution!')
                    print('Order of moves:')
                    for i in child['action_path']:
                        print(i)
                    print(' ')
                    print('Final State:')
                    print(child)
                    return
                fringe.append(child)


prob = Problem()
breadth_first_search(prob)



