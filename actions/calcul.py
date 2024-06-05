import yaml
import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the test data
with open('../train_test_split/test_data.yml', 'r') as file:
    test_data = yaml.safe_load(file)

# Extract true intents and texts
true_intents = []
texts = []

for example in test_data['nlu']:
    if 'intent' in example:
        intent = example['intent']
        examples = example['examples'].strip().split('\n')
        for text in examples:
            if text.strip():  # Check if the text is not empty
                true_intents.append(intent)
                texts.append(text.strip('- ').strip())

# Load the predictions from the intent report
with open('../results/intent_report.json', 'r') as file:
    report_data = json.load(file)

# Print the structure of report_data for debugging
print("Structure of report_data:")
print(json.dumps(report_data, indent=2))

# Extract predicted intents
predicted_intents = []
for text in texts:
    matched = False
    for intent, data in report_data.items():
        if isinstance(data, dict) and 'predictions' in data:
            for prediction in data['predictions']:
                if prediction['text'].strip() == text.strip():
                    predicted_intents.append(prediction['intent'])
                    matched = True
                    break
        if matched:
            break
    if not matched:
        predicted_intents.append('unknown')  # Handle cases where no prediction is found

# Calculate metrics
accuracy = accuracy_score(true_intents, predicted_intents)
precision = precision_score(true_intents, predicted_intents, average='weighted', zero_division=0)
recall = recall_score(true_intents, predicted_intents, average='weighted', zero_division=0)
f1 = f1_score(true_intents, predicted_intents, average='weighted', zero_division=0)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
