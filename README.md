# Unit Test

## unittest module
python -m unittest -v test </br>
python -m unittest test


## Pytest module 
### pytest command line:
ex.
testSubDirectory -> test_file3.py </br>
test_file1.py </br>
test_file2.py </br>


1. pytest -v -s
2. pytest -v -s test_file1.py        =>(to test the specified file) </br>
3. pytest -v -s testSubDirectory/    =>(to test the specified file under testSubDirectory/) </br>
4. pytest -v -s -k "test2"           =>(to test the specified file using -k (keyword)"fileKeyword") </br>
5. pytest -v -s -k "test2 or test3"  =>(to test test_file2 and test_file3) </br>
6. pytest -v -s -m "test1 or test3"  =>(to test files that has @pytest.mark.test1 and @pytest.mark.test3 decorators) </br>




