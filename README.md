# Wheel-Of-Playlist-Auto-Update
A simple Python script designed to automatically push a given song to the DistroKid "Wheel Of Playlist"

NEEDS TO BE UPDATED TO V0.2

 ## Index
 * [Installation](https://github.com/Skribb11es/Wheel-Of-Playlist-Auto-Update/blob/main/README.md#installation)
   * [Firefox](https://github.com/Skribb11es/Wheel-Of-Playlist-Auto-Update#firefox)
     * [DistroKid Cookies](https://github.com/Skribb11es/Wheel-Of-Playlist-Auto-Update/blob/main/README.md#distrokid-cookies)
     * [Spotify Cookie](https://github.com/Skribb11es/Wheel-Of-Playlist-Auto-Update#spotify-cookie)

 * [Execution](https://github.com/Skribb11es/Wheel-Of-Playlist-Auto-Update/blob/main/README.md#execution)
   * [Windows](https://github.com/Skribb11es/Wheel-Of-Playlist-Auto-Update#windows)
   * [Linux](https://github.com/Skribb11es/Wheel-Of-Playlist-Auto-Update#linux)
   * [Mac](https://github.com/Skribb11es/Wheel-Of-Playlist-Auto-Update#mac)

 * [Interaction](https://github.com/Skribb11es/Wheel-Of-Playlist-Auto-Update/blob/main/README.md#interaction)

## Installation
First and foremost download the contents of the repo, and unzip them in an ideally empty folder.

Next, assuming you don't already have [Python](https://www.python.org/) you need to [install Python](https://www.python.org/downloads/). Then use Pip to install the needed requirements

```pip install -r requirements.txt```

Once you have installed both [Python](https://www.python.org/) and the requirements, open the config.py in your favorite text editor or IDE and fill out the blanks accordingly. (Based on what browser you use this will be different, below is a list of the most common browsers and how to access the needed information for each field that needs to be filled out)

### Firefox
If you are using Firefox, first off you have the ability to use automatic cookie detection, unlike any other browser. Unfortunately, this is due to Firefox storing cookies as plain text in a Sqlite DB, unlike most other mainstream browsers.

To enable automatic cookie detection, change the `cGrab` variable to `True` in the config, save the file, and you're done.

```cGrab = True```

However, if you are like me and would rather manually define your information, this too is an option.

#### DistroKid Cookies
* Navigate to [DistroKid](https://distrokid.com)'s website
* Open dev tools (`Ctrl+Shift+I` or `f12`)
* Navigate to the storage tab, and click the dropdown labeled Cookies
* locate the cookies labeled `cfid` and `COMPUTER_00000000000000000000000000000000` (the `COMPUTER_` cookie instead having a randomly generated string instead of 32 zeros.)
* Copy the Value of the `cfid` cookie, and paste it between the "" for the variable `DKCFID`
* Copy the Value of the `COMPUTER_` cookie, and paste it between the "" for the variable `DKCOMP`
* Copy the Name of the `COMPUTER_` cookie, and paste it between the "" for the variable `DKCOMPKEY`

#### Spotify Cookie
* Navigate to [Spotify](https://spotify.com)'s website
* Open dev tools (`Ctrl+Shift+I` or `f12`)
* Navigate to the storage tab, and click the dropdown labeled Cookies
* locate the cookie labeled `sp_dc`
* Copy the Value of the `sp_dc` cookie, and paste it between the "" for the variable `SP`

Assuming you have followed the steps above to a T, it is now time for you to run the script. Scroll down to the section labeled `Execution`, and follow the steps provided.

## Execution

It is recommended that you run this through your terminal or shell of choice, as it will persist after execution allowing you to potentially diagnose any issue that you have come across. (Yes these are redundant, and no I didn't want to write them this way, however, dealing with inexperienced users I have learned a great deal that it is better to explain it plainly and in detail the first time than do it multiple times later)

### Windows
* Open CMD and navigate to the primary directory of the script `cd .\Path\To\Script` (the directory that main.py is located in)
* Execute the command `python main.py`

### Linux
* Open Terminal and navigate to the primary directory of the script `cd .\Path\To\Script` (the directory that main.py is located in)
* Execute the command `python main.py`

### Mac
* Open Terminal and navigate to the primary directory of the script `cd .\Path\To\Script` (the directory that main.py is located in)
* Execute the command `python main.py`

## Interaction
* Upon execution, it will appear to freeze for a short time, this is the application "logging in" under the provided information, and fetching the songs that you have made.
* The application will now display a list of your songs, prompting you to select one of the listed songs to add to the DistroKid "Wheel Of Playlist" playlist, simply type the number of the song you want to select and press enter.
* Next it will ask if you want to continuously push the selected song to the playlist or not, if you choose `n` it will run through the process of adding the song to the playlist once, and then close. If you instead choose `y` the application will run, once an hour, until you close it, or otherwise terminate the process.
* At this point the application will now print out the position your song is currently in the playlist, and boom you're done!
