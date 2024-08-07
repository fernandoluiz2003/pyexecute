# my_library/cli.py
import argparse
import os
from .pyexecute import run_script

def main():
    parser = argparse.ArgumentParser(description='Gerencie ambientes virtuais e execute scripts Python com PyInstaller.')
    parser.add_argument('script', help='Caminho para o script Python a ser executado.')
    parser.add_argument('--venv', help='Caminho para o ambiente virtual.', required=False)
    
    args = parser.parse_args()

    if not os.path.exists(args.script):
        print(f"Script não encontrado: {args.script}")
        return

    run_script(args.script, args.venv)

if __name__ == '__main__':
    main()
