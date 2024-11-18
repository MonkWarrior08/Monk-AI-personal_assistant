import openai
import json

def prepare_training_file(jsonl_data: list) -> str:
    """
    Upload a JSONL file and return the file ID for fine-tuning.
    """
    # Create a temporary JSONL file
    with open("training_data.jsonl", "w") as f:
        for item in jsonl_data:
            json.dump(item, f)
            f.write("\n")
    
    # Upload the file to OpenAI
    try:
        with open("training_data.jsonl", "rb") as f:
            response = openai.File.create(
                file=f,
                purpose="fine-tune"
            )
        return response.id
    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        return None

def finetune_model(
    training_file_id: str,
    model: str = "gpt-4o",
    n_epochs: int = 10,
    batch_size: int = 1,
    learning_rate_multiplier: int = 2,
) -> dict:
    """
    Create a fine-tuning job with essential parameters only.
    """
    params = {
        "training_file": training_file_id,
        "model": model,
        "hyperparameters": {
            "n_epochs": n_epochs,
            "batch_size": batch_size,
            "learning_rate_multiplier": learning_rate_multiplier,
        }
    }
    
    try:
        response = openai.FineTuningJob.create(**params)
        return response
    except Exception as e:
        print(f"Error creating fine-tuning job: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    openai.api_key = "your-api-key-here"
    
    # Example JSONL data format for fine-tuning
    training_data = [
        {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What's the weather like?"},
                {"role": "assistant", "content": "I don't have access to real-time weather data."}
            ]
        },
        # Add more conversation examples here
    ]
    
    # Upload the training file
    file_id = prepare_training_file(training_data)
    
    if file_id:
        # Start fine-tuning
        result = finetune_model(
            training_file_id=file_id,
            model="gpt-4o",
            n_epochs=10,
            batch_size=1,
            learning_rate_multiplier=1
        )
        
        if result:
            print("Fine-tuning job created successfully!")
            print(f"Job ID: {result.id}")
