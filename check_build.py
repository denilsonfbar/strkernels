import os
import tarfile
import importlib.util

import sys
print(f"--- Validando para Python {sys.version} ---")

def check_compilation():
    print("--- 1. Verificando Compilação ---")
    spec = importlib.util.find_spec("strkernels.libcore")
    if spec is None:
        print("❌ Erro: O binário libcore não foi encontrado. Rode 'pip install -e .' primeiro.")
        return False
    print("✅ Binário libcore compilado e localizado.")
    return True

def check_symbols():
    print("\n--- 2. Verificando Símbolos (Kernels) ---")
    # Tenta importar os novos kernels para garantir que a linkagem funcionou
    try:
        from strkernels import WeightedDegreeStringKernel, SpectrumStringKernel
        print("✅ Sucesso: WeightedDegree e Spectrum importados corretamente.")
    except ImportError as e:
        print(f"❌ Erro de Importação: {e}")
        return False
    except OSError as e:
        print(f"❌ Erro de Símbolo (OSError): {e}")
        print("   Dica: Verifique se os novos arquivos .c estão no setup.py.")
        return False
    return True

def check_sdist_contents():
    print("\n--- 3. Verificando Conteúdo do Pacote (MANIFEST.in) ---")
    if not os.path.exists("dist"):
        print("⚠️ Pasta 'dist' não encontrada. Rodando 'python -m build'...")
        os.system("python -m build --sdist")
    
    sdist_files = [f for f in os.listdir("dist") if f.endswith(".tar.gz")]
    if not sdist_files:
        print("❌ Erro: Nenhum arquivo .tar.gz encontrado em dist/.")
        return False
    
    latest_sdist = sorted(sdist_files)[-1]
    with tarfile.open(f"dist/{latest_sdist}", "r:gz") as tar:
        members = tar.getnames()
        # Arquivos que DEVEM estar no pacote para o usuário conseguir compilar
        required = [
            'weighted_degree_sk.c', 
            'spectrum_sk.c',
            'weighted_degree_sk.h',
            'spectrum_sk.h'
        ]
        
        missing = []
        for req in required:
            if not any(req in m for m in members):
                missing.append(req)
        
        if missing:
            print(f"❌ Erro: Arquivos faltando no sdist: {missing}")
            print("   Dica: Verifique seu MANIFEST.in.")
            return False
        else:
            print(f"✅ Todos os arquivos fonte (.c e .h) estão presentes no sdist.")
    return True

if __name__ == "__main__":
    if check_compilation() and check_symbols() and check_sdist_contents():
        print("\n🚀 TUDO PRONTO! O pacote parece íntegro para o upload.")
    else:
        print("\n| Corrija os erros acima antes de subir a versão 0.2.2. |")