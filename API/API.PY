import google.generativeai as genai

# Set up API key
genai.configure(api_key="AIzaSyBHCsh0ypLPdXpQRmd9EtpL9C1Z09BxNTI")

def generate_code_explanation(code_snippet):
    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = f"""
Provide a comprehensive and detailed explanation of the following code, formatted as documentation:
- Break the code down line-by-line, explaining the purpose and function of each part.
- Describe how each block or segment of the code contributes to the overall functionality.
- Use simple, clear language and explain any technical terms in a way that's easy to understand.
- If applicable, provide real-world examples or use cases to illustrate how the code works.
- Highlight any potential issues, improvements, or best practices, such as optimization or error handling.
- Structure the explanation in well-organized sections or bullet points for readability.
- Mention any assumptions, limitations, or dependencies that might impact the code's performance.
\n\n{code_snippet}
"""

        response = model.generate_content(prompt)

        # Extract and return content text directly without formatting
        content_text = response.candidates[0].content.parts[0].text.strip()
        print(content_text)  # Directly print the explanation
        return content_text

    except Exception as e:
        print(f"Error: {e}")
        return None
