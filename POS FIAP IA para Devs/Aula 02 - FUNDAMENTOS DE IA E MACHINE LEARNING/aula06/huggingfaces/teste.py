from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

nome_repo = "lucasbiason/curso-fiap-huggingface"

tokenizer = AutoTokenizer.from_pretrained(nome_repo)
model = AutoModelForSequenceClassification.from_pretrained(nome_repo)

class_labels = {0: "Negative", 1: "Positive"}

text = "Este é um exemplo para demonstrar como publicar um modelo."

inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

logits = outputs.logits
predicted_class_id = torch.argmax(logits).item()

predicted_class_label = class_labels[predicted_class_id]

print(f"Texto: {text}")
print(f"Classe prevista: {predicted_class_label}")
