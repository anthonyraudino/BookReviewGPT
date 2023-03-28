import configparser
import csv
import openai

# Read the OpenAI API key from the apikey.cfg file
config = configparser.ConfigParser()
config.read("apikey.cfg")
openai.api_key = config.get("openai", "api_key")

# Define the OpenAI prompt template
prompt = "Write a book overview with the following written sections, using the specific list format: Book Summary: A summary of {book_title} by {book_author} in 1000 words or less including summaries of key characters, locations, plot lines and a final conclusion on the book. Pivotal Moment: List what is the most pivotal chapter of the book and why you think it is the most pivotal chapter. Key Quote: Quote a line from the book that would be the most poignant quote."

# Define the CSV input and output file paths
input_file_path = "book_list.csv"
output_file_path = "book_reviews.csv"

# Define the OpenAI engine ID to use for generating summaries
engine_id = "text-davinci-003"

# Define a function to generate a book summary, pivotal moment, and key quote given a book title and author
def generate_book_review(book_title, book_author):
    # Replace the prompt variables with the provided book title and author
    prompt_with_book = prompt.format(book_title=book_title, book_author=book_author)

    print(f"Generating review for {book_title} by {book_author}...")

    # Generate the book review using the OpenAI API
    response = openai.Completion.create(
        engine=engine_id,
        prompt=prompt_with_book,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the generated book summary, pivotal moment, and key quote from the OpenAI API response
    generated_text = response.choices[0].text.strip().split("\n")
    book_summary = ""
    pivotal_moment = ""
    key_quote = ""

    for line in generated_text:
        if line.startswith("Book Summary:"):
            book_summary = line.replace("Book Summary:", "").strip()
        elif line.startswith("Pivotal Moment:"):
            pivotal_moment = line.replace("Pivotal Moment:", "").strip()
        elif line.startswith("Key Quote:"):
            key_quote = line.replace("Key Quote:", "").strip()

    print(f"Review generated for {book_title} by {book_author}.")

    # Return the generated book review
    return book_summary, pivotal_moment, key_quote

# Open the CSV input file and create a CSV output file
with open(input_file_path, mode="r", newline="") as input_file, open(output_file_path, mode="w", newline="") as output_file:
    # Create CSV reader and writer objects
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write the header row to the output CSV file
    writer.writerow(["Title", "Author", "Summary", "Pivotal Moment", "Key Quote"])

    # Iterate over each row in the input CSV file
    for row in reader:
        # Extract the book title and author from the current row
        book_title = row[0]
        book_author = row[1]

        # Generate the book review using the OpenAI API
        book_summary, pivotal_moment, key_quote = generate_book_review(book_title, book_author)

        # Write the book title, author, book summary, pivotal moment, and key quote to the output CSV file
        writer.writerow([book_title, book_author, book_summary, pivotal_moment, key_quote])
       
