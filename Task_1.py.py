from transformers import pipeline

def summarize_text(text):
    """
    Function to summarize long text using a pretrained NLP model
    """

    # Load summarization pipeline
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Generate summary
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

    return summary[0]['summary_text']


def main():
    print("---- AI Text Summarization Tool ----")

    choice = input("1. Enter text manually\n2. Load text from file\nChoose option (1/2): ")

    if choice == "1":
        text = input("\nPaste your article:\n")

    elif choice == "2":
        filename = input("Enter file name: ")
        try:
            with open(filename, "r", encoding="utf-8") as file:
                text = file.read()
        except:
            print("Error reading file.")
            return
    else:
        print("Invalid choice.")
        return

    print("\nGenerating summary...\n")

    summary = summarize_text(text)

    print("---- SUMMARY ----\n")
    print(summary)


if __name__ == "__main__":
    main()
