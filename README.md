# UTEasy
Used for viewing and analyzing ultrasonic signals from '.txt' files of the specified format.
This is a remake of the same analysis tools that were made in Matlab.
Specifically this is for ultrasonic signals from the Acquisition Logic ALGTe1.0x 1GHz digitizer.
Files need to be in the for seen in the Ultrasonic Signal file to work properly.

## Set Signal Smoothing
You can choose to view the ultrasonic signal as-is, or smoothed.
Smoothing is implemented with a zero-phase, backwards-forwards filter.
Press "Smoothing: On/Off" to toggle the smoothing state.


## Isolate an Echo and Find the Fourier Transform
Using the graph window's native zoom features allows you to zoom into a specific region on the signal.
Press 'Calculate FT' to apply a fast-Fourier Transform to that region and to view the power spectrum.


## Set Signal Filtering and Zero-Padding
You can filter the specified signal region using a hamming filter before calculating the Fourier Transform.
Filtering the signal helps reduce spectral leakage, which is the tendancy of a Fourier transform to spread the power spectrum.
Press "FT Filtering: On/Off" to toggle the filtering state.
Zero-padding can also be changed, causing an increase in frequency density for the Fourier transform.
Press "Zero-Padding: On/Off to change the zero padding state.
Beware, zero-padding increases the density of the signal, but may not represent the 'true' signal state.


