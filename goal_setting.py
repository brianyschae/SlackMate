from slack_bolt import App
from env import client

def goal_tracker_handlers(app: App):
    # Dictionary to store the user's goals
    user_goals = {}

    # Command to add a goal
    @app.command("/add-goal")
    def add_goal_command(ack, say, command):
        user_id = command["user_id"]
        goal = command["text"]

        # Add the goal to the user's unfinished goals list
        if user_id not in user_goals:
            user_goals[user_id] = {
                "unfinished_goals": [],
                "finished_goals": []
            }
        user_goals[user_id]["unfinished_goals"].append(goal)

        ack()
        say(f"Goal added: {goal}")

    # Command to list all goals
    @app.command("/list-goals")
    def list_goals_command(ack, say, command):
        user_id = command["user_id"]

        # Retrieve the user's unfinished and finished goals
        unfinished_goals = user_goals.get(user_id, {}).get("unfinished_goals", [])
        finished_goals = user_goals.get(user_id, {}).get("finished_goals", [])
        ack()
        text = "--------------------------------------------------\n"
        text = text + ":memo: GOAL SUMMARY: \n"
        text = text + ":round_pushpin: TODO: \n"
        if unfinished_goals:
            emoji = "        :point_right:"
            unfinished_goals_list = [f"{emoji} {item}" for item in unfinished_goals]
            text = text + "\n".join(unfinished_goals_list)
        text = text + ("\n\n:round_pushpin: DONE: \n")
        if finished_goals:
            emoji = "        :white_check_mark:"
            finished_goals_list = [f"{emoji} {item}" for item in finished_goals]
            text = text + "\n".join(finished_goals_list)
        say(text)

    # Command to mark a goal as completed
    @app.command("/complete-goal")
    def complete_goal_command(ack, say, command):
        user_id = command["user_id"]
        goal = command["text"]

        # Check if the goal exists in the user's unfinished goals list
        if (
            user_id in user_goals
            and goal in user_goals[user_id]["unfinished_goals"]
        ):
            # Move the goal from unfinished to finished goals list
            user_goals[user_id]["unfinished_goals"].remove(goal)
            user_goals[user_id]["finished_goals"].append(goal)

            ack()
            say(f"Goal marked as completed: {goal}")
        else:
            ack()
            say("Goal not found.")