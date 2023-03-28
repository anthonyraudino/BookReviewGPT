<img src="https://repository-images.githubusercontent.com/620076303/9d822a46-8a68-4328-9468-3fa886102f84"
     alt="Book Review GPT Logo"
     style="width:350px; float: left; margin-right: 10px;" />
     
# Book Review GPT
A Python application that reads a list of books and authors from a CSV and gets OpenAI's text-davinci-003 engine to summarize the book, provide a key quote and recommend a specific chapter, then dump the summaries to a outputted CSV file.

 ## How to Use
-- Add your OpenAI API key to the apikey.sample.cfg file and rename to apikey.cfg

-- Create your list of books to review in a CSV file with the header rows "Title" and "Author", save as book_list.csv in the same folder as the Python app

-- Run the app via terminal and OpenAI will summarize and save the summaries to a CSV file
