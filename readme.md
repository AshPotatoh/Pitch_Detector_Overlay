Pitch Detector Overlay
======================
######Because yes, I wasn't creative enough for a better name.


#What is this?

Somethings in life are easy. Others however, take time, practice and patiences. This app was developed to help anyone looking to change the pitch of their voice, and make it a perminent addition. This would typically be used by a trans person trying to make their voice sound more feminine, or masculine. 


#How does it work?

The overlay currently displays on the top left of your screen. It will display over any window that is not full screen. It updates every half second and takes the average of pitch of your voice over that half second. There is a threshold set in the main.py file to create a notification when your voice starts to slip. The overlay will also tell you at what Hz your last flub was. To stop the program from spamming you with notifications, it will only tell you about your flubs when you are making a pattern of lower pitch. 

We all know that pitch is only one part of the puzzle, but it is also the hardest part to make a habit. It takes a lot of time to make that new pitch your default. This app should help with other exercises you've found to help with things such as resonance and inflection.


The program currently has the Flub alarm at 180hz, the low end for feminine voices. Eventually, I would like this application to be a tray application that allows the user to change settings via a few sliding bars. 