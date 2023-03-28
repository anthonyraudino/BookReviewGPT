import csv
import pytest
import os

import reviews


@pytest.fixture(scope="module")
def sample_input_file(tmpdir_factory):
    # Create a temporary input file with some sample data
    filename = tmpdir_factory.mktemp("data").join("input.csv")
    with open(filename, mode="w", encoding="utf-8", newline="") as input_file:
        writer = csv.writer(input_file)
        writer.writerow(["Title", "Author"])
        writer.writerow(["The Great Gatsby", "F. Scott Fitzgerald"])
        writer.writerow(["To Kill a Mockingbird", "Harper Lee"])
    yield filename


def test_generate_book_summary():
    # Test generating a book summary
    book_title = "The Great Gatsby"
    book_author = "F. Scott Fitzgerald"
    book_summary = book_reviews.generate_book_summary(book_title, book_author)
    assert isinstance(book_summary, str)


def test_process_book_list(sample_input_file):
    # Test processing a sample book list
    output_file_path = os.path.join(os.path.dirname(sample_input_file), "output.csv")
    book_reviews.process_book_list(sample_input_file, output_file_path)
    assert os.path.isfile(output_file_path)
