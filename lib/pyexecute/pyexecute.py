import os
import shutil
import subprocess
import sys

def is_venv():
    return (hasattr(sys, 'real_prefix') or 
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def activate_venv(venv_dir):
    activate_script = os.path.join(venv_dir, 'venv', 'Scripts', 'activate.bat')
    if os.path.isfile(activate_script):
        subprocess.run([activate_script], shell=True, check=True)
    else:
        raise FileNotFoundError(f"Arquivo {activate_script} não encontrado.")

def is_pyinstaller():
    try:
        result = subprocess.run(
            [sys.executable, '-m','pip', 'show', 'pyinstaller'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return result.returncode == 0
    
    except Exception as e:
        print(f"Erro ao verificar o pyinstaller: {e}")
        return False 

def main():
    try:
        if len(sys.argv) < 2:
            print("Diretório de trabalho não fornecido.")
            sys.exit(1)

        working_dir = sys.argv[1]
        
        # Verifica se está dentro do venv
        venv_activated = False
        if not is_venv():
            print("Ativando o ambiente virtual...")
            activate_venv(working_dir)
            venv_activated = True
        
        if not is_pyinstaller():
            print("Instalando o pyinstaller...")
            subprocess.run(['pip','install','pyinstaller'], check=True)

        # Executa o comando pyinstaller
        print("Executando pyinstaller...")
        subprocess.run(['pyinstaller', '--onefile', 'main.py'], check=True)

        # Caminhos
        dist_dir = 'dist'
        build_dir = 'build'
        spec_file = 'main.spec'
        main_exe = os.path.join(dist_dir, 'main.exe')

        # Verifica se o executável foi criado
        if not os.path.exists(main_exe):
            raise FileNotFoundError(f"Arquivo {main_exe} não encontrado.")

        if os.path.isfile('./main.exe'):
            print("Removendo o main.exe do diretorio padrão")
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
        print(f"Erro ao executar pyinstaller: {e}")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        if venv_activated:
            subprocess.run('deactivate')
            print("Desativando o ambiente virtual.")
            
if __name__ == "__main__":
    main()
