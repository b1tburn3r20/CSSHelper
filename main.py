import re
from collections import defaultdict

def parse_and_rewrite_css(file_path):
    with open(file_path, 'r') as f:
        css_text = f.read()

    # Remove comments from CSS text
    css_text = re.sub(r"/\*.*?\*/", "", css_text, flags=re.DOTALL)

    # This regular expression will match selectors and corresponding rule sets
    css_rule_pattern = r"([^{]+){([^}]*)}"
    matches = re.findall(css_rule_pattern, css_text, re.MULTILINE)

    # Create a dictionary with default value as a dictionary
    css_rules = defaultdict(dict)

    for match in matches:
        selector, rules_text = map(str.strip, match)
        # Splitting rules_text into individual rules
        rules = rules_text.split(";")
        for rule in rules:
            rule = rule.strip()
            # Split each rule into property and value
            property_value = rule.split(":", 1)
            # Avoid adding empty rules
            if len(property_value) == 2:
                property, value = map(str.strip, property_value)
                css_rules[selector][property] = value

    # Write new CSS
    with open("optimized.css", "w") as f:
        for selector, properties in css_rules.items():
            f.write(selector + " {\n")
            for prop, value in properties.items():
                f.write("    " + prop + ": " + value + ";\n")
            f.write("}\n")

if __name__ == "__main__":
    parse_and_rewrite_css('./input.css')  # replace with your file path
