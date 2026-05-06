Rafael Alcântara Brescia
202501007431
Ciência de Dados e Inteligência Artificial

1 - Objetivo do trabalho

O objetivo da atividade foi construir a página inicial da Livraria Ibmec usando HTML e CSS puro, sem framework externo. A principal tecnologia usada no layout foi o CSS Grid, seguindo o wireframe proposto no PDF.

A página foi organizada com as seguintes áreas principais:

- topo;
- destaque;
- novidades;
- categorias;
- rodapé.

2 - Estrutura de arquivos

A estrutura criada foi:

Automobilismo/
 index4.html
 estilo2.css
 parte.escrita.md

O arquivo index4.html contém a estrutura da página e o arquivo estilo2.css contém toda a parte visual e responsiva.

3 - Explicação da implementação

Etapa 1 - Layout macro da página

Na primeira etapa, a classe .pagina foi transformada em um container grid com display: grid. Foram criadas duas colunas usando 2fr 1fr, para que a seção de destaque ocupasse aproximadamente 2/3 da largura e a seção de novidades ocupasse aproximadamente 1/3.

Também foram definidas as áreas da página com grid-template-areas, deixando o topo, as categorias e o rodapé ocupando a largura total.

As áreas usadas foram:

grid-template-areas:
 "topo topo"
 "destaque novidades"
 "categorias categorias"
 "rodape rodape";

Depois, cada elemento filho recebeu sua área correta com grid-area.

Etapa 2 - Grade de categorias responsiva

A seção .categorias também foi transformada em grid. Para deixar os cards responsivos sem media query, foi usada a seguinte configuração:

grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));

Essa regra faz com que o navegador crie automaticamente quantas colunas couberem na tela, respeitando o tamanho mínimo de 160px para cada card.

O primeiro card, Programacao, foi configurado para ocupar duas colunas com:

.card-cat:first-child {
 grid-column: span 2;
}

Etapa 3 - Alinhamento e tipografia

O header foi centralizado usando Grid interno, com:

display: grid;
place-items: center;
text-align: center;

O footer foi dividido em três colunas usando:

grid-template-columns: repeat(3, 1fr);

Na seção de destaque, o conteúdo foi alinhado no início verticalmente e centralizado horizontalmente:

align-items: start;
justify-items: center;

O preço recebeu destaque com fonte maior, negrito e a cor amarela #FFCC00.

Etapa 4 - Responsividade com media query

Para telas menores que 600px, o layout foi alterado para uma coluna única. Isso melhora a leitura em celulares, porque destaque e novidades deixam de ficar lado a lado.

Na media query, as áreas foram reorganizadas assim:

grid-template-areas:
 "topo"
 "destaque"
 "novidades"
 "categorias"
 "rodape";

Também foi removido o span de duas colunas do primeiro card no mobile, para evitar quebra ruim no layout.

4 - Respostas das questões da atividade

2.4 - Teste de responsividade

Quantas colunas aparecem com a janela em aproximadamente 800px de largura?

Resposta: aparecem cerca de 4 colunas de categorias, porque há espaço suficiente para vários cards lado a lado.

Quantas colunas aparecem com a janela em aproximadamente 400px de largura?

Resposta: aparecem cerca de 2 colunas, porque o espaço da tela fica menor.

O que acontece quando não há largura suficiente nem para uma coluna de 160px?

Resposta: o card pode ultrapassar o tamanho da tela e gerar rolagem horizontal. Por isso a media query da Etapa 4 reduz o tamanho mínimo dos cards no mobile.

3.4 - Questão reflexiva

Diferença entre justify-items e justify-self:

Resposta: justify-items é aplicado no container grid e define o alinhamento horizontal de todos os itens dentro das células. Já justify-self é usado em um item específico, quando eu quero alinhar apenas aquele item de forma diferente dos outros.

Diferença entre align-items e align-content:

Resposta: align-items alinha os itens dentro das células do grid no eixo vertical. Já align-content alinha o conjunto das linhas do grid dentro do container, quando existe espaço sobrando no container.

4.4 - Questão de consolidação

Por que redefinimos grid-template-areas na media query em vez de apenas grid-template-columns?

Resposta: porque mudar apenas as colunas não garante que a ordem visual fique organizada no celular. Ao redefinir grid-template-areas, as seções ficam em uma ordem melhor para leitura em telas pequenas.

5 - Revisão final

Questão 1

Qual é a função do -1 na notação grid-column: 1 / -1? Por que é mais robusto do que escrever o número exato da última linha?

Resposta: o -1 representa a última linha da grade. Usar grid-column: 1 / -1 faz o item ocupar toda a largura do grid. Isso é mais robusto porque continua funcionando mesmo se o número de colunas mudar depois.

Questão 2

Diferencie auto-fill de auto-fit dentro de repeat(). Em qual situação um se comporta de forma diferente do outro?

Resposta: os dois criam colunas automáticas conforme o espaço disponível. A diferença aparece quando sobra espaço. O auto-fill mantém colunas vazias reservadas, enquanto o auto-fit recolhe essas colunas vazias e permite que os itens existentes ocupem mais espaço.

Questão 3

O que acontece se você criar uma grid-template-areas não retangular, por exemplo, nomear uma área em forma de L?

Resposta: o CSS Grid exige que a área tenha formato retangular. Se ela for criada em formato de L, o navegador não aplica corretamente a área definida.

Questão 4 - Identifique o erro

Código com problema:

.pagina {
 display: grid;
 grid-template-columns: 200px 1fr;
 grid-template-areas:
  "cabecalho cabecalho"
  "nav main"
  "rodape rodape";
}

header { grid-area: header; }
nav { grid-area: nav; }
main { grid-area: main; }
footer { grid-area: footer; }

Qual é o problema?

Resposta: os nomes usados no grid-area não batem com os nomes definidos no grid-template-areas. No template foram usados os nomes cabecalho e rodape, mas depois foram usados header e footer.

Como corrigir o header:

header { grid-area: cabecalho; }

Como corrigir o footer:

footer { grid-area: rodape; }

6 - Conclusão

Com esta atividade, foi possível entender melhor como o CSS Grid ajuda a montar layouts de página de forma organizada. O uso de grid-template-areas deixou a estrutura mais fácil de visualizar, e o uso de repeat(auto-fill, minmax()) ajudou a criar uma grade de cards responsiva. A media query foi importante para adaptar o layout para telas pequenas, melhorando a experiência em celulares.