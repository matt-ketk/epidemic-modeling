import numpy as np
import matplotlib.pyplot as plt
# modules

class Record:
    def __init__(self):
        self.amount_infected = np.array([])
        self.connection_frequency = np.array([])
        # add more later

    def display_data(self):
        if self.amount_infected.size == 0 or self.connection_frequency.size == 0:
           print('Record is empty!') 
        else:
            # plt.subplot(1,2,1)
            plt.scatter(
                np.arange(0,self.amount_infected.size),
                self.amount_infected
            )
            plt.xlabel('Days Passed')
            plt.ylabel('# of People Infected')
            plt.title('Progression of Infection: Model 1')
            plt.show()