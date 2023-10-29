import streamlit as st

def caesar_cipher(text, shift, direction):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift * direction) % 26 + base)
        else:
            result += char
    return result

def main():
    st.title("Caesar Cipher App")
    text = st.text_area("Enter your text:")
    shift = st.slider("Select the shift value:", 1, 25, 3)
    direction = st.radio("Select the operation:", ["Encrypt", "Decrypt"])

    if st.button("Submit"):
        if text:
            if direction == "Encrypt":
                result = caesar_cipher(text, shift, 1)
                st.success(f"Encrypted text: {result}")
            else:
                result = caesar_cipher(text, shift, -1)
                st.success(f"Decrypted text: {result}")
        else:
            st.error("Please enter some text.")

if __name__ == "__main__":
    main()
