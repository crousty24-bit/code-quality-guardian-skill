# Code Quality Guardian - Vision Projet

## Postulat

Code Quality Guardian existe parce que les agents IA produisent souvent trop de code, trop vite, avec trop de certitude.

Le risque cible n'est pas seulement du "mauvais code". Le risque cible est l'intervention agentique mal disciplinée :

- ajouter des fichiers inutiles ;
- créer des abstractions décoratives ;
- importer une architecture étrangère au projet ;
- ajouter des dépendances sans justification ;
- refactorer trop large ;
- changer du comportement sans le dire ;
- prétendre avoir vérifié sans preuve.

## Vision MVP

Le skill doit rester un orchestrateur léger de discipline d'intervention.

Il doit aider l'agent à :

- observer avant d'agir ;
- limiter le diff ;
- préserver le comportement existant ;
- respecter les conventions de la codebase ;
- décider quand une pratique spécialisée est réellement nécessaire ;
- vérifier honnêtement ce qui a été fait.

La promesse centrale est : changer moins, mais mieux.

## Ce Que Ce Skill N'Est Pas

Code Quality Guardian n'est pas :

- un guide exhaustif de clean code ;
- une copie de `code-review-and-quality` ;
- une copie de `code-simplification` ;
- un framework complet de review, sécurité, performance, tests ou architecture ;
- un skill framework-specific ;
- un prétexte pour élargir chaque tâche à une refonte globale.

Les skills spécialisés restent les meilleures références pour leur domaine. Code Quality Guardian décide quand les invoquer ou s'en inspirer.

## Références Conceptuelles

Les notes Obsidian du projet sont la vérité initiale pour la vision et le positionnement.

Les skills suivants sont des références de patterns validés, pas du contenu à recopier :

- `code-review-and-quality` pour les axes de review, la taille des changements et la discipline de dépendances ;
- `code-simplification` pour préserver le comportement et éviter le churn ;
- `incremental-implementation` pour les petits incréments vérifiables ;
- `test-driven-development` pour les bug fixes et comportements critiques ;
- `debugging-and-error-recovery` pour le diagnostic fondé sur preuves ;
- `api-and-interface-design`, `security-and-hardening`, `performance-optimization` et `git-workflow-and-versioning` pour les concerns spécialisés.

## Règles D'Évolution

Toute évolution du skill doit respecter ces règles :

- renforcer la différenciation anti-surproduction IA ;
- rester courte et actionnable ;
- éviter de copier des checklists spécialisées ;
- préférer une règle de délégation à une section exhaustive ;
- garder `SKILL.md` compact ;
- déplacer les détails longs dans `references/` seulement s'ils changent réellement le comportement de l'agent ;
- n'ajouter que des scripts read-only, Python stdlib, sans réseau et sans rewrite ;
- ne pas prétendre à une publication stable avant exemples courts, tests terrain et retours réels.

## Futurs Skills Possibles Après Validation Terrain

Ne pas créer ces skills maintenant. Les garder en backlog jusqu'à ce que des validations terrain montrent un workflow autonome, utile seul et distinct de `code-quality-guardian`.

- `agent-change-auditor` : auditer un diff ou une PR générée par agent pour détecter scope creep, fichiers inattendus, vérification manquante et dépendances ajoutées.
- `codebase-risk-scout` : cartographier les zones à risque avant intervention à partir de signaux read-only.
- `verification-discipline` : cadrer la stratégie de vérification et distinguer preuve, signal et hypothèse non vérifiée.
- `refactor-scope-control` : refuser ou réduire les refactors trop larges quand une intervention locale suffit.

## MVP Actuel

Le repo est un MVP draft non publié.

`templates/` est réservé pour une passe ultérieure. La licence MIT est définie. Les scripts restent strictement read-only.
