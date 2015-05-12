# sublime-timecoder
####Timer timestamps for Sublime Text 3 

This is a simple plug-in that allows you to add a timer-based time-stamp to a Sublime Text 3 document. 

CTRL+Y: starts/resets the timer.
CTRL+T: inserts the timer value at the location of the cursor. 

I made this during my sixth week of the Flatiron School's Web Immersive. Lectures are dense and sometimes over two hours long. So, I wanted an easy way to find a particular topic on a video. And has made review sessions a lot more efficient. 

Here's a short [screencast](https://youtu.be/4lFmU_xLSe4) of its functionality. 

On a mac, you store the entire timecoder folder in the following directory:  

```
Users/”Username”/Library/Application Support/Sublime Text 3/Packages

```
This is a work in progress. I'm very new to Python (Flatiron is a Ruby/Ruby on Rails program), so I'm sure the Python can probably be cleaner. 

Next steps:

- fixing the visual bug where numbers less than ten appear as single digits and not with a zero, eg 1:3:4 should appear as 01:03:04. (Hopefully soon!) 

-  add .sublime-keymap docs for Linux and Window. 


I drew from three resources to make this: 

[How to Create a Sublime Text 2 Plugin, by Will Bond](http://code.tutsplus.com/tutorials/how-to-create-a-sublime-text-2-plugin--net-22685) 

[Creating Sublime Text 3 Plugins – Part 1, by Sam Mello](https://clarknikdelpowell.com/blog/creating-sublime-text-3-plugins-part-1/) 

and, of course 
the [Sublime Text API Reference](https://www.sublimetext.com/docs/3/api_reference.html) 
