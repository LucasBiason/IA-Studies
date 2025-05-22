import os
from dotenv import load_dotenv
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def load_config():
    load_dotenv()
    config = {
        "model_name": os.getenv("MODEL_NAME"),
        "model_repo_name": "lucasbiason/curso-fiap-huggingface",
        "huggingface_token": os.getenv("HUGGINGFACE_TOKEN"),
    }
    return config

def load_model_and_tokenizer(model_name):
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

def main():
    config = load_config()
    print("Config loaded:", config)
    
    model, tokenizer = load_model_and_tokenizer(config["model_name"])
    model.save_pretrained("./simple_model")
    tokenizer.save_pretrained("./simple_model")

    from publish import publish_model
    publish_model("./simple_model", config["model_repo_name"], config["huggingface_token"])

if __name__ == "__main__":
    main()
