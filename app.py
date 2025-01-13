import streamlit as st
import openai

# Streamlit app setup
st.title("Intelligent Social Media Caption Generator")
st.write("Upload an image to generate social media captions and hashtags using OpenAI's GPT model.")

# Fetch OpenAI API key from secrets
api_key = st.secrets["api_key"]  # Add your OpenAI API key to secrets.toml

# Initialize OpenAI API key
openai.api_key = api_key

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Generate caption using ChatGPT
def generate_caption(image_description):
    """Generate captions using OpenAI's GPT model based on a text description of the image."""
    prompt = f"Generate a creative caption for the following image. The image contains: {image_description}. Caption:"

    # OpenAI GPT request for caption generation using ChatCompletion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or choose a suitable model, like "gpt-4"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

if uploaded_file:
    # Step 1: Allow the user to provide a description (since ChatGPT can't process the image itself)
    image_description = st.text_input("Describe the image", "For example: A cat sitting on a windowsill.")
    
    if image_description:
        # Step 2: Generate a caption using ChatGPT based on the user's description
        caption = generate_caption(image_description)

        # Step 3: Display the generated caption
        st.subheader("Generated Caption")
        st.write(caption)

else:
    st.info("Upload an image and describe it to generate captions.")
