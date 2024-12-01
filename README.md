# Personal-AI-Assistant
Monk-AI is a sophisticated personal assistant system that combines advanced AI capabilities with dynamic personality adaptation, creating meaningful and contextually appropriate interactions. The system is trained on extensive real-world interaction data, incorporating psychological insights, communication patterns, and practical problem-solving scenarios. This comprehensive training enables Monk-AI to serve as a versatile assistant that can seamlessly adapt its personality and approach to match user preferences and situational requirements, making it an ideal companion for various aspects of daily life.

## Setup Instructions

### 1. Installation

1. Clone this repository:
```bash
git clone https://github.com/MonkWarrior08/DeepTutor-AI.git
cd DeepTutor-AI
```

2. Install dependencies using the requirements file:
```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

1. Create a `.env` file in the project root:
```bash
touch .env  # macOS/Linux
# or manually create .env file in Windows
```

2. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```


### 3. OpenAI Setup

1. Create an OpenAI account and obtain an API key from [OpenAI Platform](https://platform.openai.com/)
2. Create a fine-tuning job with the following parameters:
   - Epochs: 10
   - Learning rate multiplier: 2
   - Batch size: 1

### 4. Knowledge Base Preparation
- routine plan
- discussion topic
- books
- etc..

### 5. Vector Store Creation
1. Create vector store storage on the OpenAI plaftform
2. Upload the knowledge base to the created vector store

### 6. Assistant Configuration
1. Create a new assistant
2. Select the fine-tuned model
3. Connect the vector storage
4. Save the assistant ID

### 7. Application Setup
1. Open `main.py`
2. Replace the empty `assistant_id` variable with your assistant ID
3. Run the application:
```bash
python main.py
```

## Usage
- Exit by typing 'quit', 'exit', or 'bye'


## License

This project is licensed under the MIT License.
