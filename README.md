This is a repository for pet project. Automation testing of e-commerce web site.

*pytest --html=report.html* - This tells pytest to create html report
*pytest --count=3* - This tells pytest to repeat test cases 3 times

*pytest -s --log-cli-level=DEBUG* - This tells pytest to show log messages of level DEBUG or higher in real time.

*pytest -m with_logging --html=report.html*  --log-cli-level=INFO - This tells pytest to run all the test cases which have logiing process implemented.

*pytest -m with_logging --html=report_$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss').html --log-cli-level=INFO* - This tells pytest to run all the test cases which have logging process implemented and adds timestamp to the file name.

<<<<<<< HEAD
pytest .\testing\tests\ --html=report_$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss').html --log-cli-level=INFO - This tells pytest to run all the test cases and adds timestamp to the file name.
pytest -m "not with_logging" - This tells pytest to run all the test cases which
do not have "with_logging" mark.
=======
*pytest .\testing\tests\ --html=report_$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss').html --log-cli-level=INFO* - This tells pytest to run all the test cases and adds timestamp to the file name.
>>>>>>> 44e38e750a4c2cf996e7d2445d1de91e10e6083b
