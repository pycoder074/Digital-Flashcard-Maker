import os
import ast

def find_python_files(root_directory):
    """Recursively find all Python files in the given directory."""
    python_files = []
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith('.py'):  # Only Python files
                python_files.append(os.path.join(root, file))
    return python_files

def get_imports_and_functions(file_path):
    """Extract all imports and function definitions from a Python file."""
    imports = set()  # Use a set to avoid duplicate imports
    functions = set()  # Use a set to avoid duplicate function definitions
    with open(file_path, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename=file_path)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for n in node.names:
                    imports.add(n.name)
            elif isinstance(node, ast.ImportFrom):
                imports.add(node.module)
            elif isinstance(node, ast.FunctionDef):  # Detect function definitions
                functions.add(node.name)
    return imports, functions

def build_import_tree(python_files):
    """Build a dependency tree of imports and functions."""
    file_data = {}
    for file_path in python_files:
        imports, functions = get_imports_and_functions(file_path)
        file_data[file_path] = {'imports': imports, 'functions': functions}
    return file_data

def print_import_tree(file_data, level=0, parent=None, visited_files=None, visited_functions=None):
    """Print the import and function dependency tree."""
    if visited_files is None:
        visited_files = set()  # Initialize visited files set
    if visited_functions is None:
        visited_functions = set()  # Initialize visited functions set
    
    for file_path, data in file_data.items():
        if file_path in visited_files:  # Skip files already processed
            continue
        
        # Mark this file as visited
        visited_files.add(file_path)

        # Indentation to show hierarchy
        indent = ' ' * (level * 4)
        file_name = os.path.basename(file_path)
        
        # Print file and its functions
        if parent is None:
            print(f"{indent}[FILE] {file_name}")
        else:
            print(f"{indent}[IMPORT] {file_name} (imported by {parent})")
        
        for function in data['functions']:
            if function not in visited_functions:
                print(f"{indent}    [FUNCTION] {function}")
                visited_functions.add(function)  # Mark function as visited
        
        # Recursively print imports, but avoid cycles and redundant imports
        for imported in data['imports']:
            if imported not in visited_files:  # Prevent redundant imports
                for path, _ in file_data.items():
                    if imported in os.path.basename(path):  # Match import to the file
                        print_import_tree(file_data, level + 1, parent=file_name, visited_files=visited_files, visited_functions=visited_functions)

# Root directory where the Python files are located
root_directory = r"E:\flashcard_app"  # Change this to your root folder
python_files = find_python_files(root_directory)
file_data = build_import_tree(python_files)

# Print the import tree including functions
print_import_tree(file_data)
