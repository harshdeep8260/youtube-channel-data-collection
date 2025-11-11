# YouTube Channel Data Collection

This tool allows you to collect metadata about all videos from a specified YouTube channel using the YouTube Data API v3. The collected data is saved in a parquet file.

## Setup

Before running the script, you'll need to obtain an API key from [Google Cloud Console](https://console.cloud.google.com/).
Make sure that YouTube Data API v3 is enabled for that key.
Add it to a `.env` file in the same directory as the `main.py` script.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/harsh4026/youtube-channel-data-collection.git
    cd youtube-channel-data-collection
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script:**
    ```bash
    python3 main.py
    ```

2. **Enter the YouTube channel ID. Example:**
    ```bash
    Enter channel ID: UCNIuvl7V8zACPpTmmNIqP2A
    ```

## Output

Once the script finishes execution, the collected video data will be saved to `data.parquet`.
This file will be located in the same directory where you ran the `main.py` script.
