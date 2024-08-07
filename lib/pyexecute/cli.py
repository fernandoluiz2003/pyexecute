# my_library/cli.py
import argparse
import os
from pyexecute import run_script
import sys

def main():
    """parser = argparse.ArgumentParser(description='Gerencie ambientes virtuais e execute scripts Python com PyInstaller.')
    parser.add_argument('script', help='Caminho para o script Python a ser executado.')
    parser.add_argument('--venv', help='Caminho para o ambiente virtual.', required=False)
    
    args = parser.parse_args()

    if not os.path.exists(args.script):
        print(f"Script não encontrado: {args.script}")
        return

    # Passa o caminho do script e o caminho do ambiente virtual (se fornecido) para run_script
    run_script(args.script, args.venv)"""
    
    if len(sys.argv) < 2:
        print("Uso: pyexecute <script_path>")
        sys.exit(1)
    
    script_path = sys.argv[1]
    run_script(script_path)

if __name__ == '__main__':
    main()
