Python System Health Monitor

A Python-based DevOps project that monitors basic system health information.

Features

* Operating System information
* Hostname and Python version
* CPU usage monitoring
* RAM usage monitoring
* Disk usage monitoring
* CPU, RAM and Disk threshold alerts
* Automatic report logging in a log file

Technologies Used

* Python 3.12
* Psutil
* Git and GitHub
* Ubuntu (WSL)

Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL
cd python-system-health-monitor

Create a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependency:

pip install psutil

Run the Project

python system_check.py

Alert Thresholds

* CPU usage above 80%: Warning
* RAM usage above 80%: Warning
* Disk usage above 80%: Warning

Log File

System reports are saved in system_health.log.

Author

Subham Kumar
