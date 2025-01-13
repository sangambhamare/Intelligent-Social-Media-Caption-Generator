import streamlit as st
import requests

# Streamlit app setup
st.title("Intelligent Social Media Caption Generator")
st.write("Upload an image to generate social media captions and hashtags using the Intelligent Caption Generator.")

# Fetch API key from secrets
api_key = st.secrets["api_key"]

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        # Prepare the image to be sent as a file (multipart/form-data)
        url = "YOUR_API_URL_HERE"  # Replace with the correct API endpoint URL
        headers = {"Authorization": f"Bearer {api_key}"}
        files = {"image": uploaded_file.getvalue()}
        
        # Adding action parameter if needed
        payload = {"action": "generate_captions"}  # Adjust based on API documentation

        # Make the API request
        with st.spinner("Generating captions..."):
            response = requests.post(url, headers=headers, files=files, data=payload)

        # Parse and display the response
        if response.status_code == 200:
            captions = response.json().get("captions", [])
            if captions:
                st.subheader("Generated Captions")
                for i, caption in enumerate(captions, start=1):
                    st.write(f"{i}. {caption}")
            else:
                st.warning("No captions were generated. Try with another image.")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Upload an image to generate captions.")
