@echo off
pushd app1\test
coverage run -m unittest discover && coverage xml
popd

