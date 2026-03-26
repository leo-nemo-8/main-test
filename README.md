# readme-api-docs

## Presentation

Ce depot contient les contenus de la documentation API Goodays publiee sur ReadMe.

Il s'agit d'un depot de contenu, pas d'un service applicatif :

- les pages de documentation vivent en Markdown avec front matter YAML ;
- la reference API est rattachee a un schema OpenAPI ;
- l'ordre de navigation est pilote par des fichiers `_order.yaml`.

## Introduction

La documentation API Goodays rassemble a la fois des pages d'onboarding et une reference detaillee des endpoints exposes par la plateforme.

On y trouve notamment :

- une partie `Getting Started` pour comprendre le positionnement de l'API, l'authentification, les erreurs, la pagination et les conventions generales ;
- des sections metier dediees aux principales familles d'API : `Core`, `Response`, `Metrics`, `Dashboard`, `Solicitation`, `Collect` et `Converse` ;
- des `Clients cases` qui illustrent des usages concrets cote integrateur ;
- une reference technique endpoint par endpoint, alignee sur le schema OpenAPI versionne dans le depot.

Autrement dit, ce portail sert a la fois de guide de prise en main et de reference contractuelle pour les integrations Goodays API.

## Ce que contient le depot

- `docs/` : guides fonctionnels et pages de contexte pour l'API.
- `reference/goodays-api.json` : source OpenAPI 3.0 de la Goodays API, version `v2`.
- `reference/Goodays API/` : pages de reference ReadMe reliees au schema via `api.file` et `operationId`.
- `reference/ReadMeConfig/` : configuration ReadMe masquee (getting started, auth, my requests).
- `custom_pages/` : pages custom ReadMe hors navigation standard.

Au moment de la redaction, le depot contient 32 pages dans `docs/`, 66 pages dans `reference/` et 3 pages dans `custom_pages/`.

## Structure de la documentation

Les grandes sections actuellement publiees sont :

- `Getting Started`
- `Core API`
- `Response API`
- `Metrics API`
- `Dashboard API`
- `Solicitation API`
- `Collect API`
- `Converse API`
- `Clients cases`

La navigation de premier niveau est definie par [`docs/_order.yaml`](./docs/_order.yaml) et [`reference/_order.yaml`](./reference/_order.yaml).

## Modifier le contenu

### 1. Mettre a jour une page de guide

Editez le fichier Markdown concerne dans `docs/`.

Points d'attention :

- conserver le front matter YAML en tete de fichier ;
- conserver les slugs et liens internes existants (`doc:` et `ref:`) ;
- mettre a jour le `_order.yaml` du dossier si vous ajoutez, retirez ou deplacez une page.

### 2. Mettre a jour la reference API

La reference repose sur deux couches :

- le contrat OpenAPI dans [`reference/goodays-api.json`](./reference/goodays-api.json) ;
- les pages wrappers dans `reference/Goodays API/**`, qui pointent vers le schema avec `operationId`.

Pour ajouter ou modifier un endpoint :

1. mettez a jour `reference/goodays-api.json` ;
2. verifiez que la page Markdown correspondante existe bien dans `reference/Goodays API/...` ;
3. verifiez que l'`operationId` du wrapper correspond exactement a celui du schema ;
4. ajustez les `_order.yaml` si la navigation change.

### 3. Mettre a jour une page custom

Les pages de `custom_pages/` servent a des contenus particuliers, parfois caches ou embarquant du HTML.

Soyez prudent avec :

- les blocs `<HTMLBlock>` ;
- les iframes ;
- les pages bilingues suffixees `_fr` / `_en`.

## Conventions a respecter

- Conserver le front matter YAML de ReadMe (`title`, `excerpt`, `hidden`, `metadata`, etc.).
- Conserver les composants ReadMe existants comme `<Image>`, `<Table>` et `<HTMLBlock>`.
- Garder des noms de fichiers stables : dans ReadMe, ils servent souvent de slug ou de cible de navigation.
- Modifier les `_order.yaml` en meme temps que l'arborescence.
- Eviter les liens absolus internes quand un lien `doc:` ou `ref:` existe deja.

## Validation avant commit

- verifier que le Markdown reste lisible dans ReadMe ;
- verifier que les liens `doc:` / `ref:` pointent vers des pages existantes ;
- verifier que les composants ReadMe sont bien fermes ;
- verifier que les nouvelles operations OpenAPI ont un `operationId` unique ;
- relire les pages masquees (`hidden: true`) si elles sont utilisees par la config du portail.

## Limites du depot

Ce depot ne contient ni application a lancer, ni CI, ni script de publication versionne a la racine.

Autrement dit :

- il n'y a pas de `package.json`, `Makefile` ou workflow CI local a utiliser tel quel ;
- la publication / synchronisation ReadMe est geree en dehors de ce depot, ou via des outils non versionnes ici.