Pitch Detector Overlay
======================
###### Because yes, I wasn't creative enough for a better name.

![143563889 61_image](https://user-images.githubusercontent.com/75105627/204110684-ed8b6a85-2b54-4b41-9629-4749a5930e41.png)

## What is this?

Somethings in life are easy. Others however, take time, practice and patience. This app was spaghetti coded together to help anyone looking to change the pitch of their voice, and make it a more perminent addition. 


## How does it work?

The overlay currently displays on the top left of your screen. It will display over any window that is not full screen. It updates every half second and takes the average of pitch of your voice over that half second. There is a threshold set in the main.py file to play a notification when your voice starts to slip. The overlay will also tell you at what Hz your last flub was. To stop the program from spamming you with notifications, it will only tell you about your flubs when you are making a pattern of lower pitch. 

We all know that pitch is only one part of the puzzle, but it is also the hardest part to make a habit. It takes a lot of time to make that new pitch your default. This app should help with other exercises you've found to help with things such as resonance and inflection.

## How to use

Clone the repo and extract the files.

open a terminal and go into the folder (On win 11 right click in the folder, then click terminal).
Type pip install -r requirements.txt

Then run the main.py file with the command: 

python main.py

It will ask you what Hz you want to be your minimum. If you talk below it, it'll track it, and after talking below it for a little bit, it'll beep at you. 


Alternatively, you can download the zip'd exe [here](https://github.com/AshPotatoh/Pitch_Detector_Overlay/releases/tag/Release)
