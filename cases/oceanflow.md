# OceanFlow · da experiência no tatame a um produto para academias

[← Voltar ao perfil](../README.md) · [Site da academia](https://oceanflow.fitness/) · [OceanFlow Platform](https://oceanflow.platform)

![Frame de abertura do vídeo OceanFlow: do primeiro oi à matrícula](../assets/oceanflow-video-still.jpg)

*Frame do vídeo de apresentação produzido por mim em 2026. O arquivo completo será vinculado quando estiver publicado em um canal aberto.*

## Contexto e minha atuação

Sou faixa preta de jiu-jítsu, professor e gestor da Ocean Flow Studio Fitness, em Maresias. Ao longo de **sete meses em 2026**, desenvolvi a OceanFlow Platform a partir de problemas que vivo na própria academia: responder interessados em vários canais, transformar uma conversa em aula experimental, acompanhar matrículas, professores, turmas, recebimentos e evolução dos alunos.

Concebi o produto, participei da implementação técnica e o coloquei em produção na operação que administro. O objetivo é uma plataforma **comercializável para outras academias**, construída e exercitada em um negócio real.

## Jornada que o produto conecta

1. Um interessado chega pelo site, WhatsApp ou Instagram.
2. A **Giu** atende com contexto da academia e organiza o interesse.
3. A equipe acompanha a aula experimental, os próximos passos e o lead por etapa.
4. A matrícula conecta aluno, modalidade, mensalidade, presença e progresso.
5. Administração, professores, operação e alunos acessam visões apropriadas às suas funções.

O vídeo de 15 segundos apresenta o recorte **primeiro contato → experimental → lead organizado**. As demais capacidades são demonstradas pelos aplicativos e pela documentação pública.

## Produto em produção

| Frente | Entrega |
| --- | --- |
| Atendimento e CRM | Giu no WhatsApp, Instagram e chat; captação e acompanhamento de interessados. |
| Operação da academia | Alunos, matrículas, grade, check-in e mensalidades. |
| Experiência do aluno | Progresso em jiu-jítsu e Muay Thai, conteúdos e rotina de treino. |
| Recepção e caixa | Loja/PDV, geladeira e pagamentos com Pix. |
| Canais | Aplicação web e apps publicados para Android e iOS. |

## Engenharia e decisões

O produto usa uma aplicação React/TypeScript para web e mobile via Capacitor, com dados e autenticação em Supabase, funções de backend e regras de acesso por perfil. A Giu integra canais de atendimento com a operação. A arquitetura pública apresenta os componentes sem expor código privado, dados de alunos ou credenciais.

**Decisão de produto:** a academia real funciona como ambiente de operação e validação. Uma funcionalidade precisa servir ao professor, ao aluno e à recepção no dia a dia, além de passar pelos testes e pela publicação técnica.

## Evidências públicas

- [Ocean Flow Studio Fitness](https://oceanflow.fitness/) · [App web](https://app.oceanflow.fitness/)
- [App na Google Play](https://play.google.com/store/apps/details?id=com.oceanflow.academia) · [App na App Store](https://apps.apple.com/br/app/ocean-flow/id6813960353)
- [Arquitetura pública do ecossistema](https://github.com/AnselmoBorges/arquitetura_oceanflow)
- [Vídeo público sobre a Giu e OpenAI Realtime API](https://www.youtube.com/watch?v=njzJrfJF4jE)

*O código operacional permanece em repositórios privados. Este case documenta o domínio, as decisões e as entregas verificáveis publicamente.*
