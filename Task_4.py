import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from transformers import pipeline

def generate_text(prompt):
    generator = pipeline("text-generation", model="gpt2")

    result = generator(
        prompt,
        max_length=100,
        num_return_sequences=1,
        truncation=True
    )

    return result[0]['generated_text']


def main():
    print("---- AI Text Generation Model ----")

    prompt = input("Enter a topic or prompt: ")

    print("\nGenerating text...\n")

    generated = generate_text(prompt)

    print("Generated Paragraph:\n")
    print(generated)


if __name__ == "__main__":
    main()
