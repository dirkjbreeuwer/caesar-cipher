"""
This Streamlit app provides a simple interface for encrypting and decrypting text using the Caesar Cipher algorithm.
"""

import streamlit as st

def caesar_cipher(input_text, shift_val, direction_val="encrypt"):
    """
    Apply the Caesar Cipher algorithm to a given text.

    Args:
    input_text (str): The text to be encrypted or decrypted.
    shift_val (int): The shift value to be used in the Caesar Cipher algorithm.
    direction_val (int): The direction of the shift. Use 1 for encryption and -1 for decryption.

    Returns:
    str: The encrypted or decrypted text.
    """
    result_text = ""
    for char in input_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result_text += chr((ord(char) - base + shift_val * direction_val) % 26 + base)
        else:
            result_text += char
    return result_text

def try_all_shifts(input_text):
    """
    Try all possible shift values to decrypt a given text using the Caesar Cipher algorithm.

    Args:
    input_text (str): The text to be decrypted.

    Returns:
    list of tuple: A list of tuples where each tuple contains a shift value and the corresponding decrypted text.
    """
    results = []
    for shift in range(26):
        decrypted_text = caesar_cipher(input_text, shift, direction_val=-1)
        results.append((shift, decrypted_text))
    return results

st.title("Caesar Cipher App")

input_text = st.text_area("Enter text:")
input_shift = st.number_input("Enter shift value:", min_value=0, max_value=25, value=0)
direction = st.radio("Choose operation:", ["Encrypt", "Decrypt"])

if direction == "Encrypt":
    encrypted_text = caesar_cipher(input_text, input_shift, direction_val=1)
    st.write("Encrypted text:", encrypted_text)
else:
    decrypted_text = caesar_cipher(input_text, input_shift, direction_val=-1)
    st.write("Decrypted text:", decrypted_text)

st.header("Want to decrypt a text but don't know the shift value?")

subset_text = st.text_area("Enter a small subset of text:")
start_button = st.button("Start", disabled=not subset_text)
if start_button:
    all_shifts_results = try_all_shifts(subset_text)
    for shift_val, output_text in all_shifts_results:
        st.write(f"Shift {shift_val}: {output_text}")
