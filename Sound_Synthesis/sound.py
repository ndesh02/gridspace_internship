import math
import wave
BITRATE = 50000
FREQUENCYA = 392.00
FREQUENCYB = 659.26
FREQUENCYC = 523.25
LENGTH = 1
WIDTH = 1
NUMBEROFFRAMESPERNOTE = int(BITRATE * LENGTH )
WAVEDATA = ''
for x in range(NUMBEROFFRAMESPERNOTE):
     WAVEDATA =WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCYA)/math.pi))*127+128))
for x in range(NUMBEROFFRAMESPERNOTE):
     WAVEDATA =WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCYB)/math.pi))*127+128))
for x in range(NUMBEROFFRAMESPERNOTE):
     WAVEDATA =WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCYC)/math.pi))*127+128))

wr = wave.open("nbc-chimes.wav", 'wb');
wr.setnchannels(1);
wr.setsampwidth(2);
wr.setframerate(BITRATE)
b = str.encode(WAVEDATA);
wr.writeframes(b);
wr.close();
