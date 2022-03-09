"""ex2"""


def machineEpsilon(func=float):
    machine_epsilon = func(1)
    machine_epsilon_last = 0.0
    while func(1) + machine_epsilon != func(1):
        machine_epsilon_last = machine_epsilon
        machine_epsilon = func(machine_epsilon) / func(2)
    return machine_epsilon_last


print(machineEpsilon())

"""ex3"""
print(abs(3.0 * (4.0 / 3.0 - 1) - 1))

"""ex4"""
x = abs(3.0 * (4.0 / 3.0 - 1) - 1)
if x - machineEpsilon() <= 0:
    x = 0
print(x)
