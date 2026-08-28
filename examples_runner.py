import json

def load_templates(file_path):
    """Load prompt templates and few-shot examples from a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def format_prompt(template, variables):
    """Format prompt template with dynamic variables."""
    formatted_text = template
    for key, value in variables.items():
        placeholder = "{{" + key + "}}"
        formatted_text = formatted_text.replace(placeholder, str(value))
    return formatted_text

if __name__ == "__main__":
    data = load_templates("templates.json")
    templates = data.get("prompt_templates", [])
    
    print("Loaded " + str(len(templates)) + " advanced prompt templates.\n")
    
    for t in templates:
        template_id = t["id"]
        name = t["name"]
        raw_template = t["template"]
        example_input = t.get("sample_variable", {})
        
        print("Template ID: " + str(template_id) + " - " + name)
        if example_input:
            formatted = format_prompt(raw_template, example_input)
            print("Formatted Output:\n" + formatted)
        else:
            print("Template:\n" + raw_template)
        print("-" * 50)
