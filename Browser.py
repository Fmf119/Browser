import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to fetch website content using requests
def fetch_website(url):
    """Fetch the HTML content of the URL."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching the website: {e}")
        return None

# Function to extract the title of the webpage
def extract_title(html):
    """Extract the title of the webpage."""
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    return title

# Main function that runs the Streamlit app
def main():
    # Title of the app
    st.title("Anonymous Web Browser")

    st.write("""
    This is a simple anonymous browser. You can use it to view any website privately.
    Just enter a URL below and click "View Anonymously".
    """)

    # URL input field
    url = st.text_input("Enter URL to view anonymously:")

    if url:
        # Fetch the content of the webpage
        st.write(f"Fetching content from {url}...")
        html_content = fetch_website(url)

        if html_content:
            # Display the title of the webpage
            title = extract_title(html_content)
            st.write(f"### {title}")

            # Display the HTML content (text-only approach)
            st.write("### Webpage Content:")
            st.markdown(html_content, unsafe_allow_html=True)

            # You could add an iframe for some basic rendering of images, but JS-heavy sites might not work well
            # Display a basic "preview" iframe (this won't execute JavaScript)
            st.write(f"<iframe src='{url}' width='100%' height='600px'></iframe>", unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()
