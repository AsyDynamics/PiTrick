#!/usr/bin/env python
import sys 
from twython import Twython
tweetStr = "Lucky to get the password of the router, and set the DMZ configure of the RPI at home, make it sshable via internet. This twitter is post by a python script running on raspberry pi :)"
# your twitter consumer and access information goes here note: these are
# garbage strings and won't work
apiKey = 'Kyn90AnEUy83Or7FpSBvopjtJ'
apiSecret = 's7eyhFuY5yzhBHS7FUTJxXarKExcpDhy8gK80yPhuuBqJlfiKO'
accessToken = '904802642790154241-2rD2WRnFlShX3VDT0pyoHTfBZd4oKLo'
accessTokenSecret = 'd5M2SVeLvux0HySvFnrvgYR5BVuEgFfgcRvAbH7QDpUJc'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr
