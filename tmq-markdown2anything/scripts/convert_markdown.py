#!/usr/bin/env python3
"""
Markdown to PDF/DOCX/HTML Converter

Main conversion orchestrator for tmq-markdown2anything skill.
Supports single file and batch conversion with multiple themes.
"""

import argparse
import sys
from pathlib import Path
from style_config import get_theme, list_themes


class MarkdownConverter:
    """Convert markdown files to styled PDF, DOCX, or HTML documents"""

    def __init__(self, theme_name: str, output_format: str):
        """
        Initialize converter with theme and output format.

        Args:
            theme_name: Name of the theme to use
            output_format: Output format ('pdf', 'docx', or 'html')
        """
        self.theme = get_theme(theme_name)
        self.format = output_format.lower()

    def read_markdown_file(self, filepath: Path) -> str:
        """
        Read markdown file with UTF-8 encoding (for Slovak diacritics).

        Args:
            filepath: Path to markdown file

        Returns:
            Markdown content as string

        Raises:
            FileNotFoundError: If file doesn't exist
            IOError: If file cannot be read
        """
        if not filepath.exists():
            raise FileNotFoundError(f"Markdown file not found: {filepath}")

        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def generate_instruction_for_claude(self, content: str, output_path: str) -> str:
        """
        Generate instruction for Claude to use document-skills.

        Args:
            content: Markdown content
            output_path: Output file path

        Returns:
            Formatted instruction string for Claude
        """
        styling = self.theme.get_styling_instructions()

        instruction = f"""Convert this markdown to {self.format.upper()} with the following styling:

THEME: {self.theme.name.title()}

CONTENT:
{content}

STYLING SPECIFICATIONS:
{styling}

REQUIREMENTS:
- UTF-8 encoding for Slovak diacritics (ľščťžýáíéúäôň)
- Liberation fonts (full Slovak character support)
- Apply all theme colors and styling
- Output to: {output_path}

Use document-skills:{self.format} to generate the final document."""

        return instruction

    def convert_single_file(self, input_path: Path, output_path: Path):
        """
        Convert single markdown file.

        Args:
            input_path: Input markdown file path
            output_path: Output file path

        Raises:
            Exception: If conversion fails
        """
        print(f"\n{'='*60}")
        print(f"Converting: {input_path.name}")
        print(f"Format: {self.format.upper()}")
        print(f"Theme: {self.theme.name.title()}")
        print(f"{'='*60}\n")

        # Read markdown content
        content = self.read_markdown_file(input_path)

        if self.format == 'html':
            # Generate HTML directly using html_generator
            from html_generator import HTMLGenerator

            html_gen = HTMLGenerator(self.theme.name)
            title = input_path.stem.replace('-', ' ').replace('_', ' ').title()
            html_gen.save_html(content, output_path, title)

        else:
            # Generate instruction for Claude to use document-skills
            instruction = self.generate_instruction_for_claude(content, str(output_path))

            print("INSTRUCTION FOR CLAUDE:")
            print("="*60)
            print(instruction)
            print("="*60)
            print(f"\n✓ Ready to convert {input_path.name} → {output_path.name}")
            print(f"  Please use document-skills:{self.format} to complete the conversion.\n")

    def convert_batch(self, input_dir: Path, output_dir: Path):
        """
        Batch convert all .md files in directory.

        Args:
            input_dir: Input directory containing .md files
            output_dir: Output directory for converted files

        Raises:
            ValueError: If no .md files found
        """
        md_files = sorted(list(input_dir.glob("*.md")))

        if not md_files:
            raise ValueError(f"No .md files found in {input_dir}")

        print(f"\n{'='*60}")
        print(f"BATCH CONVERSION")
        print(f"Input: {input_dir}")
        print(f"Output: {output_dir}")
        print(f"Format: {self.format.upper()}")
        print(f"Theme: {self.theme.name.title()}")
        print(f"Files: {len(md_files)}")
        print(f"{'='*60}\n")

        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        # Convert each file
        success_count = 0
        error_count = 0

        for md_file in md_files:
            output_name = md_file.stem + f".{self.format}"
            output_path = output_dir / output_name

            try:
                self.convert_single_file(md_file, output_path)
                success_count += 1
            except Exception as e:
                print(f"✗ Error converting {md_file.name}: {e}")
                error_count += 1

        # Summary
        print(f"\n{'='*60}")
        print(f"BATCH CONVERSION COMPLETE")
        print(f"Success: {success_count}/{len(md_files)}")
        if error_count > 0:
            print(f"Errors: {error_count}")
        print(f"{'='*60}\n")


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Convert markdown to styled PDF, DOCX, or HTML with Slovak diacritics support",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert to PDF with professional theme
  python3 convert_markdown.py document.md --format pdf --theme professional

  # Convert to HTML with minimalist theme
  python3 convert_markdown.py notes.md --format html --theme minimalist

  # Batch convert directory to DOCX
  python3 convert_markdown.py docs/ --format docx --theme technical --batch

  # Convert with custom output path
  python3 convert_markdown.py input.md --format html --output result.html

Available themes: professional, minimalist, technical, basic
        """
    )

    parser.add_argument(
        "input",
        help="Input markdown file or directory"
    )

    parser.add_argument(
        "--format", "-f",
        choices=["pdf", "docx", "html"],
        default="pdf",
        help="Output format (default: pdf)"
    )

    parser.add_argument(
        "--theme", "-t",
        choices=list_themes(),
        default="basic",
        help="Theme to apply (default: basic)"
    )

    parser.add_argument(
        "--batch", "-b",
        action="store_true",
        help="Batch process all .md files in directory"
    )

    parser.add_argument(
        "--output", "-o",
        help="Output file or directory (optional)"
    )

    args = parser.parse_args()

    # Validate input
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input '{input_path}' does not exist")
        sys.exit(1)

    # Initialize converter
    try:
        converter = MarkdownConverter(args.theme, args.format)
    except Exception as e:
        print(f"Error initializing converter: {e}")
        sys.exit(1)

    # Determine operation mode
    try:
        if args.batch or input_path.is_dir():
            # Batch mode
            if input_path.is_file():
                print("Error: --batch requires a directory, not a file")
                sys.exit(1)

            output_dir = Path(args.output) if args.output else input_path / "output"
            converter.convert_batch(input_path, output_dir)

        else:
            # Single file mode
            if args.output:
                output_path = Path(args.output)
            else:
                output_path = input_path.parent / f"{input_path.stem}.{args.format}"

            converter.convert_single_file(input_path, output_path)

    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
