# Machine Learning Glossary

A collection of useful definitions of commonly used machine learning terms.
The definitions are in yaml format and are found in the `definitions.yml` file.

The definitions follow the schema:
```yml
concept name:
  definition: "..."
  synonyms: ["...", "..."] # (optional)
  source: # (optional)
    name: "..."
    url: "..."
```

## Usage
```
pip install requirements.txt
python build.py
```
Will generate a HTML page of the definitions using the default template. 

## Contribute
1. Fork the repository
2. Make changes
3. Send Pull Request