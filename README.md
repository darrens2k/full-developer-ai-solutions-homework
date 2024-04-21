# Customer Feedback Web Application

This is a Python Flask web application that accepts customer feedback, utilizes the Azure Text Analytics API to perform sentiment classification on the feedback and OpenAI's Chat Completion API to respond to the customer feedback through GPT-4.

This application can either be deployed locally, or hosted on a cloud service. Please see below for deployment instructions, or skip to the bottom to read more about the application. 

### To Deploy Locally:

* Please ensure that directory structure of this repository is maintained on your local machine after downloading.

* Once within your local python environment, run the following command to install the necessary libraries: `pip install -r requirements.txt`

* This application requires that you have an Azure Text Analytics API key and endpoint, along with an OpenAI API key. These values must be passed through a .env file that must have the following format:   

      TEXT_ANALYTICS_API_KEY="your azure analytics api key"
      TEXT_ANALYTICS_ENDPOINT="your azure text analytics endpoint"
      OPENAI_API_KEY="your openai api key"

* After the above configuration has been completed, run the app.py file locally, the application should be found at: `http://127.0.0.1:5000` or the URL of your local host.

### To Deploy on a Cloud Service

* Azure will be used as an example to explain the general process.
* Ensure that you have created a web-app resource.
* Deploy the code within this repository on to the web app resource (via GitHub, VSCode, Git, Azure CLI, etc.)
* Set your API keys and endpoints as environment variables in the configuration settings of the web-app resource. Please note the variables are named in the following convention:

      TEXT_ANALYTICS_API_KEY = your azure analytics api key
      TEXT_ANALYTICS_ENDPOINT = your azure text analytics endpoint
      OPENAI_API_KEY = your openai api key

### Project Overview

While working on this project I learnt many things, such as how to deploy an application on Azure, utilize OpenAI's API and prompt engineer. I feel that all of these are valuable skills, and are often sought after in the machine learning / artificial intelligence industry. 

I utilzied Flask for this project because it is a framework in Python that I am familiar with, though I am aware that other frameworks do offer more flexibility.

I then proceeded to initialize all of the clients I will be using (OpenAI and Azure for Text Analytics), while doing this I ended up learning about environment variables. I knew that one simply can not push API keys out into the internet, but I did not know how this was done. I then learnt about environment variables and .env files, along with the dotenv library in Python that makes working with .env files seamless. If the app is deployed locally, the dotenv library will locate a .env file and extract the variables, if the app is deployed through a cloud service, there likely will be no .env file. If there is no .env file, the dotenv library will not throw an error, and the script will locate the preset environment variables within the cloud service.

Flask does use decorators, I have worked with them before in Python but I never fully understood exactly what they did. I now understand that they are essentially functions that wrap around other functions. Flask specifically is using decorators to route HTTP requests to their corresponding functions. 

The final piece of this puzzle was understanding how to prompt-engineer through OpenAI's chat completion API. I initially used a system message to explain to the LLM what role it would be playing and what its task was. I then used a series of user and assistant messages to provide some example prompt-response pairs to the LLM. Finally, it ends with a final user prompt that contains the prompt that the LLM must respond to. It is worth noting that the completions API would have actually been better suited to this task as this is not a conversation, it was simply a single response but the completions API is no longer receiving updates (also, you cannot access GPT4 through the completions API).

Overall, I really enjoyed this project. It is seemingly simple but I developed a lot of valuable skills through it. It felt like I was really fine tuning the skills I have developed over the past 6 years of my academic careeer.

