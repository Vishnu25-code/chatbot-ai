# Lightweight Context-Aware AI Chatbot

A minimal, memory-enabled AI chatbot built for portfolio demonstrations. This project avoids huge pretrained language models (LLMs) and instead relies on lightweight NLP techniques (TF-IDF vectorization and Cosine Similarity) to ensure rapid deployment, fast responses, and a completely self-contained architecture. 

It stays far beneath the minimum size limits for source code submissions.

## Features

1. **Lightweight Context Memory**: Keeps a rolling window of recent queries, storing only essential context.
2. **Semantic Similarity Engine**: Matches meanings using standard `scikit-learn` natural language algorithms (TF-IDF & Cosine Similarity) without requiring huge language model downloads.
3. **Extendable JSON Database**: No need for complex SQL or graph databases. Fast dictionary lookups!
4. **Clean Web UI**: A beautiful, modern chat UI driven by vanilla JS and CSS without heavy framework overhead.

## Architecture Structure

- `app.py`: The main Flask REST server and page renderer.
- `chatbot.py`: The brain that strings together memory and search.
- `memory.py`: Tracks rolling session states using N-sized message history.
- `similarity.py`: Handles vector space models to assign confidence similarity scores.
- `knowledge_base.json`: The data source you can edit independently.

## Instructions to Run

1. **Setup a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Start the Backend**:
   ```bash
   python app.py
   ```
4. **Visit the Frontend**:
   Open a web browser and go to `http://localhost:5000`

## Example Queries

Try interacting with the bot by phrasing these differently to test its semantic matching powers:
- *"Who exactly are you?"* (Tests knowledge ID 0)
- *"Tell me how you keep track of messages."* (Tests knowledge ID 1)
- *"Do you understand sentence closeness?"* (Tests knowledge ID 3)
- *"Make me laugh."* (Tests knowledge ID 5)
- *"How large are your files for deployment?"* (Tests knowledge ID 6)
