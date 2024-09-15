
# File Handler Streamlit Application

## Overview

The File Handler Streamlit application allows users to manage files by specifying source and destination paths, choosing between copying or moving files, and filtering by file extensions. The application features a reset function to clear all inputs and restore default settings.

## Features

- **Input Fields**: Specify source and destination file paths.
- **Action Selection**: Choose between 'Copy' or 'Move' for file operations.
- **File Extension Filtering**: Select file extensions to filter files.
- **Reset Functionality**: Clear inputs and revert to default settings.

## Prerequisites

- Python 3.x
- Streamlit and other dependencies listed in `requirements.txt`

## Installation

1. **Clone or Download the Repository**

   Clone the repository or download the application files to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Application Directory**

   Open a terminal or command prompt and navigate to the directory containing `app.py`, `run.bat`, and `requirements.txt`.

3. **Set Up the Environment**

   - **Windows**

     Run the `run.bat` file. This batch script will create a virtual environment, install the required packages, and start the Streamlit server.

     ```batch
     run.bat
     ```

   - **Manual Setup (Alternative)**

     If you prefer manual setup, you can create a virtual environment and install dependencies as follows:

     ```bash
     python -m venv venv_handler
     ```

     Activate the virtual environment:

     - **Windows:**

       ```bash
       venv_handler\Scripts\activate
       ```

     - **macOS/Linux:**

       ```bash
       source venv_handler/bin/activate
       ```

     Install the required packages:

     ```bash
     pip install -r requirements.txt
     ```

     Start the Streamlit server:

     ```bash
     streamlit run app.py
     ```

## Running the Application

1. **Start the Streamlit Server**

   Run the `run.bat` file or manually execute the commands as described above. The application will be launched, and you will be able to access it via a web browser.

2. **Access the Application**

   Open your web browser and navigate to:

   ```
   http://localhost:8501
   ```

   You should see the Streamlit application running.

## `requirements.txt`

The `requirements.txt` file contains the necessary Python libraries and their specific versions for running the application. The file includes:

```
altair==4.1.0
astor==0.8.1
attrs==24.2.0
base58==2.1.1
blinker==1.8.2
cachetools==5.5.0
certifi==2024.8.30
charset-normalizer==3.3.2
click==8.0.4
colorama==0.4.6
entrypoints==0.4
gitdb==4.0.11
GitPython==3.1.43
idna==3.8
importlib_metadata==8.5.0
Jinja2==3.1.4
jsonschema==4.23.0
jsonschema-specifications==2023.12.1
markdown-it-py==3.0.0
MarkupSafe==2.1.5
mdurl==0.1.2
narwhals==1.6.2
numpy==2.1.1
packaging==24.1
pandas==2.2.2
pillow==10.4.0
protobuf==3.20.3
pyarrow==17.0.0
pydeck==0.9.1
Pygments==2.18.0
Pympler==1.1
python-dateutil==2.9.0.post0
pytz==2024.1
pywin32==306
referencing==0.35.1
requests==2.32.3
rich==13.8.0
rpds-py==0.20.0
semver==3.0.2
six==1.16.0
smmap==5.0.1
streamlit==1.6.0
tenacity==8.5.0
toml==0.10.2
toolz==0.12.1
tornado==6.4.1
typing_extensions==4.12.2
tzdata==2024.1
tzlocal==5.2
urllib3==2.2.2
validators==0.34.0
watchdog==4.0.2
zipp==3.20.2
```

## Usage

1. **Input Fields**

   - **File Path**: Enter the path of the file to be processed.
   - **Output Path**: Enter the destination path where the file will be copied or moved.

2. **Action Selection**

   - Choose between 'Copy' and 'Move' to specify the action.

3. **File Extension Selection**

   - Select the file extensions you want to filter by.

4. **Submit**

   - Click the 'Submit' button to execute the selected action.

5. **Reset**

   - Click the 'Reset' button to clear all inputs and restore default settings.

## License

This application is provided under the MIT License. See the [LICENSE](LICENSE) file for more details.
