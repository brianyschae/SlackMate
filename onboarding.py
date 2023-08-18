# commands.py
import slack
from slack_bolt import App
from env import client

def onboarding_process_handlers(app: App):
    @app.command("/start")
    def open_modal(ack, body, client):
        ack()
        client.views_open(
            trigger_id=body["trigger_id"],
            view={
                "type": "modal",
                "callback_id": "view-id",
                "title": {"type": "plain_text", "text": "SlackMate"},
                "submit": {"type": "plain_text", "text": "Submit"},
                "close": {"type": "plain_text", "text": "Close"},
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Hey there 👋 I'm SlackMate. I'm here to help you through your onboarding process at CTCT and provide you Listed Reminders and Goal Settings for your new beginning at CTCT."
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "To start the app 🥳, select your team down below:"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "input",
                        "block_id": "es_b",
                        "element": {
                            "type": "external_select",
                            "action_id": "es_a",
                            "placeholder": {"type": "plain_text", "text": "Select a team"},
                            "min_query_length": 0,
                        },
                        "label": {"type": "plain_text", "text": "Team"},
                    },
                ],
            },
        )

    @app.options("es_a")
    def show_options(ack):
        ack(
            {
                "options": [
                    {
                        "text": {"type": "plain_text", "text": "Contacts"}, "value": "Contacts"
                    },
                    {
                        "text": {"type": "plain_text", "text": "EM-UI"}, "value": "EM-UI"
                    },
                    {
                        "text": {"type": "plain_text", "text": "Shared Frameworks"}, "value": "Shared Frameworks"
                    },
                    {
                        "text": {"type": "plain_text", "text": "Team Goose"}, "value": "Team Goose"
                    },
                ]
            }
        )
    
    @app.view("view-id")
    def view_submission(ack, body):
        ack()
        user_id = body["user"]["id"]
        result = body["view"]["state"]["values"]["es_b"]["es_a"]["selected_option"]["text"]["text"]
        WelcomePost(result, user_id)

    def WelcomePost(team, user_id):
        text = f'Welcome to {team} 😀'
        client.chat_postMessage(channel=f'@{user_id}', text=text)

        if (team == 'Contacts'):
            text = """:round_pushpin: Some contacts that may be useful:
        <@U05HU5RQRDY>, Manager
        <@U05F2SURXNK>, Architect
        <@U05HMFRAEHL>, UX lead
:speech_balloon: Here is our team channel: <#C0230J1JLC8>
:speech_balloon: Here is our pr channel: <#C024C5UCJ1E>
:rocket: Here is our confluence page: *<https://ctct.atlassian.net/wiki/spaces/CON/overview?homepageId=11469324341| Contacts Confluence Page>*
:rocket: Here are the apps that our team owns: *<https://ctct.atlassian.net/wiki/spaces/CON/pages/11469325765/Apps+Contacts+Team+Owns?atlOrigin=eyJpIjoiN2ZiZWRiMmNhYTY1NDVkYTgwMTk2YTQ0NTQwNTAwYTEiLCJwIjoiY29uZmx1ZW5jZS1jaGF0cy1pbnQifQ| Contacts Owned Apps>*
:rocket: Here are some guides for production issues: *<https://ctct.atlassian.net/wiki/spaces/CON/pages/11469325672/Tools+for+Monitoring+and+Tracking+Down+Contacts+Production+Issues| Tools for Monitoring and Tracking Down Contacts Production Issues>*"""
            
        elif (team == 'EM-UI'):
            text = """:round_pushpin: Some contacts that may be useful:
        <@U05HU5RQRDY>, Engineering Manager
        <@U05F2SURXNK>, Senior Software Engineer
        <@U05HMFRAEHL>, Product Manager
        <@U05HU5RQRDY>, QE Lead
:speech_balloon: Here is our team channel: <#C0229C42K71>
:speech_balloon: Here is our pr channel: <#C028PADH7E2>
:rocket: Here is our confluence page: *<https://ctct.atlassian.net/wiki/spaces/ProdDel/pages/11476180019/EMUI+-+Email+Marketing+UI+and+Services+with+Email+Editors+3GE+CPE+ACE| EM-UI Confluence Page>*
:rocket: Here is our onboarding page: *<https://drive.google.com/drive/folders/0AFKy7P1fHIMtUk9PVA| EM-UI Onboarding>*
"""
            
        elif (team == 'Shared Frameworks'):
            text = """:round_pushpin: Some contacts that may be useful:
        <@U05FJHQ43FW>, Engineering Manager
        <@U05FJHQ43FW>, Product Manager
        <@U05FJHQ43FW>, Scrum Master
        <@U05FJHQ43FW>, QE Lead
:speech_balloon: Here is our team channel: <#C05HV2B1MH9>
:speech_balloon: Here is our pr channel: <#C05JJSD1GP2>
:speech_balloon: Here is our deployments channel: <#C05HV2EMB9R>
:rocket: Here is our confluence page: *<https://ctct.atlassian.net/wiki/spaces/Dev/pages/11487187853/Planning+and+Shared+Frameworks+Team| Shared Frameworks Confluence Page>*
:rocket: Here is our onboarding page: *<https://ctct.atlassian.net/browse/CPLAN-9447| Shared Frameworks Onboarding>*
:rocket: Here are the apps that our team owns: *<https://github.roving.com/search?q=topic%3Aowner-planning+org%3ACampaigns+org%3AES&type=Repositories| Shared Frameworks Owned Apps>*"""
            
        elif (team == 'Team Goose'):
            text = """:round_pushpin: Some contacts that may be useful:
        <@U05HU5RQRDY>, Manager
:rocket: Here is our confluence page: *<https://ctct.atlassian.net/wiki/spaces/CWC/overview?homepageId=11780129822| Team Goose Confluence Page>*
:rocket: Here is our onboarding page: *<https://ctct.atlassian.net/wiki/spaces/CWC/pages/11824726092/Term+Onboarding+Pages| Team Goose Onboarding>*"""
        
        client.chat_postMessage(channel=f'@{user_id}', text=text)