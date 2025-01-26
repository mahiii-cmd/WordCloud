# app.py
import streamlit as st
import wordcloud
import matplotlib.pyplot as plt

def generate_wordcloud(text):
    """Generate a word cloud from input text."""
    wordcloud_obj = wordcloud.WordCloud(
        width=800, 
        height=400, 
        background_color='white'
    ).generate(text)
    
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud_obj, interpolation='bilinear')
    plt.axis('off')
    return plt

def main():
    st.title('WordCloud Generator')
    
    # Text input
    text = st.text_area('Enter your text here:', 
                        'Paste your text to generate a word cloud. '
                        'The more frequent a word, the larger it will appear.')
    
    if st.button('Generate WordCloud'):
        if text.strip():
            # Generate and display word cloud
            word_cloud_plot = generate_wordcloud(text)
            st.pyplot(word_cloud_plot)
        else:
            st.warning('Please enter some text')

if __name__ == '__main__':
    main()
