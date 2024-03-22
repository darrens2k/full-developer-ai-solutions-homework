from flask import Flask, render_template, request
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
from openai import OpenAI
import os

# Format: pep8 via flake8
# Author: Darren Singh

# Initialize Flask app
app = Flask(__name__)

# Load in API keys from .env file (if not deployed on azure)
# Will not throw an error if a .env file is not found
load_dotenv()

# Create OpenAI client
openai_client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

# Gather Azure Text Analytics Credentials
text_analytics_api_key = os.environ.get('TEXT_ANALYTICS_API_KEY')
text_analytics_endpoint = os.environ.get('TEXT_ANALYTICS_ENDPOINT')
# Create Text Analytics client
text_analytics_client = TextAnalyticsClient(
    endpoint=text_analytics_endpoint,
    credential=AzureKeyCredential(text_analytics_api_key))

# Function to render the main html file
# Routing to activate when request is made to root URL


@app.route('/')
def index():
    # * For now do not fill in any of the response fields since we do not have
    # any responses yet
    return render_template('feedback_site.html')

# Function to handle the classification of feedback and generation of responses
# Routing to activate when a POST request is made to the /submit_feedback URL


@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():

    # Get customer feedback from form
    feedback = request.form['feedback']

    # * Perform sentiment analysis using Azure Text Analytics
    # (analyze_sentiment method returns positive, negative or
    # neutral sentiment)
    sentiment_analysis = text_analytics_client.analyze_sentiment(
        documents=[feedback])[0]
    # Extract the sentiment
    sentiment = sentiment_analysis.sentiment

    # * Generating response from GPT-4
    # * Using chat completions API to generate response (completions API is no
    # longer receiving updates)
    response = openai_client.chat.completions.create(
        # accessing gpt4
        model="gpt-4",
        messages=[
            # system messages describe the role of the assistant
            # user messages are requests for the model to respond to
            # assistant messages are previous responses
            {"role": "system", "content": "You are an assistant that responds \
             to customer feedback for a chemical producing company. You are\
              currently responding to " + sentiment + " feedback."},
            {"role": "system", "content": "Keep your responses short, concise\
              and straight forward. Do not prompt customers to provide more\
              feedback about their experience, simply acknowledge them."},
            {"role": "user", "content": "This product sucks."},
            {"role": "user", "content": "We're really sorry to hear that\
              you're not happy with your purchase. We value your feedback\
              and we're committed to improving your experience. We'll do our\
              best to address it promptly"},
            {"role": "user", "content": "This product is ok. Not too good or\
              too bad"},
            {"role": "user", "content": "Thank you for sharing your experience\
              with us. Your feedback is important as we always strive for\
              improvement."},
            {"role": "user", "content": feedback}
        ],
        # limit amount of tokens response can have
        max_tokens=50
    )
    return render_template(
        'feedback_site.html',
        generated_response=response.choices[0].message.content,
        detected_sentiment=sentiment)


# Launch app when this script is run
if __name__ == '__main__':
    app.run(debug=False)
