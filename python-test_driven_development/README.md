# Projet Python : Développement piloté par les tests (TDD)

Ce projet contient plusieurs modules Python, chacun avec une fonction spécifique, et des tests associés pour vérifier leur fonctionnement correct.

## Modules

1. `0-add_integer.py` : Contient la fonction `add_integer(a, b)` qui ajoute deux entiers ou flottants.
2. `2-matrix_divided.py` : Contient la fonction `matrix_divided(matrix, div)` qui divise tous les éléments d'une matrice par un nombre.
3. `3-say_my_name.py` : Contient la fonction `say_my_name(first_name, last_name)` qui imprime "My name is <first name> <last name>".
4. `4-print_square.py` : Contient la fonction `print_square(size)` qui imprime un carré avec le caractère `#`.
5. `5-text_indentation.py` : Contient la fonction `text_indentation(text)` qui imprime un texte avec deux nouvelles lignes après chaque caractère `.`, `?` et `:`.

## Tests

Chaque module a un fichier de test associé dans le dossier `tests`. Pour exécuter tous les tests, utilisez la commande suivante :

```bash
python3 -m doctest -v ./tests/*
```

## Utilisation

Pour utiliser une fonction, importez-la depuis son module. Par exemple, pour utiliser la fonction `add_integer`, faites comme suit :

```python
from 0-add_integer import add_integer

result = add_integer(1, 2)
print(result)  # Affiche : 3
```

## Contribution

Les contributions à ce projet sont les bienvenues. Si vous trouvez un bug ou si vous voulez ajouter une nouvelle fonctionnalité, n'hésitez pas à créer une issue ou une pull request.
