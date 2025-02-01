# QR Code Generator

Este projeto é um gerador de QR Code simples usando Python. O QR Code gerado é salvo automaticamente na área de trabalho do usuário.

## 📌 Funcionalidades
- Gera um QR Code a partir de um link.
- Salva automaticamente o QR Code na área de trabalho.
- Funciona em Windows, Linux e macOS.
- Permite personalizar o nome do arquivo gerado.

## 🚀 Tecnologias Utilizadas
- Python 3
- Biblioteca `qrcode`
- Biblioteca `PIL` (Pillow)

## 📦 Instalação
Antes de rodar o projeto, certifique-se de que tem o Python instalado. Em seguida, clone o repositório e instale as dependências necessárias:  

```sh
pip install -r requirements.txt
```  

## ▶️ Como Usar
Execute o script pelo terminal com o seguinte comando:

```sh
python main.py <LINK> [NOME_DO_ARQUIVO.png]
```  


### 🔹 Exemplos de Uso:

```sh
    python main.py https://github.com/PedroMagno11
```  

Ou especificando um nome de arquivo personalizado:

```sh
    python main.py https://github.com/PedroMagno11 qrcode_pedromagno11.png
```  

Ambos criarão um QR Code na sua área de trabalho, redirecionando para ` https://github.com/PedroMagno11`.  


## 📂 Local de Salvamento
O QR Code gerado será salvo na área de trabalho do usuário, independentemente do sistema operacional.

## ⚙️ Compatibilidade
- ✅ Windows
- ✅ Linux
- ✅ macOS

## 📜 Licença
Este projeto está sob a licença MIT. 

---
Desenvolvido por [Pedro Magno](https://github.com/PedroMagno11)

