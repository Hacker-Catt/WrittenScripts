import requests
import urllib3

# Disable SSL certificate verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def is_mxui_mentioned(url):
    """Check if 'mxui.js' is mentioned in the page source of the given URL."""
    try:
        # Ensure the URL starts with http:// or https://
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        # Ignore SSL certificate verification
        response = requests.get(url, verify=False)
        if 'mxui.js' in response.text:
            return True
    except (requests.exceptions.RequestException, 
            requests.exceptions.SSLError, 
            requests.exceptions.ConnectionError) as e:
        print(f"Error checking URL {url}: {e}")
    return False

def main(input_file, output_file):
    urls_with_mxui = []

    # Read URLs from the input file
    with open(input_file, 'r') as file:
        urls = file.readlines()

    total_urls = len(urls)
    print(f"Total URLs to check: {total_urls}")

    # Check each URL
    for index, url in enumerate(urls, start=1):
        url = url.strip()  # Remove any leading/trailing whitespace
        if is_mxui_mentioned(url):
            print(f"'mxui.js' is mentioned at: {url}")
            urls_with_mxui.append(url)

        # Calculate and print progress
        progress = (index / total_urls) * 100
        if progress >= 25 and index == round(total_urls * 0.25):
            print(f"25% completed, {total_urls - index} URLs left.")
        elif progress >= 50 and index == round(total_urls * 0.5):
            print(f"50% completed, {total_urls - index} URLs left.")
        elif progress >= 75 and index == round(total_urls * 0.75):
            print(f"75% completed, {total_urls - index} URLs left.")

    # Write URLs where 'mxui.js' is mentioned to the output file
    with open(output_file, 'w') as file:
        for url in urls_with_mxui:
            file.write(url + '\n')

    # Print summary
    print(f"Out of the {total_urls} URLs, {len(urls_with_mxui)} were found containing the mxui.js file.")
    print(f"The URLs have been saved in {output_file}")
    print("Happy hunting!")

if __name__ == "__main__":
    input_file = "input_urls.txt"  # Update this to your input file's path
    output_file = "urls_mentioning_mxui.txt"  # Update this to your desired output file's path
    main(input_file, output_file)
