from django.shortcuts import render
from django.http import HttpResponse
from API.API import generate_code_explanation
import markdown  # Import the markdown library

def main(request):
    explanation = None  # Initialize the explanation variable
    context= None

    if request.method == 'POST':
        code = request.POST.get('code')
        print(code)  # Get the input code from the form
        if code:
            explanation = generate_code_explanation(code)  # Generate the explanation

            # Convert the explanation from Markdown to HTML
            explanation_html = markdown.markdown(explanation)

            context = f"You submitted the code: {explanation_html}"  # Embed the HTML in the context
        else:
            context = "No code submitted."  # Handle the case where no code is provided
    else:
        context = "Please submit your code using the form."

    return render(request, 'index.html', {'context': context})
