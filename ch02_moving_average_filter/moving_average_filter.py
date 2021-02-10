from scipy import io
import matplotlib.pyplot as plt
import numpy as np

input_mat = io.loadmat('ch02_moving_average_filter/SonarAlt.mat');

def get_sonar(i):
    return input_mat['sonarAlt'][0][i];

class MOVAVG_Filter:
    def __init__(self,sample_num=10):
        self.sample_num = sample_num;
        self.n = np.ones(self.sample_num);
        self.count = 0;
    
    def filter(self,x):
        if self.count == 0:
            self.n *=x;
        self.count += 1;
         
        # data shift
        for data_index_ in range(self.sample_num-1):
            self.n[data_index_] = self.n[data_index_+1];
        self.n[-1] = x;

        return self.n.mean();

sample = 500;

mov_avg_filter = MOVAVG_Filter(sample_num=10);
x_meas  = [get_sonar(i) for i in range(sample)];
x_avg  = [mov_avg_filter.filter(get_sonar(i)) for i in range(sample)];

plt.plot(x_meas, 'r*', label='Measure');
plt.plot(x_avg,'b-',label = 'Moving average');
plt.xlabel("time [sec]");
plt.ylabel("Altitude [m]");
plt.show();
plt.close();
#