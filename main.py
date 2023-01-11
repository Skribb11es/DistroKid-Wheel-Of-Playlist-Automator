#Makes all of the needed imports, some are currently unused but will find use later as more features are added ;D
import imaplib2, time, email, json, os, sys, string, random, logging, contextlib
from requests import request, Session
from http.client import HTTPConnection
from bs4 import BeautifulSoup
from threading import *
from config import *
from IMAP import *

#Sends the requests needed to get have the song published to the playlist via DistroKid
def makePlaylistRequest(ses, ID):
    ses.get("https://distrokid.com/wheel/connect/?scope=playlist-modify-public+user-follow-modify", allow_redirects=True)
    place = ses.post("https://distrokid.com/api/wheel/", data={'songId': ID})

    try:
        pos = place.json()["positions"]
        pos.sort()
        if webhook:
            ses.post(webhookURL, data={"content": "@here Your song has been pushed to position " + str(pos[0]) + "!"})
        else:
            print("Done! Your song has been pushed to position " + str(pos[0]) + "!")

    except:
        try:
            if place.json()["error"] != "":
                return
        except:
            print("An unknown error occurred.")

def main():
    #Opens a session
    session = Session()
    session.max_redirects = 4
    session.get("https://distrokid.com/wheel")

    logging.getLogger().setLevel(logging.CRITICAL)

    #Only used for debugging purposes, or if you just enjoy seeing a console full of interesting information (I know I do ;D)
    if debug == True:
        HTTPConnection.debuglevel = 1
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    #Honestly a terrible way of doing this, but doing this with the library I used, it is the "best". It just clears the cookie of one value, and reinstates it with another value, also this defines your spotify cookie, and your "computer" identifier for DistroKid
    session.cookies.pop("cfid")
    session.cookies.set("cfid", DKCFID)
    session.cookies.set(DKCOMPKEY, DKCOMP)
    session.cookies.set('sp_dc', SP)
    session.cookies.set('BEEFARONI', DKBEEFARONI)
    session.cookies.set("DK_SYN", DKSYN)

    #Fetches the song list and parses it, so we can then output it in a "good looking" manner later.
    grabSongs = session.get("https://distrokid.com/wheel/")
    parsedSongs = BeautifulSoup(grabSongs.content, 'html.parser')
    songList = parsedSongs.find_all('option')
    #Just a loop and a "prompt", to output all the possible selections the user can make.
    print("Select one of the following songs to add to the playlist.")
    count = 1
    for i in songList:
        if i.text != "" and i["value"] != "":
            print(str(count) + " " + i.text[1:len(i.text)-1])
            count += 1

    #Another loop to make sure that what the user inputs into the applictaion will actually be useful information. Also sets the selected song ID to a variable
    songId = ''
    while True:
        inp = input()
        try:
            print(f"Successfully selected '{songList[int(inp)].text[1:len(songList[int(inp)].text)-1]}' as the song to push...")
            songId = songList[int(inp)]["value"]
            break
        except:
            print(f"Invalid value provided '{inp}', please supply an integer within the list.")

    #Asks the user if they want to loop the addition of their song, assuming there is availability to do so
    print("Do you want this song to be continuously pushed to the playlist? y/n")
    while True:
        inp = input()
        if inp == "y":
            while True:
                M = imaplib2.IMAP4_SSL(IMAPSERVER)
                M.login(IMAPUSERNAME,IMAPPASSWORD)
                M.select("INBOX")
                idler = Idler(M, makePlaylistRequest, [session, songId])
                idler.start()
                time.sleep(3600)
                idler.join()
                idler.stop()
                M.logout()
        if inp == "n":
            makePlaylistRequest(session, songId)
            break
        print(f"Invalid type '{inp}', please use y/n")

if __name__ == '__main__':
    main()
