import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#image = Image.open('dna-logo.jpg')

#st.image(image, use_column_width=True)
st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")

st.header ('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=350)
sequence = st.text_area("Sequence input", sequence_input, height=150)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)
sequence

st.header('INPUT (DNA Query')
sequence
st.header('OUTPUT (DNA Nucleotide Count)')

st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('C',seq.count('C')),
        ('G',seq.count('G')),
        ('T',seq.count('T'))
    ])
    return d

X = DNA_nucleotide_count(sequence)
X_label = list(X)
X_values = list(X.values())
X