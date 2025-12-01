# tmq-markdown2anything

Convert markdown files to visually appealing PDF, Word (DOCX), or HTML documents with full Slovak diacritics support and professional themes.

## Features

- **3 Output Formats**: PDF, DOCX, HTML
- **4 Professional Themes**: Professional, Minimalist, Technical, Basic
- **Slovak Diacritics**: Full UTF-8 support (ľščťžýáíéúäôň)
- **Advanced Tables**: Theme-specific styling with colors and borders
- **Batch Processing**: Convert entire directories at once
- **Self-Contained HTML**: No external dependencies, works offline

## Quick Start

### Installation

```bash
# Install dependencies
pip3 install -r scripts/requirements.txt
```

### Basic Usage

```bash
# Convert to PDF with professional theme
python3 scripts/convert_markdown.py document.md --format pdf --theme professional

# Convert to HTML with minimalist theme
python3 scripts/convert_markdown.py notes.md --format html --theme minimalist

# Batch convert directory
python3 scripts/convert_markdown.py docs/ --format pdf --theme technical --batch
```

## Themes

### Professional
Business reports, formal documents, client deliverables
- Deep blue headings (#1a237e)
- Liberation Serif fonts
- Styled tables with alternating rows

### Minimalist
Modern portfolios, clean presentations
- Black/gray color scheme
- Liberation Sans fonts
- Clean, whitespace-focused design

### Technical
API docs, technical specs, developer guides
- Dark slate headers (#263238)
- Monospace code blocks
- Developer-friendly styling

### Basic
Quick conversions, print-ready documents
- Pure black on white
- Liberation Serif fonts
- No colors, maximum compatibility

## Slovak Diacritics

Full support for all Slovak characters:
- **Test phrase**: Príliš žltý kôň úpel ďábelské ódy
- **All characters**: á ä č ď é í ĺ ľ ň ó ô ŕ š ť ú ý ž
- **Uppercase**: Á Ä Č Ď É Í Ĺ Ľ Ň Ó Ô Ŕ Š Ť Ú Ý Ž

## Command Line Options

```
Usage: python3 scripts/convert_markdown.py [OPTIONS] INPUT

Arguments:
  INPUT                 Input markdown file or directory

Options:
  --format, -f          Output format: pdf, docx, html (default: pdf)
  --theme, -t           Theme: professional, minimalist, technical, basic (default: basic)
  --batch, -b           Batch process directory
  --output, -o          Custom output path (optional)
```

## Examples

### Single File Conversion

```bash
# PDF with professional theme
python3 scripts/convert_markdown.py report.md --format pdf --theme professional

# HTML with technical theme
python3 scripts/convert_markdown.py api.md --format html --theme technical

# DOCX with custom output
python3 scripts/convert_markdown.py notes.md --format docx --output final-report.docx
```

### Batch Processing

```bash
# Convert all .md files to HTML
python3 scripts/convert_markdown.py docs/ --format html --theme minimalist --batch

# Convert to PDF with custom output directory
python3 scripts/convert_markdown.py markdown/ --format pdf --theme professional --batch --output output/pdfs/
```

## Output Formats

### PDF
- High-quality print-ready documents
- Embedded fonts for portability
- Requires: document-skills:pdf (Claude integration)

### DOCX
- Editable Microsoft Word documents
- Style preservation
- Requires: document-skills:docx (Claude integration)

### HTML
- Self-contained single file
- Responsive design (mobile-friendly)
- Embedded CSS (no external files)
- Native Python generation (no Claude needed)

## Project Structure

```
tmq-markdown2anything/
├── SKILL.md                          # Main skill instructions
├── README.md                         # This file
├── templates/
│   ├── PROFESSIONAL_TEMPLATE.md      # Professional theme docs
│   ├── MINIMALIST_TEMPLATE.md        # Minimalist theme docs
│   ├── TECHNICAL_TEMPLATE.md         # Technical theme docs
│   ├── BASIC_TEMPLATE.md             # Basic theme docs
│   └── html/
│       ├── professional.html         # Professional HTML example
│       ├── minimalist.html           # Minimalist HTML example
│       ├── technical.html            # Technical HTML example
│       └── basic.html                # Basic HTML example
└── scripts/
    ├── convert_markdown.py           # Main conversion tool
    ├── html_generator.py             # HTML generation engine
    ├── style_config.py               # Theme definitions
    └── requirements.txt              # Python dependencies
```

## Testing

Test files are included for validation:

```bash
# Test Slovak diacritics with all themes
python3 scripts/convert_markdown.py test-slovak.md --format html --theme professional
python3 scripts/convert_markdown.py test-slovak.md --format html --theme minimalist
python3 scripts/convert_markdown.py test-slovak.md --format html --theme technical
python3 scripts/convert_markdown.py test-slovak.md --format html --theme basic
```

## Troubleshooting

### Slovak Characters Not Rendering
- Verify input file is UTF-8 encoded
- Check Liberation fonts are available
- Test with: `Príliš žltý kôň úpel ďábelské ódy`

### Module Not Found Error
```bash
pip3 install -r scripts/requirements.txt
```

### PDF/DOCX Not Generating
- HTML generates directly via Python
- PDF/DOCX requires Claude with document-skills plugin
- Script prints instructions for Claude to execute

## Claude Skill

This is a Claude Agent Skill. When used within Claude Code or Claude Agent SDK:

1. User requests markdown conversion
2. Skill is automatically invoked
3. For HTML: Generated immediately
4. For PDF/DOCX: Claude uses document-skills to create final output

## Requirements

- Python 3.6+
- markdown library (see requirements.txt)
- UTF-8 file encoding
- For PDF/DOCX: Claude with document-skills plugin

## License

MIT License - See LICENSE file in repository root

## Author

Created as part of the Claude Agent Skills Creator toolkit.

## Version

1.0.0 - Initial release with PDF, DOCX, and HTML support
