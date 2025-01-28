import json
from transformers import LlamaForCausalLM, LlamaTokenizer, Trainer, TrainingArguments
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import Dataset

model_name = "meta-llama/Llama-3.1-8B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_name)

# Load the dataset
with open("labeled_cpp_dataset.json", "r") as f:
    data = json.load(f)

dataset = Dataset.from_list(data)

def preprocess_function(examples):
    inputs = []
    for i in range(len(examples['label'])):
        inputs.append(f"<label>{examples['label'][i]}</label><data>{examples['data'][i]}</data>")
    model_inputs = tokenizer(inputs, max_length=512, truncation=True, padding="max_length")
    model_inputs["labels"] = model_inputs["input_ids"].copy()  # Set labels to the input IDs
    return model_inputs

tokenized_dataset = dataset.map(
    preprocess_function,
    batched=True,
    num_proc=1,  # Adjust based on your resources
    remove_columns=dataset.column_names,
    desc="Running tokenizer on dataset",
)


training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    gradient_accumulation_steps=1,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    evaluation_strategy="no",
    save_strategy="epoch",
    save_total_limit=0,
    load_best_model_at_end=False,
    push_to_hub=False,
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()

# Save the model and tokenizer
model.save_pretrained("./trained_model") # Choose a directory for your trained model
tokenizer.save_pretrained("./trained_model")
