import argparse
from transformers import pipeline

# Load the BART summarization model
summariser = pipeline("summarization", model="facebook/bart-large-cnn")

def summarise_text(text: str, max_length: int=50, min_length: int=25) -> str:
    """Takes input text and returns a summary with specified length."""
    summary = summariser(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

def main():
    # Setup argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description="Summarise a given text using BART model.")
    parser.add_argument("text", type=str, help="Text to be summarised.")
    parser.add_argument("--max_length", type=int, default=50, help="Maximum length of the summary.")
    parser.add_argument("--min_length", type=int, default=25, help="Minimum length of the summary.")
    
    args = parser.parse_args()

    # Get the summary
    summary = summarise_text(args.text, args.max_length, args.min_length)
    print("Summary:", summary)

if __name__ == "__main__":
    main()
