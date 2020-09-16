import numpy as np
import matplotlib.pyplot as plt
# modules

class Record:
    def __init__(self):
        self.amount_infected = np.array([])
        self.connection_frequency = np.array([])
        self.marginal_growth = np.array([])
        self.growth_factor = np.array([])
        # add more later

    def post_process(self):
        self.marginal_growth = np.diff(self.amount_infected) 
       
       # determining growth factor
        self.growth_factor = self.marginal_growth[1::] / self.marginal_growth[:-1]

    def display_data(self):
        if self.amount_infected.size == 0 or self.connection_frequency.size == 0:
           print('Record is empty!') 
        else:
            self.post_process()

            plt.subplot(2,2,1)
            # plotting the amount of people infected over time
            plt.scatter(
                np.arange(0,self.amount_infected.size),
                self.amount_infected
            )
            plt.xlabel('Days Passed')
            plt.ylabel('# of People Infected')
            plt.title('Progression of Infection: Model 1')

            plt.subplot(2,2,2)
            # plotting connection frequencies of each person
            plt.bar(
                np.arange(0,self.connection_frequency.size),
                self.connection_frequency 
            ) 
            plt.xlabel('Person #')
            plt.ylabel('# of Connections')
            plt.title('Amount of Connections per Person')

            plt.subplot(2,2,3)
            # plotting marginal growth
            plt.scatter(
                np.arange(0,self.marginal_growth.size),
                self.marginal_growth
            )
            plt.xlabel('Days Passed')
            plt.ylabel('# of New Cases')
            plt.title('New Cases per Day: Model 1')
            
            plt.subplot(2,2,4)
            # plotting growth factor
            plt.scatter(
                np.arange(0,self.growth_factor.size),
                self.growth_factor
            )
            plt.xlabel('Days Passed')
            plt.ylabel('Factor of Growth')
            plt.title('Growth Factor by Day: Model 1')

            plt.show()