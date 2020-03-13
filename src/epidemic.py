import numpy as np

# modules
def random_connection(population):
    # output graph adjacency matrix with random connections
    # does not model community aspect of human interactions
    connections = np.random.randint(0,2,size=(population, population))
    return np.fill_diagonal(connections, 0) # person cannot infect him/herself

def initiate_random(population, infect_rate, initial=5):
    # randomly infects matrix of zeros into ones
    # returns matrix with amount initial infected in random places
    infect_list = np.zeros(population)
    for _ in range(initial):
        infect_list[np.random.randint(0,population) > infect_rate] = 1

    return infect_list

def iterate_model(infect_list, connect_mat, infect_rate):
    # takes popul_mat, connect_mat, and infect_rate
    # compute next iteration of infection
    connections = np.where(connect_mat==1)
    print(np.where(connect_mat==1)) # LAST LEFT OFF HERE 3/13/2020
    # new_infected = connections[1][np.random.random(connections[1].size) > infect_rate]
    infect_list[new_infected] = 1
    return connections[0] # return frequency of connections

class Epidemic:
    def __init__(self, population, infect_rate):
        self.population = population
        self.infect_rate = infect_rate
        self.__infect_list = initiate_random(self.population, self.infect_rate)
        self.__connections = random_connection(self.population)
    
    def amount_infected(self):
        return self.__infect_list[self.__infect_list==1].size


    def process_model(self, num_iterations):
        for _ in range(num_iterations):
            iterate_model(
                self.__infect_list,
                self.__connections,
                self.infect_rate
            )
            print(
                'currently infected: ',
                self.amount_infected() 
            )


