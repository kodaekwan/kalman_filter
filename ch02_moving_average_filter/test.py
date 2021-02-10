from scipy import io
import matplotlib.pyplot as plt
import numpy as np

input_mat = io.loadmat('ch02_moving_average_filter/SonarAlt.mat');

def get_sonar(i):
    return input_mat['sonarAlt'][0][i];

def mov_avg_filter(x_n, x_meas):

    n = len(x_n);
    for i in range(n-1):
        x_n[i] = x_n[i+1];
    x_n[n-1] = x_meas;

    x_avg = np.mean(x_n);
    return x_avg, x_n;


n = 10;
n_samples = 500;
time_end = 10;

dt = time_end / n_samples
time = np.arange(0, time_end, dt)
x_meas_save = np.zeros(n_samples);
x_avg_save = np.zeros(n_samples);

for i in range(n_samples):
    x_meas = get_sonar(i);

    if i == 0:
        x_avg, x_n = x_meas, x_meas * np.ones(n);
    else:
        x_avg, x_n = mov_avg_filter(x_n,x_meas);
    
    x_meas_save[i] = x_meas;
    x_avg_save[i] = x_avg;

plt.plot(time, x_meas_save, 'r*', label='Measure');
plt.plot(time,x_avg_save,'b-',label = 'Moving average');
plt.xlabel("time [sec]");
plt.ylabel("Altitude [m]");
plt.show()

# data = [get_sonar(i) for i in range(500)]


# plt.plot(data,label = 'Sonar_raw')
# plt.legend()
# plt.show()
# print()