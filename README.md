Hash Checker and Cracker Tool
Overview
	This Python tool is designed to check and crack hash values using various hashing algorithms. It supports common algorithms like MD5, SHA-1, SHA-256, and more. The tool allows you to manually input 	words to check against a hash or use a wordlist for a more comprehensive attack.

Features
	Detects hash types based on hash length.
	Supports multiple hashing algorithms including MD5, SHA-1, SHA-256, SHA3 variants, and BLAKE2.
	Allows checking against a list of words or a wordlist file.
	Provides clear output when a password match is found.
	Requirements
	Python 3.x
	No external libraries required
  
Installation
	Clone the repository:

		git clone https://github.com/Amjithkchandran/live_hash_cracker.git
		
		cd hash-cracker-tool

Install dependencies:

	No additional dependencies are required beyond Python's standard library.

Usage
	Run the tool:

	Copy code
		D:\live_hash_cracker> python hash_cracker_tool.py
	
	Enter the hash value when prompted.

	Choose an option:

		Option 1: Enter words manually to check against the hash.
		Option 2: Use a wordlist file for cracking the hash.
  
		Follow the prompts to input words or specify the path to your wordlist file.

	Example
		Checking a hash with a list of words:
  
		Enter the hash value: 5f4dcc3b5aa765d61d8327deb882cf99
		
  	Choose an option:
		1. Enter words to check manually
		2. Use a wordlist to crack the hash
		Enter your choice (1 or 2): 1
  
		Enter words to check (comma-separated): password,123456,letmein
		Checking with MD5...
  
		Password found: password using MD5 with hash value: ***5f4dcc3b5aa765d61d8327deb882cf99***
  
	Cracking a hash with a wordlist:
 
		Enter the hash value: 5f4dcc3b5aa765d61d8327deb882cf99
  
		Choose an option:
		1. Enter words to check manually
		2. Use a wordlist to crack the hash
		Enter your choice (1 or 2): 2
  
		Enter the path to your wordlist: /path/to/wordlist.txt
		Attempting to crack using MD5...
  
		Password found: password using MD5 with hash value: ***5f4dcc3b5aa765d61d8327deb882cf99***
  
		Contributing
  
If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure that your code follows the existing style and is well-tested.

License
	This project is licensed under the MIT License - see the LICENSE file for details.
