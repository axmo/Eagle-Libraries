## Pacav69 Eagle Library

Taken from various sources and some that i have created

## Instructions for installation from Adafruit

================================

### Don't click on the files! 
[Click here for pacav69 libraries](https://github.com/pacav69/Eagle-Libraries/zipball/master) 
to download this as a zip file.

[Click here for Adafruit libraries](https://github.com/adafruit/Adafruit-Eagle-Library/zipball/master) 
to download this as a zip file.

### Installation
#### To use Libraries:

* Open Eagle and select the `Control Panel` window.
* Choose `Options` and from the drop down that appears, `Directories`.
* Change the Libraries line from: `$EAGLEDIR/lbr` to something like:

### for Mac OS X:

	$EAGLEDIR/lbr:$HOME/external_lbrs
     
### for Windows:

	$EAGLEDIR\lbr;$HOME\external_lbrs 
	
#### To use Datasheets:
* Open Eagle and select the `Control Panel` window.
* Choose `Options` and from the drop down that appears, `Directories`.
* Change the Documents line from: `$EAGLEDIR/doc` to something like:

### for Mac OS X:

	$EAGLEDIR/doc:$HOME/external_lbrs/Datasheets
     
### for Windows:

	$EAGLEDIR\lbr;$HOME\external_lbrs\Datasheets
    

* Click `OK` to save your changes.
5. Eagle will prompt to create the directory if it does not already exist. Note 
the location and choose `Yes` to create the directory.

### On Mac OS X:
    
    `$HOME/external_lbrs` changes to: /Users/[USERNAME]/external_lbrs
    
### On Windows: 
    
    `$HOME\external_lbrs` changes to: C:\Users\[USERNAME]\Documents\external_lbrs


* Find and open the `external_lbrs` folder. Unzip and drag `adafruit.` and 'pacav69' libraries' into the new `external_lbrs` folder.
* Restart Eagle. The library should be now be usable. 
* Use the Eagle Cad control panel to browse libraries.
* 
## Changes
Refer to the file changelog.txt 

## Some useful library locations

* [www.element14.com](https://www.element14.com/community/community/cadsoft_eagle/blog/2015/01/15/the-10-most-popular-cadsoft-eagle-libraries)
* [sparkfun](https://github.com/sparkfun/SparkFun-Eagle-Libraries)
* [www.element14.com/community](https://www.element14.com/community/community/cadsoft_eagle/eagle_cad_libraries?ICID=cadsoft-main-sidenav)
* [element-14-all-cad-files](https://www.element14.com/community/thread/36914/l/element-14-all-cad-files)
* [bobstarr.net](http://www.bobstarr.net/pages/downloads.html)

## User Language Programs (ULP)

* [element14](https://www.element14.com/community/community/cadsoft_eagle/blog/2015/01/19/eagle-ulps-every-user-should-know)


## Useful tips

* [www.elecrom.com](http://www.elecrom.com/eagle-library-list-of-most-commonly-used-electronics-components/)

* [clean-up-the-parts-list](https://www.baldengineer.com/eagle-clean-up-the-parts-list-by-disabling-libraries.html)


