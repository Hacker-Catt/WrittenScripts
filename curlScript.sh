#!/bin/bash

input_file="inputFile.txt"   # Replace with the path to your input file
output_file="output.txt"    # Replace with the desired output file

while IFS= read -r url; do
    url_without_protocol="${url#https://}"  # Remove 'https://' prefix
    echo "URL: $url_without_protocol" >> "$output_file"
    echo "Response:" >> "$output_file"
    curl -L "https://$url_without_protocol" >> "$output_file"  # Use -L option if you want to fo>    echo -e "\n=================================================\n" >> "$output_file"
done < "$input_file"

echo "Script executed successfully. Check '$output_file' for the responses."

# Script deletes the https:// part from url and runs it through curl -L
# Edited as Https:// gives issues

# Credits to HackerCatt
