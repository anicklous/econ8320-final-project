**ECON8320 FINAL PROJECT**

*Retrieving Data in Google Colab*

My first task in creating a Streamlit Dashboard was retrieving datasets to analyze. In Google Colab, I used a BLS Public Data API Signature (Version 1.0) to collect data for multiple timeseries. Through this process I learned how to create API URL, payload, and response variables to generate a JSON object containing my datasets of interest. Importantly, while I was figuring out how to utilize the API Signature, I accidentally exceeded its daily request limit. To prevent this from happening again, I kept my finalized API request in a separate cell. This allowed me to move on to my next task, data cleaning, without worrying about temporarily losing access to everything again.

*Cleaning Data in Google Colab*

I easily converted the JSON object containing my data to a Python object, but the resulting dictionary was nested in many layers-- unfit for conversion to a usable Pandas DataFrame. Preparing the dictionary for conversion was the most challenging aspect of this task, and it involved many steps. First, I was able to strip some nested layers away by accessing specific keys within the dictionary. Doing this created a new nested dictionary, now with only two layers. From here, I was able to split this dictionary into five smaller dictionaries, each with one nested layer. At this point, I had one nested dictionary for every dataset I initially retrieved. For each of these dictionaries, I accessed the key containing data. Finally no longer nested, these dictionaries were in a proper format to be converted to Pandas DataFrames. From there, I selected which columns (formerly keys) to drop, and downloaded the resulting CSV files.

*Creating a GitHub Action*

This step required me to learn about YML and Cron syntax. Fortunately, my previous forked repositories include multiple workflow actions each, so I could replicate a lot of these steps from those. When I got to installing dependencies, I also learned how the requirements.txt file can be used to contain these elements. This GitHub Action will repeat the retrieving/cleaning/CSV download process at 9:30 AM EST on the third Friday of every month. With fresh data being pushed to this repository monthly, my Streamlit dashboard app should automatically update when the user visits again.

*Creating a Streamlit Dashboard*

Having no prior experience working with Streamlit, I found their documentation and working examples very helpful. These resources taught me how to implement changes to layouts, data elements, input widgets, and more. Before I could get too far designing my dashboard, though, I realized that my data still needed some cleaning. In the VS Code Codespace (where I designed the dashboard UI), I converted column types, removed special characters (-), and ordered my categorical columns to ensure coherent visualizations. While Streamlit offered basic visualization options, they didn't allow for much customization. For the most part, I ended up using Pandas DataFrame and Plotly Express objects as building blocks instead. Further, I wanted to change the color scheme from the default setting, but that would've required using an external TOML file. Once I was satisfied with my dashboard UI, I deployed the app through Streamlit Community Cloud.
