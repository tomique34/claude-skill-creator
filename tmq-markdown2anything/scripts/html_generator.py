"""
HTML Generator for tmq-markdown2anything

Generates standalone, self-contained HTML files with embedded CSS.
Supports all 4 themes with responsive design and Slovak diacritics.
"""

from pathlib import Path
from style_config import get_theme
import markdown


class HTMLGenerator:
    """Generate self-contained HTML documents from markdown"""

    def __init__(self, theme_name: str):
        """
        Initialize HTML generator with a theme.

        Args:
            theme_name: Name of the theme to use (professional, minimalist, technical, basic)
        """
        self.theme = get_theme(theme_name)
        self.template_path = Path(__file__).parent.parent / "templates" / "html" / f"{theme_name.lower()}.html"

    def get_css_for_theme(self) -> str:
        """
        Generate CSS based on theme configuration.

        Returns:
            Complete CSS as a string wrapped in <style> tags
        """
        css = f"""
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: '{self.theme.fonts.body_font}', serif;
                font-size: {self.theme.fonts.body_size}pt;
                color: {self.theme.colors.text};
                line-height: {self.theme.layout.line_spacing};
                max-width: 900px;
                margin: 0 auto;
                padding: 40px 20px;
                background-color: #ffffff;
            }}

            h1 {{
                font-family: '{self.theme.fonts.heading_font}';
                font-size: {self.theme.fonts.h1_size}pt;
                color: {self.theme.colors.heading};
                margin-bottom: 0.5em;
                margin-top: 1.5em;
                font-weight: bold;
            }}

            h1:first-child {{
                margin-top: 0;
            }}

            h2 {{
                font-family: '{self.theme.fonts.heading_font}';
                font-size: {self.theme.fonts.h2_size}pt;
                color: {self.theme.colors.heading};
                margin-bottom: 0.4em;
                margin-top: 1.2em;
                font-weight: bold;
            }}

            h3 {{
                font-family: '{self.theme.fonts.heading_font}';
                font-size: {self.theme.fonts.h3_size}pt;
                color: {self.theme.colors.heading};
                margin-bottom: 0.3em;
                margin-top: 1em;
                font-weight: bold;
            }}

            h4, h5, h6 {{
                font-family: '{self.theme.fonts.heading_font}';
                color: {self.theme.colors.heading};
                margin-bottom: 0.3em;
                margin-top: 0.8em;
                font-weight: bold;
            }}

            p {{
                margin-bottom: 1em;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 1.5em 0;
                border: 1px solid {self.theme.colors.table_header_bg};
            }}

            th {{
                background-color: {self.theme.colors.table_header_bg};
                color: {self.theme.colors.table_header_text};
                padding: 12px;
                text-align: left;
                font-weight: bold;
                border: 1px solid {self.theme.colors.table_header_bg};
            }}

            td {{
                padding: 10px 12px;
                border: 1px solid #ddd;
            }}

            {"tr:nth-child(even) td {" if self.theme.tables.alternating_rows else ""}
                {"background-color: " + self.theme.colors.table_row_alt + ";" if self.theme.tables.alternating_rows else ""}
            {"}}" if self.theme.tables.alternating_rows else ""}

            code {{
                font-family: '{self.theme.fonts.code_font}', monospace;
                background-color: #f5f5f5;
                padding: 2px 6px;
                border-radius: 3px;
                font-size: 0.9em;
            }}

            pre {{
                background-color: #f5f5f5;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
                margin: 1em 0;
                border: 1px solid #ddd;
            }}

            pre code {{
                background-color: transparent;
                padding: 0;
                border-radius: 0;
            }}

            a {{
                color: {self.theme.colors.primary};
                text-decoration: none;
            }}

            a:hover {{
                text-decoration: underline;
            }}

            ul, ol {{
                margin-left: 2em;
                margin-bottom: 1em;
            }}

            li {{
                margin-bottom: 0.5em;
            }}

            blockquote {{
                border-left: 4px solid {self.theme.colors.primary};
                margin: 1em 0;
                padding-left: 1em;
                color: #666;
                font-style: italic;
            }}

            hr {{
                border: none;
                border-top: 1px solid #ddd;
                margin: 2em 0;
            }}

            img {{
                max-width: 100%;
                height: auto;
                display: block;
                margin: 1em 0;
            }}

            /* Responsive design */
            @media (max-width: 768px) {{
                body {{
                    padding: 20px 15px;
                    font-size: {self.theme.fonts.body_size - 1}pt;
                }}

                h1 {{
                    font-size: {self.theme.fonts.h1_size - 4}pt;
                }}

                h2 {{
                    font-size: {self.theme.fonts.h2_size - 2}pt;
                }}

                h3 {{
                    font-size: {self.theme.fonts.h3_size - 1}pt;
                }}

                table {{
                    font-size: 0.9em;
                }}

                th, td {{
                    padding: 8px;
                }}
            }}

            /* Print styles */
            @media print {{
                body {{
                    max-width: 100%;
                    padding: 0;
                    color: #000;
                }}

                a {{
                    color: #000;
                    text-decoration: underline;
                }}

                pre, code {{
                    background-color: #f5f5f5;
                    border: 1px solid #ccc;
                }}
            }}
        </style>
        """
        return css

    def generate_html(self, markdown_content: str, title: str = "Document") -> str:
        """
        Convert markdown to complete HTML document with embedded CSS.

        Args:
            markdown_content: Raw markdown content
            title: Document title for <title> tag

        Returns:
            Complete HTML document as a string
        """
        # Parse markdown to HTML with extensions
        md = markdown.Markdown(extensions=[
            'tables',
            'fenced_code',
            'codehilite',
            'nl2br',
            'sane_lists'
        ])
        html_content = md.convert(markdown_content)

        # Get CSS for the theme
        css = self.get_css_for_theme()

        # Create complete HTML document
        html = f"""<!DOCTYPE html>
<html lang="sk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="generator" content="tmq-markdown2anything">
    <title>{title}</title>
    {css}
</head>
<body>
    {html_content}
</body>
</html>"""

        return html

    def save_html(self, markdown_content: str, output_path: Path, title: str = "Document"):
        """
        Generate and save HTML file.

        Args:
            markdown_content: Raw markdown content
            output_path: Path where to save the HTML file
            title: Document title

        Raises:
            IOError: If file cannot be written
        """
        html = self.generate_html(markdown_content, title)

        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write HTML file with UTF-8 encoding
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"✓ HTML generated: {output_path}")
        print(f"  Theme: {self.theme.name}")
        print(f"  Size: {len(html)} bytes")


def main():
    """Simple test of HTML generator"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 html_generator.py <markdown_file> [theme] [output_file]")
        print("Themes: professional, minimalist, technical, basic")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    theme = sys.argv[2] if len(sys.argv) > 2 else "basic"
    output_file = Path(sys.argv[3]) if len(sys.argv) > 3 else input_file.with_suffix('.html')

    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)

    # Read markdown content
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate HTML
    generator = HTMLGenerator(theme)
    title = input_file.stem.replace('-', ' ').replace('_', ' ').title()
    generator.save_html(content, output_file, title)


if __name__ == "__main__":
    main()
