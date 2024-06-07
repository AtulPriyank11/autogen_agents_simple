# Autogen Demo

## Overview
This demo showcases the simple integration of local Language Model (LLM) applications via multiple agents to accomplish various tasks.

## Features
- Integration with local LLMs (From Hugging Face)
- Setting up Userproxy agent & Assistant agent
- Mapping external function calls to agent chat
- RetrieveAgents with task QA & code as RAG

## Getting Started
### Prerequisites
- Python 3.x
- Transformers library (from Hugging Face)

### Installation
1. Clone the repository:

    ```
    git clone <repository-url>
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

### Usage
1. Navigate to the project directory:

    ```
    cd autogen-demo
    ```

2. Run the main script:

    ```
    python main.py
    ```

## Files
- **main.py**: Main script to run the Autogen demo.
- **agents.py**: Contains the definitions of the Userproxy and Assistant agents.
- **functions.py**: Includes functions for fetching data, generating code snippets, and answering questions.
