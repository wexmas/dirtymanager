from slackclient import SlackClient

slack_client = SlackClient("xoxb-*******************")

api_call = slack_client.api_call("users.list")
if api_call.get('ok'):
    users = api_call.get('members')
    for user in users:
        print user.get('name')