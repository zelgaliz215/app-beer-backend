git checkout -b scripts/installar-dependendias
git status
git add .
git commit -m "Agregando script para instalar dependencias y gestionar configuracion"
git push origin scripts/installar-dependendias

git checkout main
git merge scripts/installar-dependendias
git push origin main