import json
from genson import SchemaBuilder

def generate_json_schema_from_file(filename):
    try:
        # Open and load the JSON data from the specified file
        pathTofile = './responses/'
        with open(pathTofile+filename, 'r') as file:
            json_data = json.load(file)

        # Create a SchemaBuilder instance
        builder = SchemaBuilder()
        builder.add_object(json_data)
        return builder.to_schema()

    except FileNotFoundError:
        return "Error: The file was not found."
    except json.JSONDecodeError:
        return "Error: The file is not a valid JSON file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Prompt the user for the filename
filename = input("Please enter the filename of your JSON file: ")

# Generate the JSON Schema
schema = generate_json_schema_from_file(filename)

# Check if the output is a dictionary (which means it's a schema)
if isinstance(schema, dict):
    # Prompt for a filename to save the schema
    output_filename = './schema/' + filename[:-5] + 'Schema.txt'

    # Write the schema to the specified file
    try:
        with open(output_filename, 'w') as schema_file:
            json.dump(schema, schema_file, indent=2)
        print(f"Schema successfully written to {output_filename}.")
    except Exception as e:
        print(f"Failed to write schema to file: {e}")
else:
    print(schema)
