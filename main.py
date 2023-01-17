import aubio
import numpy as num
import pyaudio
from pyaudio import PyAudio
import vlc
import time
import tkinter as tk
from tkinter import Button, Entry, Tk, Toplevel, Canvas, Label
import tkinter.font as font
import threading
import wave

def param_builder():

    print("Welcome to the Pitch Detector Overlay!\n")
    target_hz = input("What is the minimum Hz you would like to aim for? (Whole numbers only) ")
    target_hz = float(target_hz)
    print(type(target_hz))

    if target_hz.is_integer() == False:
        print("error whole numbers only. Use numbers like 160, 180, 220, etc")
        param_builder()
    else:
        print("Target set to " + str(target_hz))
        return target_hz

targethz = param_builder()

######PARAMS
BUFFER_SIZE             = 2048
CHANNELS                = 1
FORMAT                  = pyaudio.paFloat32
METHOD                  = "default"
SAMPLE_RATE             = 44100
HOP_SIZE                = BUFFER_SIZE//2
PERIOD_SIZE_IN_FRAME    = HOP_SIZE

averagePitch = 0

frames = []
yes_no = True
please_stop = False
is_playing = False



def playback():
   
   print("Recording Started")
   CHUNK = 1024
   FORMAT = pyaudio.paInt16
   CHANNELS = 2
   RATE = 44100
   RECORD_SECONDS = 5
   WAVE_OUTPUT_FILENAME = "output.wav"

   p = pyaudio.PyAudio()
   print("Playback 1")
   stream = p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK)

   print("Playback 1")

   global frames
   global yes_no
   still_running = True
   while still_running:
      
      data = stream.read(CHUNK)
      frames.append(data)
      #print(len(frames))

      if len(frames) > 1000:
         del frames[:]
         print("Playback 1")

      if yes_no == False:
         print(yes_no)
         print("saving")
         last_five = frames[-216:]
         waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
         waveFile.setnchannels(CHANNELS)
         waveFile.setsampwidth(p.get_sample_size(FORMAT))
         waveFile.setframerate(RATE)
         waveFile.writeframes(b''.join(last_five))
         waveFile.close()
         yes_no = True
         print(yes_no)
      
      if win.state:
         pass
      else:
         still_running = False
      
      
   print("* done recording")

   stream.stop_stream()
   stream.close()
   p.terminate()


def oneSecond(listy):
   
   


   pListSum = sum(listy)
   pListLen = len(listy)
   average = 0
   if pListLen > 1: 
      average = pListSum/pListLen
      

      print(average)
   return(average)

def start_pitch():
   pitch = threading.Thread(target=pitch_detector)
   pitch.run()
   return True

def update_timer(t_bool):
   #track last output of timer

   
   last_time = 0
   #last_time - current_time + total_time
   current_time = 0
   total_time = 0
   if t_bool == True:
      last_time = 0
   else:
      t0 = time.time()
      current_time = t0
      total_time = last_time - current_time + total_time
      last_time = t0
      




def pitch_detector(mic_index, target):
    pA = pyaudio.PyAudio()
    mic = pA.open(format=FORMAT, channels=CHANNELS,
        rate=SAMPLE_RATE, input=True, input_device_index=mic_index,
        frames_per_buffer=PERIOD_SIZE_IN_FRAME)
   
    pDetection = aubio.pitch(METHOD, BUFFER_SIZE,
        HOP_SIZE, SAMPLE_RATE)
    pDetection.set_unit("Hz")

    
    pDetection.set_silence(-35)
    count = 0
    messup = 0
    pitch_average = []
   


    while True:
        data = mic.read(PERIOD_SIZE_IN_FRAME)
        
        samples = num.fromstring(data,
            dtype=aubio.float_type)
        
        pitch = pDetection(samples)[0]

        volume = num.sum(samples**2)/len(samples)
        
        volume = "{:6f}".format(volume)
        
        pitch_average.append(pitch)
        bananas = 5
        if len(pitch_average) > 30:
          
         average = [item for item in pitch_average if item >= 10.0 and item <= 500.0]
         
         global oneSecondAverage
         oneSecondAverage = oneSecond(average)
         global averagePitch
         averagePitch = oneSecondAverage
         print(type(oneSecondAverage))


         pitchhz.config(text=f'{str(int(oneSecondAverage)) + "Hz"}')
         
         floatAverage=num.float64(oneSecondAverage)
         pitch_average.clear()
         average.clear()
         print(count)
         target = float(target)
         if floatAverage < target and floatAverage > 110.0:
            messup += 1
            global yes_no
            print("is actually " + str(yes_no))
            print(messup + pitch)
            
            if messup > 4:
               messuphz.config(text=f'Last messup: {str(int(floatAverage)) + "Hz"}', bg="red2")
               
               d = vlc.MediaPlayer("boop.mp3")
               d.audio_set_volume(100)
               d.play()
               time.sleep(0.4)
               yes_no = False
               messuphz.config(text=f'Last flub: {str(int(floatAverage)) + "Hz"}', bg="black")
               messup = 0
               


            
            count = 0
         elif count > 400:
            count = 0
            messup = 0
         count += 1












######### WINDOW CONFIGS
win = tk.Tk()
desktop_y = win.winfo_rooty
desktop_x = win.winfo_rootx
win_x = 3840 + 400
win_y = 1080 + 300

win.attributes('-transparentcolor', 'black', '-topmost', 1)
win.config(bg='black')
win.bg = Canvas(win,width=400, height=300, bg='black')
#win.wm_attributes('-fullscreen', 'True')
win.wm_attributes("-disabled", True)
win.geometry('480x300+400+0')

e = Entry(highlightthickness=2)
e.config(highlightbackground= "green", highlightcolor="green")
e.pack
win.overrideredirect(1)
pitchhz = Label(win, text='', font='Helvetica 16 bold', bg='black', foreground="white", highlightbackground="black", command=threading.Thread(target=pitch_detector, args=(1, targethz,)).start(), )
#pitchhz['font'] = font.Font(size=16)
pitchhz.grid(column=1, row=1, padx=(0,0))
messuphz = Label(win, text="last flub:",font='Helvetica 16 bold', bg='black', foreground="white")
messuphz.grid(column=2,row=1, padx=10)
# exit_button = Button(win, text="Exit", command=win.quit)
# exit_button.grid(column=3, row=1, padx=10)


#button = tk.Button(win, text='start', .pack(pady=40)
win.mainloop()



    
        
