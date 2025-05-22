from transformers import AutoModelForSequenceClassification, AutoTokenizer

def publish_model(model_dir, model_repo_name, huggingface_token):
    model = AutoModelForSequenceClassification.from_pretrained(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    
    print(f"Publishing model to {model_repo_name} with token {huggingface_token}")

    model.push_to_hub(model_repo_name, token=huggingface_token)
    tokenizer.push_to_hub(model_repo_name, token=huggingface_token)
