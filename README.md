# SlackMate

![image](https://github.com/brianyschae/SlackMate/assets/49376205/a3522148-a694-46b7-be70-84aa0e35fe4d)

![image](https://github.com/brianyschae/SlackMate/assets/49376205/1ce450dc-00fb-49c2-b165-747d77300657)


## File Structure
- **bot.py** handles the app initialization and registers event and command handlers.
- **events.py** contains event handlers.
- **commands.py** contains command handlers.
- **socket_handler.py** initializes the Socket Mode handler using the **app** instance from **bot.py**.


## Run Locally

1. Install python3 and pip3

2. Make sure you have all the required dependencies installed. You can use pip to install the necessary packages by running the following command in your terminal or command prompt

```bash
  pip3 install slack_bolt pathlib dotenv
```

3. Create an app in slack-api and set up all the configurations and permissions

4. Set up the environment variables by creating a .env file in the same directory as your code (bot.py, events.py, commands.py, and socket_handler.py). Inside the .env file, add the following key-value pairs:

```bash
SLACK_TOKEN=<your_slack_token>
SIGNING_SECRET=<your_signing_secret>
SOCKET_TOKEN=<your_socket_token>
```

5. Initialize the Socket Mode handler and start the app.

```bash
  python3 socket_handler.py
```

