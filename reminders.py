# reminders.py
from slack_bolt import App
from env import client
from slack.errors import SlackApiError

reminder_list = [
    '. Payroll Set Up: Check your Gmail inbox for an email from PEO Canada and return the necessary forms by the end of this week.\n',
    '. HR Training Courses: Please check your Gmail inbox for emails regarding training assignments that have been assigned to you.\n',
    '. Workday Timecard: Enter your daily work hours on Workday to ensure your paycheck will be accurate for the pay date. Remember to submit your weekly timecards by Friday at 2 pm! \n'
]

def schedule_message(client, user_id):
    message = ':two: Hey there new hire! Here is a list of onboarding tasks to be completed within the first week at SlackMate.\n'
    task = 1
    for msg in reminder_list:
        message = message + '        📝 ' + str(task) + msg
        task = task + 1
    print(message)
    client.chat_postMessage(
        channel=user_id,
        text=message
    )

date_picker = {
    "blocks": [
        {
            "type": "input",
            "element": {
                "type": "datetimepicker",
                "action_id": "datetime_input",
                "initial_date_time": 1690003200
            },
            "label": {
                "type": "plain_text",
                "text": "Pick a date & time for the deadline"
            }
        }
    ]
}

def schedule_date(app: App):
    @app.command("/pick-date")
    def pick_date(ack, say, command):
        user_id = command["user_id"]
        ack()
        response = client.chat_postMessage(
            channel=f'{user_id}',
            blocks=date_picker["blocks"]
        )