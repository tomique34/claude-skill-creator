"""
Theme Configuration for tmq-markdown2anything

Defines all theme configurations for PDF, DOCX, and HTML output formats.
Each theme includes fonts, colors, layout, and table styling specifications.
"""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class FontConfig:
    """Font configuration for a theme"""
    body_font: str
    body_size: int
    heading_font: str
    h1_size: int
    h2_size: int
    h3_size: int
    code_font: str = "Liberation Mono"


@dataclass
class ColorConfig:
    """Color configuration for a theme"""
    primary: str
    text: str
    heading: str
    table_header_bg: str
    table_header_text: str
    table_row_alt: str


@dataclass
class LayoutConfig:
    """Layout configuration for a theme"""
    margin_top: str
    margin_bottom: str
    margin_left: str
    margin_right: str
    line_spacing: float


@dataclass
class TableConfig:
    """Table styling configuration for a theme"""
    header_style: Dict = field(default_factory=dict)
    border_style: str = "solid"
    alternating_rows: bool = True


@dataclass
class ThemeConfig:
    """Complete theme configuration"""
    name: str
    fonts: FontConfig
    colors: ColorConfig
    layout: LayoutConfig
    tables: TableConfig

    def get_styling_instructions(self) -> str:
        """Generate formatted styling instructions for document-skills"""
        instructions = f"""
FONTS:
- Body: {self.fonts.body_font}, {self.fonts.body_size}pt
- Headings: {self.fonts.heading_font}
  - H1: {self.fonts.h1_size}pt Bold
  - H2: {self.fonts.h2_size}pt Bold
  - H3: {self.fonts.h3_size}pt Bold
- Code: {self.fonts.code_font}

COLORS:
- Primary: {self.colors.primary}
- Text: {self.colors.text}
- Headings: {self.colors.heading}

TABLES:
- Header Background: {self.colors.table_header_bg}
- Header Text: {self.colors.table_header_text}
- Alternating Rows: {self.colors.table_row_alt if self.tables.alternating_rows else 'None'}
- Border Style: {self.tables.border_style}
- Cell Text Wrapping: Enabled (word-wrap: break-word)

PAGE LAYOUT:
- Margins: T:{self.layout.margin_top} B:{self.layout.margin_bottom} L:{self.layout.margin_left} R:{self.layout.margin_right}
- Line Spacing: {self.layout.line_spacing}
- Page Width: Respect margins strictly
- Overflow Handling: Wrap all text, no horizontal overflow

CODE BLOCKS AND PROMPTS:
- Word Wrapping: Enabled (white-space: pre-wrap)
- Overflow: break-word (overflow-wrap: break-word)
- Max Width: 100% of content area (respect margins)
- Long Lines: Wrap to next line, don't overflow page
- Background: #f5f5f5
- Padding: 10px (internal spacing)
- Border: 1px solid #ddd

TEXT FORMATTING:
- All Text Elements: word-wrap: break-word
- Long Words: overflow-wrap: break-word (break if necessary)
- URLs: break-word (don't overflow)
- Paragraphs: Keep within margins, wrap naturally
"""
        return instructions.strip()


# Define all 4 themes

PROFESSIONAL_THEME = ThemeConfig(
    name="professional",
    fonts=FontConfig(
        body_font="Liberation Serif",
        body_size=11,
        heading_font="Liberation Serif",
        h1_size=24,
        h2_size=18,
        h3_size=14,
        code_font="Liberation Mono"
    ),
    colors=ColorConfig(
        primary="#1a237e",
        text="#212121",
        heading="#1a237e",
        table_header_bg="#1a237e",
        table_header_text="#ffffff",
        table_row_alt="#f5f5f5"
    ),
    layout=LayoutConfig(
        margin_top="2.5cm",
        margin_bottom="2.5cm",
        margin_left="3cm",
        margin_right="3cm",
        line_spacing=1.15
    ),
    tables=TableConfig(
        header_style={"bold": True, "background": "#1a237e"},
        border_style="solid",
        alternating_rows=True
    )
)

MINIMALIST_THEME = ThemeConfig(
    name="minimalist",
    fonts=FontConfig(
        body_font="Liberation Sans",
        body_size=10,
        heading_font="Liberation Sans",
        h1_size=22,
        h2_size=16,
        h3_size=13,
        code_font="Liberation Mono"
    ),
    colors=ColorConfig(
        primary="#333333",
        text="#333333",
        heading="#000000",
        table_header_bg="#f0f0f0",
        table_header_text="#000000",
        table_row_alt="#ffffff"
    ),
    layout=LayoutConfig(
        margin_top="3cm",
        margin_bottom="3cm",
        margin_left="2.5cm",
        margin_right="2.5cm",
        line_spacing=1.5
    ),
    tables=TableConfig(
        header_style={"bold": True, "background": "#f0f0f0"},
        border_style="thin",
        alternating_rows=False
    )
)

TECHNICAL_THEME = ThemeConfig(
    name="technical",
    fonts=FontConfig(
        body_font="Liberation Sans",
        body_size=10,
        heading_font="Liberation Sans",
        h1_size=20,
        h2_size=16,
        h3_size=13,
        code_font="Liberation Mono"
    ),
    colors=ColorConfig(
        primary="#00897b",
        text="#212121",
        heading="#263238",
        table_header_bg="#263238",
        table_header_text="#ffffff",
        table_row_alt="#f5f5f5"
    ),
    layout=LayoutConfig(
        margin_top="2cm",
        margin_bottom="2cm",
        margin_left="2cm",
        margin_right="2cm",
        line_spacing=1.3
    ),
    tables=TableConfig(
        header_style={"bold": True, "background": "#263238"},
        border_style="solid",
        alternating_rows=True
    )
)

BASIC_THEME = ThemeConfig(
    name="basic",
    fonts=FontConfig(
        body_font="Liberation Serif",
        body_size=11,
        heading_font="Liberation Serif",
        h1_size=18,
        h2_size=14,
        h3_size=12,
        code_font="Liberation Mono"
    ),
    colors=ColorConfig(
        primary="#000000",
        text="#000000",
        heading="#000000",
        table_header_bg="#ffffff",
        table_header_text="#000000",
        table_row_alt="#ffffff"
    ),
    layout=LayoutConfig(
        margin_top="2.5cm",
        margin_bottom="2.5cm",
        margin_left="2.5cm",
        margin_right="2.5cm",
        line_spacing=1.0
    ),
    tables=TableConfig(
        header_style={"bold": True, "background": "#ffffff"},
        border_style="solid",
        alternating_rows=False
    )
)

# Theme registry
THEMES = {
    "professional": PROFESSIONAL_THEME,
    "minimalist": MINIMALIST_THEME,
    "technical": TECHNICAL_THEME,
    "basic": BASIC_THEME
}


def get_theme(name: str) -> ThemeConfig:
    """
    Get theme configuration by name.

    Args:
        name: Theme name (case-insensitive)

    Returns:
        ThemeConfig object for the requested theme,
        defaults to BASIC_THEME if not found
    """
    return THEMES.get(name.lower(), BASIC_THEME)


def list_themes() -> list:
    """Return list of available theme names"""
    return list(THEMES.keys())
