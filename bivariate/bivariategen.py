import json
import numpy as np
import seaborn as sns

def generate_bivariate_style(layer_name, attr_x, attr_y, num_classes=3, color_palette="RdYlBu"):
    """
    Generate a bivariate style for a vector tile layer.
    
    Parameters:
    - layer_name (str): Name of the vector layer.
    - attr_x (str): First attribute for classification.
    - attr_y (str): Second attribute for classification.
    - num_classes (int): Number of categories per attribute (default: 3).
    - color_palette (str): Seaborn colormap for bivariate colors.
    
    Returns:
    - dict: JSON style for Mapbox GL / MapLibre
    """
    
    # Generate a bivariate color matrix
    cmap = sns.color_palette(color_palette, num_classes**2).as_hex()
    
    # Create a classification matrix
    categories = {}
    for i in range(num_classes):
        for j in range(num_classes):
            key = f"{i}{j}"
            categories[key] = cmap[i * num_classes + j]

    # Create Mapbox GL style expression
    style_expression = [
        "match",
        ["concat", ["to-string", ["get", attr_x]], ["to-string", ["get", attr_y]]]
    ]

    # Add classification colors
    for key, color in categories.items():
        style_expression.extend([key, color])

    # Default color if no match
    style_expression.append("#cccccc")

    # Generate the final Mapbox GL JSON style
    style_json = {
        "id": f"bivariate_{layer_name}",
        "type": "fill",
        "source": "my_source",
        "source-layer": layer_name,
        "paint": {
            "fill-color": style_expression,
            "fill-opacity": 0.8
        }
    }
    
    return json.dumps(style_json, indent=2)


# Example usage:
layer_name = "my_layer"
attr_x = "population_class"
attr_y = "income_class"

style_json = generate_bivariate_style(layer_name, attr_x, attr_y)
print(style_json)
