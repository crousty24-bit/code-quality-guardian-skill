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
- n'ajouter que des scripts de détection read-only, Python stdlib, sans réseau, rewrite ou exécution de commandes projet ;
- ne pas prétendre à une publication stable avant exemples courts, tests terrain et retours réels.

## Enseignements De La Phase Terrain 1

La première campagne sur cinq repos confirme le comportement recherché :

- l'agent observe avant de modifier ;
- les changements restent limités et vérifiés ;
- les scripts sont interprétés comme des signaux, pas comme des verdicts ;
- la délégation reste conditionnelle au besoin réel ;
- aucun refactor massif ou ajout d'architecture injustifié n'a été observé.

Elle a aussi identifié trois limites à corriger :

- les scripts initiaux favorisaient les conventions JavaScript et détectaient mal Rails ;
- certains diagnostics confondaient une convention locale avec l'intention produit ;
- la méthodologie ne prouve pas encore un gain causal face à une vraie baseline sans skill.

Le support ajouté pour Rails/Ruby et Rust/Tauri reste ciblé sur des preuves terrain. Le projet ne doit pas annoncer une compatibilité universelle.

## Enseignements De La Phase Terrain 2

La seconde campagne confirme :

- la détection effective de Rails/Ruby et Rust/Tauri sur des projets réels ;
- la discipline de scope, le diff limité et la vérification honnête ;
- l'amélioration de la précision des diagnostics et de la gestion de l'intention produit ;
- l'absence de surarchitecture malgré des interventions multi-couches.

Elle révèle aussi que la décision binaire `stay local` ou `delegate` est insuffisante. Un résultat métier local peut nécessiter une coordination multi-fichier ou une délégation spécialisée lorsque la sécurité, les migrations, les contrats persistants ou la concurrence sont matériels.

Le skill distingue désormais :

- `Level 1 Local` : intervention contenue et faible risque d'exécution ;
- `Level 2 Coordinated` : objectif borné nécessitant plusieurs disciplines ou couches ;
- `Level 3 Specialized` : risque matériel nécessitant une expertise dédiée.

Code Quality Guardian conserve le contrôle du scope à tous les niveaux. Il orchestre les skills spécialisés sans copier leurs checklists.

## Futurs Skills Possibles Après Validation Terrain

Ne pas créer ces skills maintenant. Les garder en backlog jusqu'à ce que des validations terrain montrent un workflow autonome, utile seul et distinct de `code-quality-guardian`.

- `agent-change-auditor` : auditer un diff ou une PR générée par agent pour détecter scope creep, fichiers inattendus, vérification manquante et dépendances ajoutées.
- `codebase-risk-scout` : cartographier les zones à risque avant intervention à partir de signaux read-only.
- `verification-discipline` : cadrer la stratégie de vérification et distinguer preuve, signal et hypothèse non vérifiée.
- `refactor-scope-control` : refuser ou réduire les refactors trop larges quand une intervention locale suffit.

## MVP Actuel

Le repo est publié comme MVP expérimental `0.1.0-beta.1` après deux phases de validation terrain.

La licence MIT est définie. Les scripts restent strictement read-only et ne peuvent pas exécuter les commandes qu'ils détectent.

Une version stable post-bêta exige encore :

- une campagne comparative avec de vraies passes de contrôle sans skill installé ou activé ;
- au moins un repo de réserve non utilisé pendant l'élaboration ;
- le suivi séparé des faux positifs, de la taille des diffs et des vérifications réellement exécutées ;
- la validation des trois niveaux d'intervention sur des scénarios distincts ;
- la validation de l'installation publique depuis GitHub.
