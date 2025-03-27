## Performance Analysis of Mutation Tools for Banking Application
### Project Overview
This project evaluates the performance of mutation testing tools, MutPy and Mutatest, in a banking application. The goal is to assess their effectiveness in injecting and detecting faults while analyzing their performance under load using Locust.

### Approach
**Mutation Testing**: Injects controlled faults using MutPy and Mutatest.\
**Test Execution**: Uses Python’s unittest framework to evaluate detection rates.\
**Load Testing**: Simulates multiple users in Locust to measure performance impact.

### Technologies Used
**Mutation Testing**: MutPy, Mutatest\
**Performance Testing**: Locust\
**Programming Language**: Python\
**Testing Frameworks**: pytest, unittest

### Prerequisites
Ensure you have Python 3.8+ to 3.10 installed.

### How to Run
```
pip install mutpy
pip install mutatest
pip install locust
```

### Run mutation testing
- Using MutPy:
```
python "path/to/your/mut.py" --target BankApplication --unit-test test_BankApplication -m
```

- Using Mutatest:
```
mutatest --src "path/to/your/code" -s BankApplication.py -t "pytest"
```

### Start Locust for load testing:
```
locust -f locustfile.py -u 10 -r 2 --run-time 1m --csv=results  
```
For more details on Locust, refer to the documentation [Locust website](https://locust.io/) for usage.

### Conclusion
This study provides insights into selecting the optimal mutation testing tool for banking applications while ensuring high fault detection and efficient performance under stress.

