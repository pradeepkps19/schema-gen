# API Schema Generator
This is to generate the schema for APIs from the API response JSONs.

The Python library - genson SchemaBuilder is used. 


### Steps to generate
1. Clone this repository to your Python3 installed machine.
2. Install **genson** like: ```pip install genson``` from your terminal.
3. Save your API responses as individual JSON files in the `responses` directory.
4. Run the **schemagen.py** like: ```python3 schemagen.py``` from your terminal.
5. Input the response JSON file name like: ```example-response.json``` as provided as an example.
6. If the JSON is valid, schema will be generated and saved as a new text file named **{{INPUT_JSON_FILE_NAME}}-schema.txt** under the **schema** folder.
