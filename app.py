from slackclient import SlackClient
import time

slack_client = SlackClient("xoxp-345187792039-344274260453-566478079093-7790aebe7b2a15608e718c0fc3a561e5")

if slack_client.rtm_connect(with_team_state=False):
    print ("Successfully connected, listening for events")
    while True:
        print slack_client.rtm_read()

        time.sleep(1)
else:
    print "Connection Failed"