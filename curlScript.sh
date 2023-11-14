#!/bin/bash

input_file="scriptInput.txt"   # Replace with the path to your input file
output_file="curlResults.txt"    # Replace with the desired output file

while IFS= read -r url; do
    echo "URL: $url" >> "$output_file"
    echo "Response:" >> "$output_file"
    curl -L "$url" >> "$output_file"  # Use -L option if you want to follow redirects
    echo -e "\n=================================================\n" >> "$output_file"
done < "$input_file"

echo "Script executed successfully. Check '$output_file' for the responses."

# Credits to HackerCatt
# File created to check if URLs give CURL -L response. input_file need to be the file with the URLs you want to check. output_file gets created after run.
