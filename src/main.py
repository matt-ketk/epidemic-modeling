import numpy as np

# modules
from epidemic_model_1 import Epidemic
from record import Record
def main():
    e = Epidemic(10000, 0.05) # 1000 people, 5 percent infect rate
    r = Record()
    e.process_model(50, r) 
    r.display_data()

if __name__ == '__main__':
    main()