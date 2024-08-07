import os
import shutil
import subprocess
import sys

def is_venv():
    """Verifica se o ambiente virtual está ativado."""
    return (hasattr(sys, 'real_prefix') or 
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def activate_venv(venv_dir):
    """Ativa o ambiente virtual localizado em `venv_dir`."""
    activate_script = os.path.join(venv_dir, 'venv', 'Scripts', 'activate.bat')
    if os.path.isfile(activate_script):
        subprocess.run([activate_script], shell=True, check=True)
    else:
        raise FileNotFoundError(f"Arquivo {activate_script} não encontrado.")

def is_pyinstaller():
    """Verifica se o PyInstaller está instalado."""
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'show', 'pyinstaller'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return result.returncode == 0
    
    except Exception as e:
        print(f"Erro ao verificar o PyInstaller: {e}")
        return False

def run_script(script_path, venv_dir=None):
    """Executa o script Python fornecido com a ativação opcional do ambiente virtual."""
    try:
        # Verifica se está dentro do venv
        venv_activated = False
        if venv_dir and not is_venv():
            print("Ativando o ambiente virtual...")
            activate_venv(venv_dir)
            venv_activated = True
        
        if not is_pyinstaller():
            print("Instalando o PyInstaller...")
            subprocess.run(['pip', 'install', 'pyinstaller'], check=True)

        # Executa o comando PyInstaller
        print("Executando PyInstaller...")
        subprocess.run(['pyinstaller', '--onefile', script_path], check=True)

        # Caminhos
        dist_dir = 'dist'
        build_dir = 'build'
        spec_file = 'main.spec'
        main_exe = os.path.join(dist_dir, 'main.exe')

        # Verifica se o executável foi criado
        if not os.path.exists(main_exe):
            raise FileNotFoundError(f"Arquivo {main_exe} não encontrado.")

        if os.path.isfile('./main.exe'):
            print("Removendo o main.exe do diretório padrão...")
            os.remove('./main.exe')
        
        # Copia o executável para o diretório principal
        print(f"Copiando {main_exe} para o diretório principal...")
        shutil.copy(main_exe, '.')

        # Remove a pasta build
        if os.path.exists(build_dir):
            print(f"Removendo pasta {build_dir}...")
            shutil.rmtree(build_dir)

        # Remove a pasta dist
        if os.path.exists(dist_dir):
            print(f"Removendo pasta {dist_dir}...")
            shutil.rmtree(dist_dir)

        # Remove o arquivo main.spec
        if os.path.exists(spec_file):
            print(f"Removendo arquivo {spec_file}...")
            os.remove(spec_file)

        print("Script executado com sucesso!")

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar PyInstaller: {e}")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        if venv_activated:
            subprocess.run('deactivate', shell=True)
            print("Desativando o ambiente virtual.")
