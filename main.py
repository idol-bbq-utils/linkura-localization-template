import argparse
import sys
from pathlib import Path
from src.generate import analyze

i18n = ["zh-CN", "en"]
OUTPUT_DIR = Path("data")
RAW_DIR = Path("raw")
README_FILE = Path("README.md")


def command_gentodo(args):
    """From raw file to translation todo file"""
    print("TODO")
    print("We recommend to generate raw files in raw directory, this will help you keep track of your translation progress.")
    return 0

def command_translate(args):
    """
    Translation tool, providing basic large model API translation interface

    And user also can translated by handmade
    """
    print("TODO")
    return 0

def command_generate(args):
    """Generate translated files and progress reports"""
    (total, translated) = analyze.analyze_translation_progress(RAW_DIR, OUTPUT_DIR, locale=args.locale)
    analyze.write_translation_progress(README_FILE, total, translated, locale=args.locale)
    return 0

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Linkura Translation Tool Template",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--locale', '-l',
        default='zh-CN',
        choices=i18n,
        help='Translation locale'
    )
    
    subparsers = parser.add_subparsers(
        dest='command',
        metavar='COMMAND'
    )
    # gentodo
    parser_gentodo = subparsers.add_parser(
        'gentodo',
        help='From raw file to translation todo file',
    )
    parser_gentodo.add_argument(
        '--about', '-a',
        help='Example for sub args'
    )
    parser_gentodo.set_defaults(func=command_gentodo)
    
    # translate
    parser_translate = subparsers.add_parser(
        'translate',
        help='Translation tool, providing basic large model API translation interface',
    )
    parser_translate.add_argument(
        '--about', '-a',
        help='Example for sub args'
    )
    parser_translate.set_defaults(func=command_translate)
    
    # generate
    parser_generate = subparsers.add_parser(
        'generate',
        help='Generate translated files and progress reports',
    )
    parser_generate.add_argument(
        '--about', '-a',
        help='Example for sub args'
    )
    parser_generate.set_defaults(func=command_generate)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    try:
        return args.func(args)
    except Exception as e:
        print(f"Error occurred while executing command: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())