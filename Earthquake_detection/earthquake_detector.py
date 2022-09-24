from asyncio.windows_events import NULL
import numpy as np

class EarthquakeDetector:
    old_seismograph_roc;
    new_datapoints;
    total_datapoints;
    def __init__(self,
                seismograph_count, 
                sample_rate_hz,
                alert_callback):

        """
        Args: 
            seismograph_count: the number of seismographs in the detector network.
            sample_rate_hz: the sample rate of the seismograph.
            alert_callback: a callback function if an earthquake is detected.
        """

        """
        Steps for earthquake detection
        1. Loop through every seismograph
        2. compare the slope of the previous x amount of points (called old_seismograph_roc) with the new slope
        3. If the slope is threshold * the previous slope, set a flag (called possibly_earthquake) to true
        4. If all the detectors have set their flags to true, trigger the alert
        """
        """This value is 5, but based on testing it should be changed"""
        threshold = 5

        if old_seismograph_roc == NULL:
            old_seismograph_roc = np.full((seismograph_count, 2), None)

        if new_datapoints == NULL:
            pass

        possibly_earthquake = np.full(seismograph_count, False)
        
        for i in range(seismograph_count):
            old_seismograph_roc[i][0] = (new_datapoints[1] - new_datapoints[0])/sample_rate_hz
            for j in range(new_datapoints)-1:
                old_seismograph_roc[i][1] = new_datapoints[j] - new_datapoints[j-1] / sample_rate_hz
                if old_seismograph_roc[i][1] > threshold*old_seismograph_roc[i][0]:
                    possibly_earthquake[i] = True
                old_seismograph_roc[i][0] = old_seismograph_roc[i][1]
            
                
        
        if possibly_earthquake.all() == True:
            alert_callback()

        pass

    def new_samples(self, seismograph_id, samples):

        """New samples are available for a seismograph.

        Args: 
            seismograph_id: the zero-indexed seismograph id.
            samples: an ndarray of integer samples.
        """
        if new_datapoints == NULL:
            new_datapoints = {}

        new_datapoints[seismograph_id] = samples
        
        if total_datapoints.get(seismograph_id) == None: 
            total_datapoints[seismograph_id] = samples
        else:
            total_datapoints[seismograph_id].append()

        pass