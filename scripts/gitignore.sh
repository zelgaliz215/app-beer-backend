echo "env" > .gitignore

touch .gitignore && echo "env/" >> .gitignore

# Otra forma de hacerlo
cat <<EOF > .gitignore
env/
__pycache__/
*.pyc
EOF