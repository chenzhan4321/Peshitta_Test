
    # Open the input file
import numpy as np
import pandas as pd

# Define the mapping from transcription to Syriac glyphs
transcription_to_syriac = {
    '>': 'ܐ',
    'B': 'ܒ',
    'G': 'ܓ',
    'D': 'ܕ',
    'H': 'ܗ',
    'W': 'ܘ',
    'Z': 'ܙ',
    'X': 'ܚ',
    'V': 'ܛ',
    'J': 'ܝ',
    'K': 'ܟ',
    'L': 'ܠ',
    'M': 'ܡ',
    'N': 'ܢ',
    'S': 'ܣ',
    '<': 'ܥ',
    'P': 'ܦ',
    'Y': 'ܨ',
    'Q': 'ܩ',
    'R': 'ܪ',
    'C': 'ܫ',
    'T': 'ܬ',
    '^' : '',
    '"': '',

}

def transcribe_to_syriac(transcription):
    """
    Transcribe a given Latin transcription into Syriac glyphs.

    Args:
    transcription (str): A string with Latin transcription.

    Returns:
    str: A string with Syriac glyphs.
    """
    syriac_text = ''.join(transcription_to_syriac.get(char, char) for char in transcription)
    return syriac_text

def transcribe_to_latin(syriac_text):
    """
    Transcribe a given Syriac text into Latin transcription.

    Args:
    syriac_text (str): A string with Syriac glyphs.

    Returns:
    str: A string with Latin transcription.
    """
    latin_transcription = ''.join(syriac_to_transcription.get(char, char) for char in syriac_text)
    return latin_transcription

df = pd.read_csv('s2-in.txt', sep='\t')
df.head()
text_combined = df['Text'].str.cat(sep=' ')
print(text_combined[:100])
    # Process the content
processed_content = transcribe_to_syriac(text_combined)
print(processed_content[:100])
    # Write the processed content to the output file
with open('result.txt', 'w') as output_file:
    output_file.write(processed_content)