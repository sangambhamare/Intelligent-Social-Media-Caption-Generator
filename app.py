import streamlit as st
import requests
import base64

# Streamlit app setup
st.title("Intelligent Social Media Caption Generator")
st.write("Upload an image to generate social media captions and hashtags using the Intelligent Caption Generator.")

# Fetch API key from secrets
api_key = st.secrets["api_key"]

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        # Encode the image to base64
        image_data = uploaded_file.read()
        encoded_image = base64.b64encode(image_data).decode("utf-8")

        # Send the image to the API
        url = "https://chatgpt.com/g/g-6784114c670081919aa773a672118e24-intelligent-caption-generator"  # Replace with your API URL
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {"image": encoded_image}

        # Make the API request
        with st.spinner("Generating captions..."):
            response = requests.post(url, headers=headers, json=payload)

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
