import streamlit as st

def analyze_watermark(text):
    zero_width_chars = {
        'Zero Width Space (U+200B)': '\u200B',
        'Zero Width Non-Joiner (U+200C)': '\u200C',
        'Zero Width Joiner (U+200D)': '\u200D',
        'Zero Width No-Break Space (U+FEFF)': '\uFEFF'
    }

    total_length = len(text)
    found = False
    results = []

    for name, char in zero_width_chars.items():
        count = text.count(char)
        if count > 0:
            found = True
            frequency = (count / total_length) * 100 if total_length > 0 else 0
            results.append(f"{name} found {count} times. Frequency: {frequency:.2f}%")

    if found:
        st.write("Zero-width characters detected:")
        st.write(results)
    else:
        st.write("No zero-width characters found.")

def main():
    st.title("Watermark Analyzer")

    watermarked_text = st.text_input("Enter the text to analyze")

    if st.button("Analyze Text"):
        if watermarked_text:
            analyze_watermark(watermarked_text)
        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    main()