from coin import Coin


class Experiment:
    def flip_coin_x_times(self, x):
        # returns the probability of HEAD
        c = Coin()
        return sum((c.flip() for _ in range(x))) / x

    def flip_coin_2x_ntimes(self, n):
        c = Coin()
        experiments = [sum([c.flip(), c.flip()]) == 2 for _ in range(n)]
        return sum(experiments) / n

    def flip_coin_5x_ntimes(self, n, success):
        c = Coin()
        experiments = [([c.flip(), c.flip(), c.flip(), c.flip(), c.flip()]
                        == success) for _ in range(n)]

        print(experiments)
        return sum(experiments) / n

    def flip_coin_with_pattern_n_time(self, pattern, n, flips):
        c = Coin()
        experiments = [[c.flip() for f in range(flips)]
                       == pattern for e in range(n)]
        return sum(experiments) / n
