# Heartbeat Scraper

This Python script sends an HTTP request to a local server running on `localhost:12345`, extracts the heartbeat time from the HTML page, and checks if it matches the current time.

## Requirements

Before running the script, ensure you have the necessary dependencies installed.

### Install dependencies

Make sure to install the required Python libraries by running:

```bash
pip install requests beautifulsoup4
```
## Description

The script:

1. Sends a GET request to a specified URL (`http://localhost:12345`).
2. If the request is successful (status code 200), it parses the HTML content of the response using BeautifulSoup.
3. It looks for an HTML element with the ID `heartBeat` and compares its text content with the current timestamp formatted as `Heartbeat! YYYY-MM-DD HH:MM:SS`.
4. If the text matches the expected value, the script prints `"Success"`. Otherwise, it prints `"Failure"`.
5. If the request fails (i.e., status code is not 200), it prints an error message with the status code.

## How to Use

1. Ensure that the URL (`http://localhost:12345`) is pointing to a service that includes a heartbeat value in a `<p>` tag with the ID `heartBeat`.
2. Run the script with Python 3:

    ```bash
    python health_check.py
    ```

### Example Output

```bash
Success
```

If there is a mismatch, the output will be:

```bash
Failure
```

### Troubleshooting

- Ensure the target web page includes the heartbeat text in the correct format.
- Verify that the service at `http://localhost:12345` is running and accessible.
- Check for any network issues that might prevent the script from reaching the URL.
