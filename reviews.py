
import csv
import openai
openai.api_key = "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"  # Replace with your API key

def generate_summary(book_title, book_author):
    # Your script to generate the book review summary using ChatGPT

    # Example code using OpenAI's GPT-3 API to generate text
    prompt = f"Please generate a summary for the book {book_title} by {book_author}."
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    summary = response.choices[0].text.strip()
    
    # Return the summary for writing to CSV file
    return summary

# Open CSV file containing book titles and authors
with open('book_list.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    books = []
    for row in csv_reader:
        books.append({"title": row['Title'], "author": row['Author']})

# Generate summaries for each book and write to CSV file
with open('book_summaries.csv', mode='w') as csv_file:
    fieldnames = ['Title', 'Author', 'Summary']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for book in books:
        title = book["title"]
        author = book["author"]
        summary = generate_summary(title, author)
        writer.writerow({'Title': title, 'Author': author, 'Summary': summary})
