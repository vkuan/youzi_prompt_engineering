# Victor Kuan
# March 2024
import time
import random
import csv
from csv import writer
import pandas as pd

def clean_data():
#   df = pd.read_csv('test_data - test_youzi_prompts.csv')
#   print(df)

# Open the CSV file
    with open('test_data - test_youzi_prompts.csv', newline='', mode='r') as csvfile, \
        open('new_data_2.csv', newline='', mode='w', encoding='utf-8') as outfile:
        # Create a csv reader object
        reader = csv.reader(csvfile)
        writer = csv.writer(outfile)

        

        # Iterate over each row in the csv file
        for row in reader:
            if row:  # Check if the row is not empty
                # Print the second column of the current row
                # print(row[1])
                # Split the text into parts using the prompt numbers as delimiters

                text = row[1]

                if(len(row[1]) < 10):
                    continue
                
                convo_starter_1 = find_middle_text("Chinese convo starter #1:", "English translation #1:", text)
                english_translate_1 = find_middle_text("English translation #1:", "Related Chinese media recommendation #1:", text)
                media_1 = find_middle_text("Related Chinese media recommendation #1:", "One vocab word that is relevant to use in the response #1:", text)
                vocab_1_1 = find_middle_text("One vocab word that is relevant to use in the response #1:", "Second vocab word that is relevant to use in the response #1:", text)
                vocab_2_1 = find_middle_text("Second vocab word that is relevant to use in the response #1:", "Third vocab word that is relevant to use in the response #1:", text)
                vocab_3_1 = find_middle_text("Third vocab word that is relevant to use in the response #1:", "Funny Chinese slang/phrase that can be used in the response #1:", text)
                funny_1 = find_middle_text("Funny Chinese slang/phrase that can be used in the response #1:", "Example response #1:", text)
                example_response_1 = find_middle_text("Example response #1:", "English translation of response #1:", text)
                example_response_translate_1 = find_middle_text("English translation of response #1:", "Follow up Chinese convo starter #2:", text)

                convo_starter_2 = find_middle_text("Chinese convo starter #2:", "English translation #2:", text)
                english_translate_2 = find_middle_text("English translation #2:", "Related Chinese media recommendation #2:", text)
                media_2 = find_middle_text("Related Chinese media recommendation #2:", "One vocab word that is relevant to use in the response #2:", text)
                vocab_1_2 = find_middle_text("One vocab word that is relevant to use in the response #2:", "Second vocab word that is relevant to use in the response #2:", text)
                vocab_2_2 = find_middle_text("Second vocab word that is relevant to use in the response #2:", "Third vocab word that is relevant to use in the response #2:", text)
                vocab_3_2 = find_middle_text("Third vocab word that is relevant to use in the response #2:", "Funny Chinese slang/phrase that can be used in the response #2:", text)
                funny_2 = find_middle_text("Funny Chinese slang/phrase that can be used in the response #2:", "Example response #2:", text)
                example_response_2 = find_middle_text("Example response #2:", "English translation of response #2:", text)
                example_response_translate_2 = find_middle_text("English translation of response #2:", "Final follow up Chinese convo starter #3:", text)

                convo_starter_3 = find_middle_text("Final follow up Chinese convo starter #3:", "English translation #3:", text)
                english_translate_3 = find_middle_text("English translation #3:", "Related Chinese media recommendation #3:", text)
                media_3 = find_middle_text("Related Chinese media recommendation #3:", "One vocab word that is relevant to use in the response #3:", text)
                vocab_1_3 = find_middle_text("One vocab word that is relevant to use in the response #3:", "Second vocab word that is relevant to use in the response #3:", text)
                vocab_2_3 = find_middle_text("Second vocab word that is relevant to use in the response #3:", "Third vocab word that is relevant to use in the response #3:", text)
                vocab_3_3 = find_middle_text("Third vocab word that is relevant to use in the response #3:", "Funny Chinese slang/phrase that can be used in the response #3:", text)
                funny_3 = find_middle_text("Funny Chinese slang/phrase that can be used in the response #3:", "Example response #3:", text)
                example_response_3 = find_middle_text("Example response #3:", "English translation of response #3:", text)

                start_substring = "English translation of response #3:"

                # Find the start index of the substring
                start_index = text.find(start_substring)

                example_response_translate_3 = ""
                # Check if the substring was found
                if start_index != -1:
                    # Slice the string from the start index to the end
                    example_response_translate_3 = text[start_index:]
                # print(example_response_translate_3)

                new_data = [convo_starter_1, english_translate_1, media_1, vocab_1_1, vocab_2_1, vocab_3_1, funny_1, example_response_1, example_response_translate_1, convo_starter_2, english_translate_2, media_2, vocab_1_2, vocab_2_2, vocab_3_2, funny_2, example_response_2, example_response_translate_2, convo_starter_3, english_translate_3, media_3, vocab_1_3, vocab_2_3, vocab_3_3, funny_3, example_response_3, example_response_translate_3]
                modified_row = row + new_data
        
                # Write the modified row to the new CSV file
                writer.writerow(modified_row)


def find_middle_text(start_string, end_string, text):
    # Define the start and end markers
    start_marker = start_string
    end_marker = end_string

    # Find the start index and adjust it to get the actual starting point of the desired text
    start_index = text.find(start_marker) + len(start_marker)

    # Find the end index
    end_index = text.find(end_marker)

    # Extract the substring
    extracted_text = text[start_index:end_index].strip()

    # Print the result
    # print(extracted_text)
    return(extracted_text)



clean_data()