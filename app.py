from slackclient import SlackClient

slack_client = SlackClient("xoxp-345187792039-344274260453-566478079093-7790aebe7b2a15608e718c0fc3a561e5")

api_call = slack_client.api_call("users.list")
if api_call.get('ok'):
    users = api_call.get('members')
    for user in users:
        print user.get('name')