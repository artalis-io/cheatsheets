.PHONY: cheatsheets cheatsheet cheatsheets-check cheatsheets-test cheatsheets-clean

cheatsheets:
	python3 scripts/cheatsheets.py build

cheatsheet:
	@test -n "$(NAME)" || (echo "usage: make cheatsheet NAME=tmux" >&2; exit 2)
	python3 scripts/cheatsheets.py build "$(NAME)"

cheatsheets-check:
	python3 scripts/cheatsheets.py check

cheatsheets-test:
	python3 -m unittest discover -s tests -v

cheatsheets-clean:
	python3 scripts/cheatsheets.py clean

