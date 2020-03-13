import numpy as np
# modules
def random_connection(population, connection_frequency=0.01):
    # output graph adjacency matrix with random connections
    # does not model community aspect of human interactions
    # connections = np.random.randint(0,2,size=(population, population))
    connections = np.random.choice(
        2,
        (population, population),
        p=[1-connection_frequency, connection_frequency]
    )
    np.fill_diagonal(connections, 0) # person cannot infect him/herself
    return connections

def initiate_random(population, initial=5):
    # randomly infects matrix of zeros into ones
    # returns matrix with amount initial infected in random places
    infect_list = np.zeros(population)
    # print(initial)
    for _ in range(int(initial)):
        infect_list[np.random.randint(0,population)] = 1
        # print('amount infected: ', infect_list[infect_list==1].size)
        # print(infect_list==1)

    return infect_list

def iterate_model(infect_list, connect_mat, infect_rate):
    # takes popul_mat, connect_mat, and infect_rate
    # compute next iteration of infection
    connections = np.where(connect_mat==1)
    # print(connections)
    # print(np.where(connect_mat==1)) # LAST LEFT OFF HERE 3/13/2020
    # np.where(infect_list==1) # return the number persons infected
    infected = np.isin(connections[0], np.where(infect_list==1))
    # print('infected persons #: ',np.where(infect_list==1))
    # print(infected)
    
    new_infected = connections[1][infected][np.random.random(connections[1][infected].size) < infect_rate]
    infect_list[new_infected] = 1
    return connections[0] # return frequency of connections

# classes
class Epidemic:
    def __init__(self, population, infect_rate):
        self.population = population
        self.infect_rate = infect_rate
        self._infect_list = initiate_random(self.population)
        self._connections = random_connection(self.population)
    
    def amount_infected(self):
        return self._infect_list[self._infect_list==1].size


    def process_model(self, num_iterations):
        print('initial infected: ', self.amount_infected())
        for _ in range(num_iterations):
            iterate_model(
                self._infect_list,
                self._connections,
                self.infect_rate
            )
            print(
                'currently infected: ',
                self.amount_infected() 
            )


