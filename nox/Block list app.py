#utf-8

import subprocess

str = """adb shell pm hide com.android.providers.contacts
adb shell pm hide com.svox.pico
adb shell pm hide com.android.bluetooth
adb shell pm hide com.android.wallpaper.livepicker
adb shell pm hide com.android.soundrecorder
adb shell pm hide com.google.android.gsf.login
adb shell pm hide com.android.providers.userdictionary
adb shell pm hide com.android.browser
adb shell pm hide com.google.android.play.games
adb shell pm hide com.android.providers.telephony
adb shell pm hide com.android.keychain
adb shell pm hide com.android.webview
adb shell pm hide com.android.contacts
adb shell pm hide com.google.android.gsf
adb shell pm hide com.android.providers.downloads
adb shell pm hide com.android.htmlviewer
adb shell pm hide com.facebook.lite
adb shell pm hide com.android.gallery3d
adb shell pm hide com.android.soundrecorder
adb shell pm hide com.android.phone
adb shell pm hide com.android.mms.service
adb shell pm hide com.android.server.telecom
adb shell pm hide com.android.vending
"""
s=str.splitlines()
for x in s:
    print(x.split()) 
    subprocess.call(x.split())
