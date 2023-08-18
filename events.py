# events.py
from slack_bolt import App
from reminders import schedule_message
from env import client

def register_event_handlers(app: App):
    @app.event("member_joined_channel")
    def ask_for_introduction(event, say):
        user_id = event["user"]
        text = f"Welcome to SlackMate, <@{user_id}>! 🎉\n:one: These are some of the commands to get you started.\n        :keyboard: Use command `/start` to start the onboarding process!\n        :keyboard: Use command `/add-goal` to add a goal.\n        :keyboard: Use command `/list-goals` to list all your existing goals.\n        :keyboard: Use command `/complete-goal` to finish and remove your goal.\n        :keyboard: Use command `/pick-date` to set a schedule for the task."
        say(text=text, channel=f'@{user_id}')
        # Schedule messages
        schedule_message(client, f'{user_id}')
