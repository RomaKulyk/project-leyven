This is a repository for pet project. Automation testing of e-commerce web site.

pytest --html=report.html - This tells pytest to create html report
pytest --count=3 - This tells pytest to repeat test cases 3 times

pytest -s --log-cli-level=DEBUG - This tells pytest to show log messages of
level DEBUG or higher in real time.

pytest -m with_logging --html=report.html  --log-cli-level=INFO - This tells
pytest to run all the test cases which have logiing process implemented.