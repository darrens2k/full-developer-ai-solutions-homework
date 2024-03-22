# Customer Feedback Web Application

This is a web application that accepts customer feedback, utilizes the Azure Text Analytics API to perform sentiment classification on the feedback and OpenAI's Chat Completion API to respond to the customer feedback through GPT-4.

This application can either be deployed locally, or hosted on a cloud service.

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


