import requests

def is_mxui_mentioned(url):
    """Check if 'mxui.js' is mentioned in the page source of the given URL."""
    try:
        response = requests.get(url)
        # Check if 'mxui.js' is in the response content
        if 'mxui.js' in response.text:
            return True
    except requests.exceptions.RequestException as e:
        print(f"Error checking URL {url}: {e}")
    return False

def main(input_file, output_file):
    urls_with_mxui = []

    # Read URLs from the input file
    with open(input_file, 'r') as file:
        urls = file.readlines()

    # Check each URL
    for url in urls:
        url = url.strip()  # Remove any leading/trailing whitespace
        if is_mxui_mentioned(url):
            print(f"'mxui.js' is mentioned at: {url}")
            urls_with_mxui.append(url)

    # Write URLs where 'mxui.js' is mentioned to the output file
    with open(output_file, 'w') as file:
        for url in urls_with_mxui:
            file.write(url + '\n')

if __name__ == "__main__":
    input_file = "input_urls.txt"  # Update this to your input file's path
    output_file = "urls_mentioning_mxui.txt"  # Update this to your desired output file's path
    main(input_file, output_file)
