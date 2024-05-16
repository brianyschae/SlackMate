# bot.py
import os
from slack_bolt import App
from events import register_event_handlers
from onboarding import onboarding_process_handlers
from goal_setting import goal_tracker_handlers
from reminders import schedule_date
from env import env_path

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ['SLACK_TOKEN'],
    signing_secret=os.environ['SIGNING_SECRET']
)

# Register event handlers
register_event_handlers(app)

# Register onboarding handlers
onboarding_process_handlers(app)

# Register goal-tracker handlers
goal_tracker_handlers(app)

schedule_date(app)