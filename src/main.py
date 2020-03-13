import numpy as np

# modules
from epidemic_model_1 import Epidemic

def main():
    e = Epidemic(1000, 0.05) # 1000 people, 5 percent infect rate
    # print('connection matrix: ', e._connections)
    e.process_model(100) # process model through 100 iterations

if __name__ == '__main__':
    main()