class ConversationMemory:
    """
    Handles context memory for the chatbot session.
    Keeps track of the last N messages to maintain a lightweight context window.
    """
    def __init__(self, context_window=5):
        self.context_window = context_window
        self.history = []

    def add_message(self, role, content):
        """
        Adds a message to the history. 
        Role should be 'user' or 'bot'.
        """
        self.history.append({"role": role, "content": content})
        
        # Truncate history to keep only the last N context window limit
        if len(self.history) > self.context_window * 2: # pairs of user/bot interactions
            self.history = self.history[-(self.context_window * 2):]

    def get_context(self):
        """
        Returns the current context window as a flat text string.
        """
        context_texts = [f"{msg['role']}: {msg['content']}" for msg in self.history]
        return " | ".join(context_texts)

    def get_history(self):
        """
        Returns the structured history.
        """
        return self.history

    def clear(self):
        """
        Clears the conversation memory.
        """
        self.history = []
