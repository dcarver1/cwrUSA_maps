# Distributions and conservation status of crop wild relatives of the United States
Storage and visualization of species level summary documentation from the paper ["Crop wild relatives of the United States require urgent conservation action"](https://www.pnas.org/content/117/52/33351)

## Data Availability
Occurrence data used in the modeling and the individual species summary documents visualized here and can found at [https://doi.org/10.7910/DVN/BV4I06](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/BV4I06 )

## Code Availability

Code and additional information on the modeling methodology can be found [here](https://github.com/dcarver1/CWR-of-the-USA-Gap-Analysis)

## questions

dan carver
carverd@colostate.edu


## Search index update
A system to search through the collection was made possible using the add_html_path.py script.
If new analysis files replace old ones, running this script will update the CSV document powering the website search.
To execute this file it might help to run it from a virtual environment so the dependencies are available.  
Setting-up the virtual environment can be done from the terminal on osx and linux with the following commands:
```python3 -m venv env
source venv/bin/activate
python3 -m pip install -r requirements.txt
# and to run the update script use
python add_html_path.py
```

# Testing the website locally
To test the website locally you'll need to run this from a web server.
Using python makes this easy if you have the virtual environment set-up and running
To run a local server from the terminal on osx and linux use:
```
python -m http.server 8000
```
Then navigate to http://localhost:8000/ from your web browser
