# from slackclient import SlackClient
from slack_sdk import WebClient
from config import get_env
from slack_sdk.errors import SlackApiError


class SlackHelper:

    def __init__(self):
        self.slack_token = get_env('SLACK_TOKEN')
        # formerly known as slackclient
        self.slack_client = WebClient(token=self.slack_token)
        self.slack_channel = get_env('SLACK_CHANNEL')

    def post_message(self, msg, recipient):
        try:
            return self.slack_client.chat_postMessage(
                channel=recipient,
                text=msg,
            )
        except SlackApiError as e:
            print(f"Error posting message: {e}")

        # return self.slack_client.api_call(
        #     "chat.postMessage",
        #     channel=recipient,
        #     text=msg,
        #     as_user=True
        # )

    def post_message_to_channel(self, msg):
        try:
            return self.slack_client.chat_postMessage(
                channel=self.slack_channel,
                text=msg,
            )
        except SlackApiError as e:
            print(f"Error posting message: {e}")

        # return self.slack_client.api_call(
        #     "chat.postMessage",
        #     channel=self.slack_channel,
        #     text=msg,
        #     username='Ranti',
        #     parse='full',
        #     as_user=False
        # )

        # additional methods to interact with slack
    def file_upload(self, file_content, file_name, file_type, title=None, ):
        return self.slack_client.api_call(
            "files.upload",
            channels=self.slack_channel,
            content=file_content,
            filename=file_name,
            filetype=file_type,
            initial_comment='{} Log File'.format(file_name),
            title=title
        )

    def user_info(self, uid):
        return self.slack_client.users_info(
            user=uid
        )
