import json
import logging
from similarity import SimilarityEngine
from memory import ConversationMemory

# Setup simple logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContextAwareChatbot:
    """
    The core chatbot orchestrator that glues memory, similarity engine and knowledge base.
    """
    def __init__(self, knowledge_base_path):
        self.kb_path = knowledge_base_path
        self.knowledge_base = self._load_knowledge_base()
        
        # Extract questions for the similarity engine corpus
        if self.knowledge_base:
            self.questions = [item["question"] for item in self.knowledge_base]
        else:
            self.questions = []
        
        self.similarity_engine = SimilarityEngine(self.questions)
        
        # Initialize conversation memory to remember last 5 interactions
        self.memory = ConversationMemory(context_window=5)

    def _load_knowledge_base(self):
        """Loads JSON knowledge database."""
        try:
            with open(self.kb_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except Exception as e:
            logger.error(f"Failed to load knowledge base: {e}")
            return []

    def get_response(self, user_text):
        """
        Processes a user message, handles context memory, finds the best response,
        records the interaction, and returns the response details.
        """
        if not self.knowledge_base:
            return {"response": "I have no knowledge base loaded.", "confidence": 0.0, "context_used": ""}
            
        # Get historical context
        context_string = self.memory.get_context()
        logger.info(f"Current Context: {context_string}")
        
        # Match query with the knowledge base questions
        query_to_match = user_text
        
        # Retrieve the best matching predefined knowledge
        best_idx, confidence_score = self.similarity_engine.find_best_match(query_to_match)
        
        # Confidence threshold
        threshold = 0.2
        
        if confidence_score >= threshold:
            answer = self.knowledge_base[best_idx]["answer"]
        else:
            answer = "I'm sorry, I don't have enough confidence to answer that. Could you rephrase your question?"

        # Update Memory
        self.memory.add_message("user", user_text)
        self.memory.add_message("bot", answer)
        
        return {
            "response": answer,
            "confidence": float(confidence_score),
            "context_used": context_string
        }
        
    def reset_session(self):
        """Resets the memory buffer for a new conversation session."""
        self.memory.clear()
