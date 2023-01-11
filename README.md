# DistroKid-Wheel-Of-Playlist-Automator
A simple Python script designed to automatically push a given song to the DistroKid "Wheel Of Playlist"

 ## Index
 * [Installation](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator/blob/main/README.md#installation)
   * [Cookies](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator#cookies)
     * [DistroKid Cookies](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator/blob/main/README.md#distrokid-cookies)
     * [Spotify Cookie](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator#spotify-cookie)
   * [Email Integration](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator#email-integration)
     * [Gmail](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator#gmail)
       * [IMAP Setup](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator#imap-Setup)
       * [With 2FA](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator#with-2fa)
       * [Without 2FA](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator#without-2fa)
   * [Discord Integration](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator#discord-integration)

 * [Execution](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator/blob/main/README.md#execution)
   * [Windows](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator#windows)
   * [Linux](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator#linux)
   * [Mac](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator#mac)

 * [Interaction](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator/blob/main/README.md#interaction)

## Installation
First and foremost download the contents of the repo, and unzip them in an ideally empty folder.

Next, assuming you don't already have [Python](https://www.python.org/) you need to [install Python](https://www.python.org/downloads/). Then use Pip to install the needed requirements

```pip install -r requirements.txt```

Once you have installed both [Python](https://www.python.org/) and the requirements, open the file `config.py` in your favorite text editor or IDE and fill out the blanks according to the instructions laid out in the [Cookies](https://github.com/Skribb11es/DistroKid-Wheel-Of-Playlist-Automator#cookies) section. (Based on what browser you use this will be different, below is a list of the most common browsers and how to access the needed information for each field that needs to be filled out)

### Cookies

#### DistroKid Cookies
* Navigate to [DistroKid](https://distrokid.com)'s website
* Open dev tools (`Ctrl+Shift+I` or `f12`)
* For firefox, navigate to the storage tab, and click the dropdown labeled Cookies.
* Chromium based browsers, such as Opera, Edge, Google Chrome, Brave, etc, select to the lock icon to the left of the search bar, select cookies, and then the dropdown for `distrokid.com`, finally select the Cookies folder.
* locate the cookies labeled `cfid`, `BEEFARONI`, `DK_SYN`, and `COMPUTER_00000000000000000000000000000000` (the `COMPUTER_` cookie will instead have a randomly generated string instead of 32 zeros.).
* Copy the Value of the `cfid` cookie, and paste it between the "" for the variable `DKCFID`
* Copy the Value of the `COMPUTER_` cookie, and paste it between the "" for the variable `DKCOMP`
* Copy the Name of the `COMPUTER_` cookie, and paste it between the "" for the variable `DKCOMPKEY`
* Copy the Value of the `BEEFARONI` cookie, and paste it between the "" for the variable `DKBEEFARONI`
* Copy the Value of the `DK_SYN` cookie, and paste it between the "" for the variable `DKSYN`

#### Spotify Cookie
* Navigate to [Spotify](https://spotify.com)'s website
* Open dev tools (`Ctrl+Shift+I` or `f12`)
* Navigate to the storage tab, and click the dropdown labeled Cookies
* locate the cookie labeled `sp_dc`
* Copy the Value of the `sp_dc` cookie, and paste it between the "" for the variable `SP`

### Email Integration

Since DistroKid sends you an email each time your song is removed from the playlist, we are able to use that as a trigger to push our song to the playlist again

This section will only cover how to use Gmail as an IMAP server, if you use any other email provider, it is recommended that you consult their documentation on how to connect your email account to this script.

**IMPORTANT!** Note that using IMAP will cause Gmail to show your emails as read, even if you have not manually opened them. (I am currently unaware if this occurs with any other email platforms)

#### Gmail

##### IMAP Setup
* Navigate to your [Gmail homepage](https://mail.google.com/)
* Navigate to the settings cog in the top right.
* Select `See all settings`.
* Navigate to the tab labeled `Forwarding and POP/IMAP`.
* Select the `Enable IMAP` option.
* Select `Save Changes` at the bottom of the page.

##### With 2FA
* Navigate to your [Google Account](https://myaccount.google.com/).
* Navigate to `Security`.
* Navigate to `App Passwords` (You may need to enter your password after you select this).
* From the leftmost dropdown select `Mail`, then select the type of device from the other dropdown.
* Select `Generate`
* Copy the string of characters within the yellow text box.
* Return to your text editor and open `config.py`.
* Input your email address between the "" for the variable `IMAPUSERNAME`.
* Input the text you just copied between the "" for the variable `IMAPPASSWORD`.
* Input `imap.gmail.com` between the "" for the variable `IMAPSERVER`.

##### Without 2FA
* Return to your text editor and open `config.py`.
* Input your email address between the "" for the variable `IMAPUSERNAME`.
* Input your Gmail account password between the "" for the variable `IMAPPASSWORD`.
* Input `imap.gmail.com` between the "" for the variable `IMAPSERVER`.

### Discord Integration
This is only really useful if you plan on running this script remotely, or you just want a notification through discord that your song has been pushed to the playlist.
* In your discord server of choice (I would reccomend an empty server), make a webhook. (Hover over a channel, select the cog icon, click `Integrations`, then `Create Webhook`, select the new webhook, and click `Copy Webhook URL`)
* Input the webhook you just copied between the "" for the variable `webhookURL`.
* Change the value of the `webhook` variable to `True`

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
