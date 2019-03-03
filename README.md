# iBlink : Eye blink reminder
An Application to help you remind to blink and protect your eyes!

## About
A cross platform application built using electron Js and python to generate desktop notifications to remind users to blink.
People spending large amount of time on screens, suffer from various eye sight related problems, major one of them being dryness of eyes caused dropped blinking rate.
We developed an application that can be useful to remind people when to blink, also another feature includes the famous 20-20-20 rule reminder.
The notifications are displayed over any application that you're currently using, even if this application is minimised. The notification frequency is completely adjustable according to personal needs in the settings section.
<br/>
The application also provides a feature to completely turn off notifications, so as to not disturb or distract the user. But it maintains the blink count of user and the user can watch his blink rate of past 24 hrs on a live graph.


## Code Requirements
* Node JS
* Electron JS
* python 3.x with following modules installed

1. numpy
2. imutils
3. scipy
4. dlib
5. opencv2

## Execution

* Step 1:
Clone this repo into your system <br/>
` git clone https://github.com/shubham99bisht/iblink.git ` <br/>

* Step 2:
Download the **shape_predictor_68_face_landmarks.dat**
[here](https://github.com/akshaybahadur21/Drowsiness_Detection/raw/master/shape_predictor_68_face_landmarks.dat)
<br/> Save this into `engine` folder

* Step 3:<br/>
`cd iblink`<br/>
`npm init` (You will be asked few details in this steps, you can skip them by pressing return key a few times) <br/>
`npm install`<br/>
`npm start`<br/>


## Algorithm

Using 68 Face Landmarks, we're figuring out the location of eyes in the camera feed, once we've the points around eyes, we calculate the Eye Aspect ratio (EAR).
If the EAR value is less than a particular threshold, we assume that the eye is closed. Whenever we find a sequence of closing and opening of eyes, we increment the blink count and at the end of the minute
a total count of blinks is displayed.

For detailed explanation about EAR calculation please visit Akshay Bahadur's [Drowsiness Detection](https://github.com/akshaybahadur21/Drowsiness_Detection)
This code's core algorithm of detecting eye blinks has been borrowed from this repository. 
<br/>
P.S. : Thank you Akshay for amazing projects :)


## Demo

**Running Demo**<br/>
![alt_text](https://github.com/shubham99bisht/iblink/blob/master/samples/demo1a.gif)
<br/><br/>

**Notifications are generated even when the app is minized**<br/>
![alt](https://github.com/shubham99bisht/iblink/blob/master/samples/demo2.png)
