import os
import sys
import shutil
import subprocess

from time import sleep

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def is_venv():
    """
    Verifica se o ambiente virtual está ativado.
    """
    return (
        hasattr(sys, 'real_prefix') or
    (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )
    
def activate_venv(venv_dir: str = None):
    """
    Ativa o ambiente virtual localizado em `venv_dir`
    """
    activate_script = os.path.join(
        venv_dir or 'venv', 'Scripts', 'activate.bat'
    )
    
    if os.path.isfile(activate_script):
        result = subprocess.run(
            [activate_script],
            shell          = True,
            capture_output = True
        )
        if result.returncode != 0:
            raise Exception(f'Falha ao ativar o virtualenv: {result.stderr}')
    
    else:
        raise FileNotFoundError(f'Arquivo {activate_script} não encontrado.')

def has_pyinstaller():
    """
    Verifica se o `pyinstaller` está instalado.
    """
    try:
        result = subprocess.run(
            [
                sys.executable,
                '-m', 'pip', 'show', 'pyinstaller'
            ],
            stdout= subprocess.PIPE, stderr = subprocess.PIPE
        )
        return result.returncode == 0
    
    except Exception as e:
        logging.error(f"Erro ao verificar o pyinstaller")
        return False
    

def run_script(script_path: str, executable_name: str = None, venv_dir: str = None, overwrite:bool = False):
    """
    Executa o script python fornecido com a ativação opciona do ambiente virtual.
    """
    
    dist_dir  = 'dist'
    build_dir = 'build'
    
    spec_file          = None
    interrupted_script = True
    
    try:
        if executable_name is None:
            script_name = os.path.splitext(
                os.path.basename(script_path)
            )[0]
            
        else:
            script_name = executable_name
        
        spec_file = f'{script_name}.spec'
        logging.info(f'Nome do script: {script_name}')
        
        venv_activated = False
        if not is_venv():
            logging.info('Ativando o ambiente virtual...')
            sleep(5)
            
            activate_venv(venv_dir)
            venv_activated = True
        
        if not has_pyinstaller():
            logging.info('Instalando pyinstaller...')
            subprocess.run(['pip', 'install', 'pyinstaller'], check=True)
            sleep(5)
        
        logging.info('Executando pyinstaller...')
        subprocess.run(
            ['pyinstaller', '--onefile', script_path], 
            check = True
        )
        
        main_exe = os.path.join(
            dist_dir, f'{script_name}.exe'
        )
        sleep(5)
        
        if not os.path.exists(main_exe):
            raise FileNotFoundError(f'Arquivo {main_exe} não encontrado.')
        
        if os.path.exists(f'./{script_name}.exe'):
            if overwrite is True:
                logging.info('Removendo o main.exe do diretório principal...')
                os.remove(f'./{script_name}.exe')
            else:
                FileExistsError("Não foi possível deletar o executavel.")
                
        logging.info(f'Copiando {main_exe} para o diretorio principal...')
        shutil.copy(main_exe, '.')

    except subprocess.CalledProcessError as e:
        logging.error(e)
    
    except FileNotFoundError as e:
        logging.error(e)
    
    except FileExistsError as e:
        logging.error(e)
        
    except Exception as e:
        logging.error(e)
        
    else:
        interrupted_script = False
        
    finally:
        if os.path.exists(build_dir):
            logging.info(f'Removendo pasta {build_dir}...')
            shutil.rmtree(build_dir)
        
        if os.path.exists(spec_file):
            logging.info(f'Removendo pasta {dist_dir}...')
            shutil.rmtree(dist_dir)
        
        if os.path.exists(spec_file):
            logging.info(f'Removendo arquivo {spec_file}...')
            os.remove(spec_file)
        
        if venv_activated:
            subprocess.run('deactivate', shell = True)
            logging.info('Desativando o virtualenv.')
        
        if interrupted_script is False:
            logging.info('Script executado com sucesso!')
            return