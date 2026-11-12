# Setup
Cada equipo debe hacer un fork desde este repo.

## Una unica vez
```commandline
git clone https://github.com/Alumno/BlaBlaTuring2627.git
cd blablacturing
git remote add upstream https://github.com/DavidHormigoRamirez/BlaBlaTuring2627.git
git remote -v    # origin = fork, upstream = repositorio del profesor
```

## Trabajo diario
```commandline
# 1. Sync main with upstream
git checkout main
git fetch upstream
git merge upstream/main          # or: git rebase upstream/main
git push origin main

# 2. Work on a feature branch (never directly on main)
git checkout -b vehicles/add-vehicle-model

# 3. Commit small and often
git add .
git commit -m "vehicles: add Vehicle model"

# 4. Before opening the PR, bring the branch up to date
git fetch upstream
git rebase upstream/main

# 5. Push to the fork and open a PR against upstream/main
git push origin vehicles/add-vehicle-model

```
