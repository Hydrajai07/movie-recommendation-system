import nbformat

# Load the notebook
notebook_path = "Movie_recomadation.ipynb"
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Remove corrupted metadata
if 'widgets' in nb['metadata']:
    print("Removing invalid widgets metadata...")
    del nb['metadata']['widgets']

# Save the cleaned notebook
with open("Movie_recomadation_cleaned.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook cleaned and saved as 'Movie_recomadation_cleaned.ipynb'")
python fix_notebook.py
