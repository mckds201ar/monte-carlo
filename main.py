# for testing the methods

from experiment import Experiment

e = Experiment()
answer = e.flip_coin_5x_ntimes(10000, [0, 1, 0, 1, 1])
print(answer)
