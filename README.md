Yolo Bounding Box
=================


Descrição:
==========
Software em python para criação de Bouding Box para Yolo.
Seleciona um bando de imagens e o usuário seleciona os itens.
Ao salvar cria um arquivo .txt com mesmo nome da imagem com os dados do elemento selecionado.
Por enquanto somente para uma classe
No arquivo txt: "Classe Centro_x Centro_Y Largura Altura"

Requisitos:
-----------
* Pillow
* Tkinter

Tutorial: 
--------
1. Rodar no terminal "$python bbYOLO.py"

2. Clicar em "Load" e selecionar as imagens( somente .jpg por enquanto)

3. Primeiro clique demarca o primeiro limite da Bounding box, o segundo fecha o retângulo.

4. Caso tenha dado o primeiro clique e queira cancelar "ESC"

5. Caso queira remover um retângulo ver o ID dele na direita em cima do retângulo e duplo no elemento da lista na direita com mesmo ID.

6. Finalizado clicar em "Save" para gerar o arquivo .txt.

7. "Next" e "Back" vai para a próxima imagem das selecionadas.

8. "Close" para fechar o programa

9. Caso possua monitor maior e queira redimensionar a janela, editar no inicio do bbYOLO.py as variáveis width e height.

10. Cada clique com as setas equivale a um step em pixel, para editar o tamanho do step no inicio do bbYOLO.py editar a variável step.
