#!/usr/bin/env python3
"""
Test PDF generation with text wrapping fix
"""
import sys
import markdown
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib import colors
import re

from style_config import get_theme


class MarkdownToPDF:
    def __init__(self, theme_name='professional'):
        self.theme = get_theme(theme_name)
        self.styles = getSampleStyleSheet()
        self._create_custom_styles()

    def _create_custom_styles(self):
        # Body style with word wrapping
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['Normal'],
            fontName='Helvetica',
            fontSize=self.theme.fonts.body_size,
            textColor=colors.HexColor(self.theme.colors.text),
            leading=self.theme.fonts.body_size * self.theme.layout.line_spacing,
            spaceAfter=12,
            wordWrap='CJK'  # Enable word wrapping
        ))

        # Heading styles
        self.styles.add(ParagraphStyle(
            name='CustomH1',
            parent=self.styles['Heading1'],
            fontName='Helvetica-Bold',
            fontSize=self.theme.fonts.h1_size,
            textColor=colors.HexColor(self.theme.colors.heading),
            spaceAfter=12,
            spaceBefore=24
        ))

        self.styles.add(ParagraphStyle(
            name='CustomH2',
            parent=self.styles['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=self.theme.fonts.h2_size,
            textColor=colors.HexColor(self.theme.colors.heading),
            spaceAfter=10,
            spaceBefore=20
        ))

        # Code block style with wrapping - key fix for the overflow issue
        self.styles.add(ParagraphStyle(
            name='CustomCode',
            parent=self.styles['Code'],
            fontName='Courier',
            fontSize=9,
            textColor=colors.black,
            backColor=colors.HexColor('#f5f5f5'),
            borderPadding=10,
            borderWidth=1,
            borderColor=colors.HexColor('#ddd'),
            leftIndent=10,
            rightIndent=10,
            spaceAfter=12,
            wordWrap='CJK',  # Enable word wrapping for code blocks
            splitLongWords=True
        ))

    def wrap_long_lines(self, text, max_width=70):
        """Wrap long lines in code blocks to prevent overflow"""
        lines = text.split('\n')
        wrapped_lines = []

        for line in lines:
            if len(line) <= max_width:
                wrapped_lines.append(line)
            else:
                # Break long lines
                while len(line) > max_width:
                    wrapped_lines.append(line[:max_width])
                    line = line[max_width:]
                if line:
                    wrapped_lines.append(line)

        return '\n'.join(wrapped_lines)

    def convert(self, md_file, output_pdf):
        # Read markdown
        print(f"Reading markdown file: {md_file}")
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Convert to HTML first
        html = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

        # Create PDF with proper margins
        print(f"Creating PDF: {output_pdf}")
        doc = SimpleDocTemplate(
            output_pdf,
            pagesize=A4,
            topMargin=2.5*cm,
            bottomMargin=2.5*cm,
            leftMargin=3*cm,
            rightMargin=3*cm
        )

        story = []

        # Parse HTML and build story
        lines = html.split('\n')
        in_code_block = False
        code_lines = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Handle code blocks - this is where the fix applies
            if '<pre>' in line or '<code>' in line:
                in_code_block = True
                code_lines = []
                line = line.replace('<pre>', '').replace('<code>', '')

            if in_code_block:
                # Remove HTML tags from code
                clean_line = re.sub(r'<[^>]+>', '', line)
                if clean_line and '</pre>' not in clean_line and '</code>' not in clean_line:
                    code_lines.append(clean_line)

                if '</pre>' in line or '</code>' in line:
                    in_code_block = False
                    # Create preformatted text with wrapping applied
                    code_text = '\n'.join(code_lines)
                    # Wrap long lines to prevent overflow
                    wrapped_code = self.wrap_long_lines(code_text, max_width=70)
                    story.append(Preformatted(wrapped_code, self.styles['CustomCode']))
                    story.append(Spacer(1, 12))
                continue

            # Handle headings
            if line.startswith('<h1>'):
                text = re.sub(r'<[^>]+>', '', line)
                story.append(Paragraph(text, self.styles['CustomH1']))
            elif line.startswith('<h2>'):
                text = re.sub(r'<[^>]+>', '', line)
                story.append(Paragraph(text, self.styles['CustomH2']))
            elif line.startswith('<p>'):
                text = re.sub(r'<[^>]+>', '', line)
                if text:
                    story.append(Paragraph(text, self.styles['CustomBody']))
            elif line.startswith('<li>'):
                text = re.sub(r'<[^>]+>', '', line)
                if text:
                    story.append(Paragraph(f"• {text}", self.styles['CustomBody']))

        # Build PDF
        doc.build(story)
        print(f"✓ PDF created successfully: {output_pdf}")
        print(f"✓ Text wrapping applied to code blocks and prompts")
        print(f"✓ All content should stay within page margins")


if __name__ == '__main__':
    converter = MarkdownToPDF('professional')
    converter.convert(
        '/Users/tvince/Library/Mobile Documents/com~apple~CloudDocs/_Zivnost-Wiseworx/Klienti/KSK-Specializovane AI skolenia/priprava_financne_oddelenie/Financie_M365_Workshop_Pracovny_Zosit_v2.md',
        'test-workshop-fixed.pdf'
    )
