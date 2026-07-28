# Gerenciador de Pacotes da Snakened (spm) escrito em Snakened
import os
import http
import zip
import toml  # Assumindo um parser de TOML nativo ou básico

fn install_packages():
    print("Lendo ficheiro snakned.toml...")
    
    # 1. Validar se o arquivo de configuração existe
    if not os.exists("snakned.toml"):
        print("Erro: Ficheiro snakned.toml não encontrado!")
        return
    
    # 2. Ler e parsear o TOML
    var config = toml.parse_file("snakned.toml")
    var dependencies = config["dependencies"]
    
    # 3. Criar a pasta de módulos se não existir
    if not os.exists("snakned_modules"):
        os.mkdir("snakned_modules")
        print("Pasta 'snakned_modules' criada com sucesso.")

    # 4. Loop para baixar cada dependência
    for lib_name in dependencies.keys():
        var repo_info = dependencies[lib_name] # Ex: "lucas/requests-snakned@main"
        
        # Separar o repositório da branch/tag
        var parts = repo_info.split("@")
        var repo = parts[0]   # "lucas/requests-snakned"
        var target = parts[1] # "main"
        
        print("A baixar " + lib_name + " (" + target + ")...")
        
        # Construir a URL de download do GitHub
        var url = "https://github.com/" + repo + "/archive/refs/heads/" + target + ".zip"
        
        # Definir caminhos temporários
        var zip_path = "snakned_modules/" + lib_name + ".zip"
        var dest_folder = "snakned_modules/" + lib_name
        
        # 5. Fazer o download do ZIP
        var success = http.download(url, zip_path)
        
        if success:
            print("Download concluído. A extrair...")
            
            # 6. Extrair o arquivo ZIP
            zip.extract(zip_path, dest_folder)
            
            # 7. Limpar o arquivo ZIP temporário
            os.remove(zip_path)
            
            print("Pacote " + lib_name + " instalado com sucesso!")
        else:
            print("Erro ao baixar o pacote " + lib_name)

# Executar a função principal
install_packages()