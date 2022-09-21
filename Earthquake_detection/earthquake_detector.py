from asyncio.windows_events import NULL
import numpy as np

class EarthquakeDetector:
    old_seismograph_roc;
    def __init__(self,
                seismograph_count, 
                sample_rate_hz,
                alert_callback):

        """
        Steps for earthquake detection
        1. Loop through every seismograph
        2. compare the slope of the previous x amount of points (called old_seismograph_roc) with the new derivative
        3. Set a flag (called possibly_earthquake) to true
        4. If all the detectors have set their flags to true, trigger the alert
        """
        if old_seismograph_roc == NULL:
            old_seismograph_roc = np.full((seismograph_count, 10), None)

        setpoints = False
        new_seismograph_roc = None

        """
        This threshold should be changed based on how often we want the earthquake detector to provide alerts - should be done with testing.
        I have set it to 3 temporarily.
        """
        threshold = 3 
        possibly_earthquake = np.full(seismograph_count, False)
        """
        Args: 
            seismograph_count: the number of seismographs in the detector network.
            sample_rate_hz: the sample rate of the seismograph.
            alert_callback: a callback function if an earthquake is detected.
        """

        for i in range(seismograph_count):
            new_datapoints = new_samples(i)
            old_seismograph_roc[i][0] = (new_datapoints[1] - new_datapoints[0])/sample_rate_hz
            for j in range(new_datapoints)-1:
                old_seismograph_roc[i][j] = new_datapoints[j] - new_datapoints[j-1] / sample_rate_hz
                if old_seismograph_roc[i][j] > threshold*old_seismograph_roc[i][j-1]:
                    possibly_earthquake[i] = True
                else:
                    old_seismograph_roc[i][j-1] = old_seismograph_roc[i][j]
            
                
        
        if possibly_earthquake.all() == True:
            alert_callback()

        pass

    def new_samples(self, seismograph_id, samples):
        """I have made an assumption that calling this function provides me with the samples I need for my seismograph"""

        """New samples are available for a seismograph.

        Args: 
            seismograph_id: the zero-indexed seismograph id.
            samples: an ndarray of integer samples.
        """
        pass