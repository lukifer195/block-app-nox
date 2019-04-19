#utf-8

import subprocess

str = """com.android.providers.contacts
com.svox.pico
com.android.bluetooth
com.android.wallpaper.livepicker
com.android.soundrecorder
com.google.android.gsf.login
com.android.providers.userdictionary
com.android.browser
com.google.android.play.games
com.android.providers.telephony
com.android.keychain
com.android.webview
com.android.contacts
com.google.android.gsf
com.android.providers.downloads
com.android.htmlviewer
com.facebook.lite
com.android.gallery3d
com.android.soundrecorder
com.android.phone
com.android.mms.service
com.android.server.telecom
com.android.vending
"""

you_want_to = 'block'

s=str.splitlines()
for x in s:
    subprocess.Popen('adb shell pm '+ you_want_to + x)
