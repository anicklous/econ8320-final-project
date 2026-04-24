**ECON8320 FINAL PROJECT**

*Retrieving Data in Google Colab*

My first task in creating a Streamlit Dashboard was retrieving datasets to analyze. In Google Colab, I used a BLS Public Data API Signature (Version 1.0) to collect data for multiple timeseries. Through this process I learned how to create API URL, payload, and response variables to generate a JSON object containing my datasets of interest. Importantly, while I was figuring out how to utilize the API Signature, I accidentally exceeded its daily request limit. To prevent this from happening again, I kept my finalized API request in a separate cell. This allowed me to move on to my next task, data cleaning, without worrying about temporarily losing access to everything again.

*Cleaning Data in Google Colab*

I easily converted the JSON object containing my data to a Python object, but the resulting dictionary was nested in many layers-- unfit for conversion to a usable Pandas DataFrame. Preparing the dictionary for conversion was the most challenging aspect of this task, and it involved many steps. First, I was able to strip some nested layers away by accessing specific keys within the dictionary. Doing this created a new nested dictionary, now with only two layers. From here, I was able to split this dictionary into five smaller dictionaries, each with one nested layer. At this point, I had one nested dictionary for every dataset I initially retrieved. For each of these dictionaries, I accessed the key containing data. Finally no longer nested, these dictionaries were in a proper format to be converted to Pandas DataFrames. From there, I selected which columns (formerly keys) to drop, and downloaded the resulting CSV files.

*Creating a Github Action*

Still figuring this out, but the action will eventually repeat the retrieving/cleaning/CSV download process at 9:30 AM EST on the first Friday of every month. The Github Action should download the CSVs to this repository. This ensures the Streamlit Dashboard, which pulls CSV data directly from this repository, is updated monthly.

*Creating a Streamlit Dashboard*
