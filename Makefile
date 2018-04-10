init: requirements.txt
	test -d venv || virtualenv -p python3 venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

test:
	. venv/bin/activate; py.test project/tests

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
