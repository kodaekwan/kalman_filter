import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)


def get_volt():
    "Measure voltage"
    noise = np.random.normal(0,4);  # v         : measurement noise
    volt_mean = 14.4                # volt_mean : mean (nominal) voltage
    return volt_mean + noise        # return measure voltage

class AVG_filter():
    def __init__(self):
        self.x_avg = 0;
        self.k = 1;
    def filter(self,x_meas):
        alpha   = (self.k - 1) / self.k;
        self.k  += 1; 
        self.x_avg = alpha * self.x_avg + (1 - alpha) * x_meas;
        return self.x_avg

class LOWPASS_filter():
    def __init__(self,gain=0.9):
        self.x_avg = 0;
        self.alpha = gain;
        self.k = 1;
    def filter(self,x_meas):
        if self.k == 1:
            self.x_avg = x_meas;
            self.k += 1;
            return self.x_avg;
        self.x_avg = self.alpha * self.x_avg + (1 - self.alpha) * x_meas;
        return self.x_avg



avg = AVG_filter();
lpf = LOWPASS_filter(0.99);

meas = [];
filt = [];
filt2 = [];

for i in range(1000):
    x_measure = get_volt();
    x_filter  = avg.filter(x_measure);
    x_filter2  = lpf.filter(x_measure);
    meas.append(x_measure);
    filt.append(x_filter);
    filt2.append(x_filter2);
    print(x_measure , x_filter,x_filter2);


plt.plot(meas, 'r*', label='Measured')
plt.plot(filt, 'b-', label='Average')
plt.plot(filt2, 'g-', label='LOWPASS')


plt.show();