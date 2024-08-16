import os
import shutil
import subprocess
import sys
from time import sleep

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

def run_script(script_path, venv_dir=None, overwrite=False):
    """Executa o script Python fornecido com a ativação opcional do ambiente virtual."""
    
    dist_dir = 'dist'
    build_dir = 'build'
    spec_file = None 
    error = False
    
    try:
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Arquivo {script_path} não encontrado.")
        
        script_name = os.path.splitext(os.path.basename(script_path))[0]
        print(f"Nome do script: {script_name}")
        
        venv_activated = False
        if venv_dir and not is_venv():
            print("Ativando o ambiente virtual...")
            activate_venv(venv_dir)
            venv_activated = True
        
        if not is_pyinstaller():
            print("Instalando o PyInstaller...")
            subprocess.run(['pip', 'install', 'pyinstaller'], check=True)

        print("Executando PyInstaller...")
        subprocess.run(['pyinstaller', '--onefile', script_path], check=True)
        
        spec_file = f'{script_name}.spec'
        main_exe = os.path.join(dist_dir, f'{script_name}.exe')

        sleep(5) # Espera 5 segundos para continuar
        
        if not os.path.exists(main_exe):
            raise FileNotFoundError(f"Arquivo {main_exe} não encontrado.")

        if os.path.exists(f'./{script_name}.exe'):
            if overwrite is True:
                print("Removendo o main.exe do diretório padrão...")
                os.remove(f'./{script_name}.exe')
            else:
                raise FileExistsError("Não foi possível deletar o executavel.")
        
        print(f"Copiando {main_exe} para o diretório principal...")
        shutil.copy(main_exe, '.')
            
    except subprocess.CalledProcessError as e:
        error = True
        print(f"Erro ao executar PyInstaller: {e}")
        
    except FileNotFoundError as e:
        error = True
        print(e)
        
    except FileExistsError as e:
        error = True
        print(e)
        
    except Exception as e:
        error = True
        print(f"Ocorreu um erro: {e}")
    
    finally:
        if os.path.exists(build_dir):
            print(f"Removendo pasta {build_dir}...")
            shutil.rmtree(build_dir)

        if os.path.exists(dist_dir):
            print(f"Removendo pasta {dist_dir}...")
            shutil.rmtree(dist_dir)

        if os.path.exists(spec_file):
            print(f"Removendo arquivo {spec_file}...")
            os.remove(spec_file)
        
        if venv_activated:
            subprocess.run('deactivate', shell=True)
            print("Desativando o ambiente virtual.")
            
    if error is False:
        print("Script executado com sucesso!")
        return
        
