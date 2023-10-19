# MySQL Fast Repair Script

## Overview

This Python program serves as a MySQL database maintenance tool. It allows you to perform various operations on your MySQL database, including creating backups, cleaning up unnecessary files and folders, and restoring data from backups.

## Features

- **Select MySQL Directory**: The program opens a file dialog, enabling you to select the directory where your MySQL database is located.

- **Create Backup**: It creates a backup of the "data" directory and stores it in a directory named "data_old" to ensure data safety.

- **Remove Unnecessary Folders**: The tool cleans up corrupted files in folders: "mysql," "performance_schema," "phpmyadmin," and "test" from the "data" directory.

- **Delete Unnecessary Files**: Unnecessary files are removed from the data directory, with the exception of a file named "ibdata1."

- **Restore from Backup**: You can restore your database from a previously created backup located in the "backup" directory.

## Usage

1. Run the program, and a file dialog will open.
2. Select the directory where your MySQL database is located.
3. The program will create a backup, remove unnecessary folders and files, and restore the database from a backup.
4. A message will inform you when the operation is complete.

## Prerequisites

- Python 3.x
- tkinter library (usually included with Python)
- A MySQL database installed and configured

## Troubleshooting

- If you encounter an error, ensure that the correct directory is selected when prompted.
- In case of a wrong directory error, restart the program and select the correct directory.

## Contributing

Contributions and suggestions are welcome. Feel free to create issues or submit pull requests to improve this tool.

## License

This program is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

Special thanks to the Python community and contributors who have helped develop and improve this tool.

---
**Note:** This tool is provided as-is, and the user should exercise caution when using it to manipulate MySQL databases. It is advisable to make a complete backup of your data before running any maintenance tasks.

## Download

You can download the latest release of the MySQL Fast Repair Script from the following link:
[MySQL Fast Repair Script v1.0](https://github.com/Inexpli/MySQL-FRS/releases/tag/v1.0)
