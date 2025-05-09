import os
import json

def parse_directory_to_json(directory, output_file="tree.json"):
    """
    Parse the directory structure and save it as a JSON file.

    Args:
        directory (str): Path of the directory to parse.
        output_file (str): Name of the JSON file to generate.
    """
    def traverse_dir(dir_path):
        """
        Traverse the directory and build a nested structure.
        """
        tree = {"name": os.path.basename(dir_path), "children": []}
        with os.scandir(dir_path) as entries:
            for entry in entries:
                if entry.is_dir():
                    tree["children"].append(traverse_dir(entry.path))
                else:
                    tree["children"].append({"name": entry.name})
        return tree

    # Traverse the directory and build the structure
    directory_tree = traverse_dir(directory)

    # Write to a JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(directory_tree, f, indent=4)

    print(f"JSON file '{output_file}' has been generated!")

# Example usage
if __name__ == "__main__":
    # Replace '.' with the path to the directory you want to parse
    parse_directory_to_json(".")
