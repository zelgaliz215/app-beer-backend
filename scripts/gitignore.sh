echo "env" > .gitignore

touch .gitignore && echo "env/" >> .gitignore

# Otra forma de hacerlo
cat <<EOF > .gitignore
env/
__pycache__/
*.pyc
EOF

# Forma alterna
echo "env/" > .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore