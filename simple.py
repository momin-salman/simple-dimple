import streamlit as st

# Function to simulate AI text generation
# In a real application, you would replace this with an actual LLM API call
def generate_text_with_ai(prompt):
    """
    Simulates an AI generating text based on a given prompt.
    For a real application, integrate with an LLM like Google's Gemini API.
    """
    if not prompt:
        return "Please enter a prompt to generate text."

    # Simple placeholder logic for demonstration
    if "hello" in prompt.lower():
        return "Hello there! How can I assist you today?"
    elif "weather" in prompt.lower():
        return "I'm sorry, I don't have real-time weather information. Is there anything else I can help with?"
    elif "story" in prompt.lower():
        return "Once upon a time, in a land far, far away, there lived a curious little robot who loved to explore. One day, it stumbled upon a hidden garden filled with glowing flowers..."
    else:
        return f"You asked for: '{prompt}'. This is a simulated AI response. For more advanced generation, connect to a powerful language model!"

# --- Streamlit App Layout ---
st.set_page_config(page_title="Simple AI Text Generator", layout="centered")

st.title("🤖 Simple AI Text Generator")
st.markdown("""
Welcome to this basic AI text generation app! 
Type a prompt below, and the AI will generate a response.
""")

st.write("---")

# Text input for the user's prompt
user_prompt = st.text_area(
    "Enter your prompt here:",
    placeholder="e.g., Write a short story about a brave knight...",
    height=150
)

# Button to trigger generation
if st.button("Generate Text"):
    with st.spinner("Generating response..."):
        # Call the AI generation function
        generated_response = generate_text_with_ai(user_prompt)
        st.subheader("Generated Response:")
        st.info(generated_response)
else:
    st.write("Click 'Generate Text' to see the AI's response!")

st.write("---")
st.markdown("This app demonstrates a basic concept. For real AI power, integrate with an actual LLM!")
