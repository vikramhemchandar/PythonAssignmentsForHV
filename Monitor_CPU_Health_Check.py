"""
As a DevOps engineer, it is crucial to monitor the health and performance of servers. Write a Python program to monitor the health of the CPU. 
Few pointers to be noted:
   The program should continuously monitor the CPU usage of the local machine.
   If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.
   The program should run indefinitely until interrupted.
   The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.
Hint:
   The psutil library in Python can be used to retrieve system information, including CPU usage. You can install it using pip install psutil.
   Use the psutil.cpu_percent() method to get the current CPU usage as a percentage.
Expected Output:
Monitoring CPU usage...
Alert! CPU usage exceeds threshold: 85%
Alert! CPU usage exceeds threshold: 90%
... (continues until interrupted) 
"""

#First install psutil - pip install psutil

import psutil

print("***Monitoring CPU Usage***")

def main():
   while True:
      #Checking the CPU Usage
      cpu_usage = psutil.cpu_percent(interval=1)

      #Below print statement is written optional to check the current CPU Usage
      print(f'Current CPU Usage is :  {cpu_usage}%')
      
      #Condition to check if CPU Usage is greater than 85% and lesser than 90%
      if(cpu_usage >=85 and cpu_usage <90):
         print("Alert! CPU usage exceeds threshold: 85%")
      
      #Condition to check if CPU Usage is greater than 90%
      elif(cpu_usage >=90):
         print("Alert! CPU usage exceeds threshold: 90%")
      
      #Program continues till it is uninterrupted

if __name__ == "__main__":
   main()
