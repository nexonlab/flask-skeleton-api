# Dependências
# Apenas Node por enquanto...
DEPS := docker npm node aglio
CHECK := $(foreach dep, $(DEPS), \
	$(if $(shell which $(dep)),\
		"Checando $(dep)...",\
		$(error "Dependência $(dep) não encontrado na $$PATH")\
	))

.PHONY: all

all:
	@echo "<TODO>"

clean:
	@echo "Removendo arquivos temporários"
	@echo "<TODO>"

tests:
	@echo "<TODO>"

# Node

docs:
	aglio -i ./app/docs/api-blueprint-sample.apib --theme-full-width --no-theme-condense -o ./app/templates/apidocs/index.html

# Flask

checa_virtualenv:
	@if [ -z "$(VIRTUAL_ENV)" ]; then \
		echo "ERROR: virtualenv não detectado." 1>&2;\
		exit 1;\
	fi

pip: checa_virtualenv
	@echo "<TODO>"

# Docker

compose:
	docker-compose up -d --build

