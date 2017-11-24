#Yolo-Bounding-Box



#H1 Descrição: 

Sofware em python para criacao de Bouding Box para Yolo.
Seleciona um bando de imagens e o usuario seleciona os itens.
Ao salvar cria um arquivo .txt com mesmo nome da imagem com os dados do elemento selecionado.
Por enquanto somente para uma classe.
No arquivo txt: "Classe Centro_x Centro_Y Largura Altura"

#H1 Requisitos:
⋅⋅* Pillow
⋅⋅* Tkinter

#H1 Tutorial: 

1. Rodar no terminal "$python bbYOLO.py"

2. Clicar em "Load" e selecionar as imagens( somente .jpg por enquanto)

3. Primeiro clique demarca o primeiro limite da Bounding box, o segundo fecha o retangulo.

4. Caso tenha dado o primeiro clique e queira cancelar "ESC"

5. Caso queira remover um retangulo ver o ID dele na direita em cima do retangulo e duplo no elemento da lista na direita com mesmo ID.

6. Finalizado clicar em "Save" para gerar o arquivo .txt.

7. "Next" e "Back" vai para a proxima imagem das selecionadas.

8. "Close" para fechar o programa
