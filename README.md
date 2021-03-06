## My-Gallery


## Table of Contents

+ [Description](#description)
+ [Get Started](#get-started)
+ [Requirements](#requirements)
+ [Code](#code)
+ [Technology Used](#technology-used)
+ [Reference](#reference)
+ [Licence](#licence)
+ [Authors Info](#author-Info)

## Description
Welcome to My-Gallery web application where we give you a platform view different images, add your images, add a description, add a date when the picture was posted
and add comments to other people's pitches.

The app has`template` folder where the markup langauge is written, a `static` folder where
the stylesheet is stored and media files and the `manage.py` file where the main function is run. Other severall python files too that are used to import data

<p>The images, description,date and unique ID are stored and managed in a database</p>


### Get Started
* Visit the webapp and navigate to the `categories` tab to select on the categoryy of choice and view photos for those categories. When you click on the category of choice all images under that category are displayed.

* My-Gallery also allows you to add images and categories of choice. For every image created, a unique id is autogenerated for it. Once you click on any category the url crteates a path by the categor name `http://127.0.0.1:8000/?category=Sport`
When you want to view the image description, you click on `view` and the url creates a path to a different template and displays th image with its uniqueId `http://127.0.0.1:8000/photo/?photo=9c6c5af27cbd`

[Go Back to the top](##-Table-of-Contents)


### Requirements

* A laptop or a desktop computer

* An access to the reliable Internet connection

### Code
To access the code;

* Just clone this `https://github.com/Collins07/My-gallery.git` project into your computer

* Open the terminal

* run the `python3.8(version of your python) manage.py runserver` file 



[Go Back to the top](##-Table-of-Contents)

## Technology Used

* Django - a python framework

* Databases - store user data


## Reference

* python official website ```https://packaging.python.org```

* Programming with Mosh

* Code With Harry (youtube channel)
[Go Back to the top](##-Table-of-Contents)

## Licence

MIT License

Copyright (c) [2022] [Collins07]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
[Go Back to the top](##-Table-of-Contents)