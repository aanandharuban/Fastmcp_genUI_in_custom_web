import os
import json
from fastmcp import FastMCP
from fastmcp.apps import AppConfig

# Initialize the Server Framework
mcp = FastMCP("Dynamic Custom HTML Visualizer")

# Define our unique internal custom layout namespace
VIEW_URI = "ui://dashboard-app/view.html"

@mcp.resource(VIEW_URI)
def serve_dashboard_ui() -> str:
    """
    Exposes the raw dashboard.html layout structure as a passive app resource.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_filepath = os.path.join(base_dir, "dashboard.html")
    
    with open(html_filepath, "r", encoding="utf-8") as file:
        return file.read()

# 💡 THE MANDATORY FIX: We explicitly declare the data payload parameters inside the AppConfig mapping
@mcp.tool(app=AppConfig(resource_uri=VIEW_URI))
async def render_dynamic_dashboard(
    title: str,
    x_axis_labels: list[str],
    y_axis_values: list[int],
    metric_label: str = "Value"
) -> dict: # 💡 RETURN A DICTIONARY, NOT A STRING!
    """
    Renders an interactive custom HTML analytical dashboard with flexible filters and dynamic chart types.
    """
    # FastMCP's AppConfig infrastructure handles routing dictionary nodes automatically.
    # Returning a native python dict structure forces Claude to trigger the App iframe container.
    return {
        "title": title,
        "labels": x_axis_labels,
        "values": y_axis_values,
        "metric": metric_label
    }

if __name__ == "__main__":
    mcp.run()