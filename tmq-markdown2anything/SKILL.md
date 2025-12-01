---
name: tmq-markdown2anything
description: Convert markdown files to visually appealing PDF, Word, or HTML documents with Slovak diacritics support, professional themes (professional, minimalist, technical, basic), and advanced table formatting. Use when converting markdown documentation to presentation-ready documents, creating professional web pages from markdown, reports from markdown notes, or batch-converting markdown files to styled PDF/DOCX/HTML formats.
---

# Markdown to PDF/Word/HTML Converter

## Overview

Convert markdown files into professionally styled documents with full Slovak diacritics support. This skill transforms plain markdown into visually appealing PDF, Word (DOCX), or HTML documents using one of four professional themes.

**Key Features:**
- **3 Output Formats**: PDF, DOCX, HTML
- **4 Professional Themes**: Professional, Minimalist, Technical, Basic
- **Slovak Diacritics**: Full UTF-8 support for all Slovak characters
- **Advanced Tables**: Theme-specific styling with colors and borders
- **Batch Processing**: Convert entire directories at once
- **Self-Contained HTML**: No external dependencies, works offline

## Quick Start

### Single File Examples

```bash
# Convert to PDF with professional theme
python3 scripts/convert_markdown.py document.md --format pdf --theme professional

# Convert to HTML with minimalist theme
python3 scripts/convert_markdown.py notes.md --format html --theme minimalist

# Convert to Word with technical theme
python3 scripts/convert_markdown.py api-docs.md --format docx --theme technical
```

### Batch Conversion

```bash
# Convert all markdown files in a directory to HTML
python3 scripts/convert_markdown.py docs/ --format html --theme professional --batch
```

## Installation

```bash
# Install Python dependencies
cd tmq-markdown2anything
pip3 install -r scripts/requirements.txt
```

## Features

### Slovak Diacritics Support

Full support for all Slovak characters with proper UTF-8 encoding:
- **Lowercase**: á ä č ď é í ĺ ľ ň ó ô ŕ š ť ú ý ž
- **Uppercase**: Á Ä Č Ď É Í Ĺ Ľ Ň Ó Ô Ŕ Š Ť Ú Ý Ž
- **Test**: Príliš žltý kôň úpel ďábelské ódy

### Output Formats

**PDF:**
- High-quality print-ready documents
- Embedded fonts for portability
- Professional typography
- Requires: document-skills:pdf

**DOCX:**
- Editable Microsoft Word documents
- Style preservation
- Compatible with Word/LibreOffice
- Requires: document-skills:docx

**HTML:**
- Self-contained single file
- Responsive design (mobile-friendly)
- Embedded CSS (no external files)
- Works offline
- Native Python generation (fast)

### Themes

#### 1. Professional
**Use Case**: Business reports, formal documents, client deliverables

- **Fonts**: Liberation Serif, 11pt body, 24pt/18pt/14pt headings
- **Colors**: Deep blue (#1a237e) headings, formal styling
- **Tables**: Blue header, alternating rows
- **Best For**: Corporate documents, formal presentations

#### 2. Minimalist
**Use Case**: Modern portfolios, clean presentations, design docs

- **Fonts**: Liberation Sans, 10pt body, 22pt/16pt/13pt headings
- **Colors**: Black/gray, minimal accent
- **Tables**: Light gray header, clean design
- **Best For**: Contemporary documents, creative work

#### 3. Technical
**Use Case**: API docs, technical specs, developer guides

- **Fonts**: Liberation Sans/Mono, code-optimized
- **Colors**: Dark slate (#263238), teal accents
- **Tables**: Dark header, code-friendly
- **Best For**: Technical documentation, code samples

#### 4. Basic
**Use Case**: Quick conversions, print-ready, maximum compatibility

- **Fonts**: Liberation Serif, simple sizing
- **Colors**: Pure black on white only
- **Tables**: Black borders, no colors
- **Best For**: Drafts, simple notes, B&W printing

## Detailed Usage

### Command Line Interface

```bash
python3 scripts/convert_markdown.py [OPTIONS] INPUT

Arguments:
  INPUT                 Input markdown file or directory

Options:
  --format, -f          Output format: pdf, docx, html (default: pdf)
  --theme, -t           Theme: professional, minimalist, technical, basic (default: basic)
  --batch, -b           Batch process directory
  --output, -o          Custom output path (optional)
```

### Single File Conversion

Convert one markdown file to the specified format:

```bash
# PDF with professional theme
python3 scripts/convert_markdown.py report.md --format pdf --theme professional

# HTML with technical theme
python3 scripts/convert_markdown.py api.md --format html --theme technical --output api-docs.html

# DOCX with minimalist theme
python3 scripts/convert_markdown.py notes.md --format docx --theme minimalist
```

**Default Behavior**:
- Output file created in same directory as input
- Output name: `<input-name>.<format>`
- Example: `document.md` → `document.pdf`

### Batch Conversion

Convert all `.md` files in a directory:

```bash
# Basic usage - output to 'output/' subdirectory
python3 scripts/convert_markdown.py markdown-files/ --format html --theme professional --batch

# Custom output directory
python3 scripts/convert_markdown.py src/docs/ --format pdf --theme minimalist --batch --output build/pdfs/
```

**Batch Behavior**:
- Processes all `.md` files in directory
- Creates output directory if needed
- Preserves original filenames
- Shows progress for each file
- Summary report at end

### Slovak Content Example

```markdown
# Technická Dokumentácia

## Úvod

Príliš žltý kôň úpel ďábelské ódy.

| Názov | Popis | Hodnota |
|-------|-------|---------|
| Prvý | Slovenský text | 100 |
| Druhý | S diakritikou | 200 |
```

This markdown will correctly render all Slovak diacritics in PDF, DOCX, and HTML output.

## Examples

### Example 1: Business Report (PDF)

```bash
python3 scripts/convert_markdown.py quarterly-report.md --format pdf --theme professional
```

**Output**: Professional PDF with deep blue headings, formal tables, business-ready formatting.

### Example 2: Portfolio Website (HTML)

```bash
python3 scripts/convert_markdown.py portfolio.md --format html --theme minimalist
```

**Output**: Clean, modern HTML page with responsive design, perfect for hosting online.

### Example 3: API Documentation (HTML)

```bash
python3 scripts/convert_markdown.py api-reference.md --format html --theme technical
```

**Output**: Developer-friendly HTML with syntax highlighting, monospace code blocks, dark slate styling.

### Example 4: Meeting Notes (DOCX)

```bash
python3 scripts/convert_markdown.py meeting-notes.md --format docx --theme basic
```

**Output**: Simple, editable Word document with black and white styling.

### Example 5: Batch Documentation

```bash
python3 scripts/convert_markdown.py project-docs/ --format pdf --theme professional --batch
```

**Output**: All markdown files in `project-docs/` converted to professional PDFs in `project-docs/output/`.

## Advanced Usage

### HTML Output Features

HTML output includes:
- **Responsive Design**: Adapts to screen size (max-width: 900px)
- **Mobile Optimized**: Touch-friendly, readable on phones
- **Print-Friendly**: CSS optimized for printing
- **Self-Contained**: All CSS embedded, no external files
- **Offline Ready**: Works without internet connection

### Table Formatting

Tables are automatically styled based on theme:

**Professional Theme**:
- Blue header background (#1a237e)
- White header text
- Alternating row colors (light gray/white)

**Minimalist Theme**:
- Light gray header (#f0f0f0)
- Thin borders
- No row alternation

**Technical Theme**:
- Dark slate header (#263238)
- Code-friendly spacing
- Alternating rows for readability

**Basic Theme**:
- Black borders only
- Bold headers
- No colors

### Code Blocks

Code blocks are preserved with proper formatting:

````markdown
```python
def hello_slovak():
    print("Príliš žltý kôň")
    return True
```
````

- **Technical Theme**: Optimized for code with syntax highlighting
- **All Themes**: Monospace font (Liberation Mono)
- **HTML**: Horizontal scroll for long lines

## Templates Reference

Detailed theme specifications:
- [Professional Theme](templates/PROFESSIONAL_TEMPLATE.md) - Business and formal
- [Minimalist Theme](templates/MINIMALIST_TEMPLATE.md) - Clean and modern
- [Technical Theme](templates/TECHNICAL_TEMPLATE.md) - Developer-focused
- [Basic Theme](templates/BASIC_TEMPLATE.md) - Simple and universal

HTML examples:
- [Professional HTML](templates/html/professional.html)
- [Minimalist HTML](templates/html/minimalist.html)
- [Technical HTML](templates/html/technical.html)
- [Basic HTML](templates/html/basic.html)

## Scripts Reference

- **[convert_markdown.py](scripts/convert_markdown.py)** - Main conversion tool
- **[html_generator.py](scripts/html_generator.py)** - HTML generation engine
- **[style_config.py](scripts/style_config.py)** - Theme definitions

## Troubleshooting

### Issue: Slovak Diacritics Not Rendering

**Solution**:
1. Verify input file is UTF-8 encoded
2. Check Liberation fonts are available
3. Test with: `echo "Príliš žltý kôň" | python3 scripts/convert_markdown.py`

### Issue: Tables Not Formatting Correctly

**Solution**:
1. Verify markdown table syntax (proper pipes `|`)
2. Ensure header separator line: `|---|---|---|`
3. Check theme supports table colors

### Issue: Batch Conversion Fails

**Solution**:
1. Verify directory contains `.md` files
2. Check directory permissions
3. Ensure output directory is writable
4. Try single file first to test setup

### Issue: HTML Not Displaying Properly

**Solution**:
1. Open in modern browser (Chrome, Firefox, Safari)
2. Check file encoding is UTF-8
3. Verify no browser extensions blocking styles

### Issue: PDF/DOCX Not Generating

**Solution**:
- HTML: Generated directly by Python script
- PDF/DOCX: Requires Claude to invoke document-skills
- Script prints instructions for Claude to execute
- Verify document-skills plugin is available

### Issue: Text Overflows Page Boundaries in PDF

**Problem**: Prompts in code blocks or long lines overflow outside defined page margins in PDF output (HTML works correctly).

**Solution**:
The skill now includes automatic text wrapping for PDF output:
- All text respects page margins strictly
- Code blocks and prompts wrap long lines automatically
- Table cells wrap content with word-wrap: break-word
- No horizontal overflow in any text elements
- Long URLs and words break if necessary

**Technical Details**:
The fix is implemented in `scripts/style_config.py` in the `get_styling_instructions()` method:
- `CODE BLOCKS AND PROMPTS` section enables white-space: pre-wrap
- `TEXT FORMATTING` section enables word-wrap: break-word for all elements
- `PAGE LAYOUT` section enforces strict margin respect
- Maximum width set to 100% of content area (respects margins)

This ensures all content, including long prompts and code blocks, stays within the defined page boundaries when document-skills:pdf generates the final PDF.

## Workflow Integration

### For PDF/DOCX

1. User runs conversion script
2. Script reads markdown (UTF-8)
3. Script generates instruction for Claude
4. Claude invokes document-skills:pdf or document-skills:docx
5. Final document created

### For HTML

1. User runs conversion script
2. Script reads markdown (UTF-8)
3. Script generates HTML with embedded CSS
4. HTML file saved directly (no Claude interaction needed)
5. Self-contained HTML ready to use

## Best Practices

### Choosing a Theme

- **Professional**: Client-facing documents, formal reports
- **Minimalist**: Modern, design-focused content
- **Technical**: Code documentation, API references
- **Basic**: Quick drafts, maximum compatibility

### Slovak Content

- Always use UTF-8 encoding for markdown files
- Test with standard phrase: "Príliš žltý kôň úpel ďábelské ódy"
- Liberation fonts support all Slovak characters

### Batch Processing

- Organize markdown files in dedicated directory
- Use consistent naming for output organization
- Choose appropriate theme for document set
- Review one file before batch processing all

### HTML Output

- Use for web publishing or online documentation
- Theme choice affects website aesthetic
- Responsive design works on all devices
- Can be edited with any text editor

## When to Use This Skill

Use **tmq-markdown2anything** when you need to:
- Convert markdown documentation to professional documents
- Create visually appealing PDFs from markdown notes
- Generate Word documents with Slovak text
- Build single-file HTML pages from markdown
- Batch process multiple markdown files
- Ensure proper Slovak diacritics rendering
- Apply consistent styling across documents
- Create print-ready or web-ready output

## Technical Requirements

- Python 3.6+
- markdown library (see requirements.txt)
- UTF-8 file encoding
- For PDF/DOCX: Claude with document-skills plugin
- For HTML: No additional requirements
