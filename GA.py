from population import *

class GA(object):

    def solve(self,
              test_instance,
              pop_size,
              niche_method,
              gen_no):

        population = Population(pop_size,test_instance)

        for i in xrange(gen_no):
            print i
            niche_method(population)
        sorted_pop = sorted(population.MEMBERS, key = lambda x: x.subsets_fitness)
        print test_instance.U-set.union(*sorted_pop[0].subsets_chosen)


