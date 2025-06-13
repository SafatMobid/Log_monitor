Log File Monitor & Alert System

+++++ FOR REAL-TIME LOG MONITORING +++++

My next Personal Python project designed to monitor application or system log files in real-time. It scans for critical messages such as ERROR and WARNING, prints alerts to the console, and logs findings to a separate file for tracking.

I chose this as my next project to tackle because I wanted to simulate a real-world application support task—actively monitoring systems and detecting issues before they escalate. It's also a great way to understand better how logs work and how to build lightweight alerting systems for troubleshooting.

Useful for real-time diagnostics and system health monitoring

Helps sharpen regex and file I/O skills

Simulates what support engineers often do manually or with more complex tools

Monitors:

Any .log file (sample: sample_log.log inside log/ folder)

Automatically tracks for new entries

Detects and flags lines containing ERROR or WARNING

Logs to:

monitor.log (tracks detection activity)

Libraries Used:

os

time

re

csv

For email capabilities (planned):

smtplib

schedule

json

+++++ Alert Example Console Output +++++

[ALERT] ERROR detected in sample_log.log
Time: 2025-06-13 12:14:08
Message: Connection timeout on service restart
TO BE ADDED:

Email alerts on detection

Autorun on OS startup

Auto-discover and track new .log files in specified directories

Filter by severity level or custom keywords

Log rotation support

By building this, my skills in system monitoring, automation, and alerting workflows have grown significantly. I’ve deepened my knowledge of real-time file handling, regular expressions, and Python’s scheduling and email libraries—all crucial for developing production-ready support tools.
