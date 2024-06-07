class UserProxyAgent:
    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        return f"UserProxyAgent ({self.name}): {message}"

class AssistantAgent:
    def __init__(self, name):
        self.name = name

    def receive_message(self, message):
        return f"AssistantAgent ({self.name}): Processed message - {message}"
