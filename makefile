.DEFAULT_GOAL := test

FILES :=					\
	app/models.py       	\
	app/tests.py        	\
	app/insert_records.py	\
	app/db_manager.py		\
	IDB2.html				\
	IDB2.log				\
	IDB2.pdf				\
	.travis.yml

ifeq ($(shell uname), Darwin)          # Apple
	PYTHON   := python3.5
	PIP      := pip3.5
	PYLINT   := pylint
	COVERAGE := coverage-3.5
	PYDOC    := pydoc
	AUTOPEP8 := autopep8
	VENV="venv/lib*"
else ifeq ($(CI), true)                # Travis CI
	PYTHON   := python3.5
	PIP      := pip3
	PYLINT   := pylint
	COVERAGE := coverage
	PYDOC    := pydoc3
	AUTOPEP8 := autopep8
	VENV="/home/travis/virtualenv/*"
else ifeq ($(shell uname -p), unknown) # Docker
	PYTHON   := python2.7
	PIP      := pip3.5
	PYLINT   := pylint
	COVERAGE := coverage-3.5
	PYDOC    := pydoc
	AUTOPEP8 := autopep8
	VENV="venv/lib*"
else                                   # UTCS
	PYTHON   := python3.5
	PIP      := pip3
	PYLINT   := pylint
	COVERAGE := coverage
	PYDOC    := pydoc3
	AUTOPEP8 := autopep8
	VENV="venv/lib*"
endif

.pylintrc:
	$(PYLINT) --generate-rcfile > $@

IDB2.html: app/models.py
	python3 -m pydoc -w app/models.py
	mv models.html IDB2.html

IDB2.log:
	git log > IDB2.log


check:
	@	not_found=0;                                 \
	for i in $(FILES);                            \
	do                                            \
		if [ -e $$i ];                            \
		then                                      \
			echo "$$i found";                     \
		else                                      \
			echo "$$i NOT FOUND";                 \
			not_found=`expr "$$not_found" + "1"`; \
		fi                                        \
	done;                                         \
	if [ $$not_found -ne 0 ];                     \
	then                                          \
		echo "$$not_found failures";              \
		exit 1;                                   \
	fi;                                           \
	echo "success";

	-$(PYLINT) --reports=y --disable=locally-disabled app/tests.py  > tests.out

	coverage run app/tests.py >> tests.out 
	coverage report --omit=$(VENV) -m >> tests.out
	cp tests.out app/static/tests.txt
	cat tests.out

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -f  *.tmp

test: IDB2.html IDB2.log tests.out
	ls -al
	make check

versions:
	which make
	make --version
	@echo
	which git
	git --version
	@echo
	which $(PYTHON)
	$(PYTHON) --version
	@echo
	which $(PIP)
	$(PIP) --version
	@echo
	which $(PYLINT)
	$(PYLINT) --version
	@echo
	which $(COVERAGE)
	$(COVERAGE) --version
	@echo
	-which $(PYDOC)
	-$(PYDOC) --version
	@echo
	which $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	$(PIP) list

pretty:
	$(AUTOPEP8) . --in-place --recursive --verbose --exclude ./venv



