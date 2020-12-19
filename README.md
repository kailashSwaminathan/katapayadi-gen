# katapayadi-gen
Generator of word sequences in संस्कृतं for numerical input based on the कटपयादि scheme.

The कटपयादि is a scheme used to encode numerical entities (like date of composition, value of pi, etc)
in Sanskrit prose/poetry.

## introduction

Following verse found in Śaṅkaravarman's Sadratnamāla explains this scheme. 

    नञावचश्च शून्यानि संख्या: कटपयादय:। 
    मिश्रे तूपान्त्यहल् संख्या न च चिन्त्यो हलस्वर:॥
	
Rules 

  - *na* (न), *nya* (ञ) and *a* (अ)-s, i.e., vowels represent zero. 
  - The nine integers are represented by consonant group beginning with*ka*, *ṭa*, *pa*, *ya*. 
  - In a conjunct consonant, the last of the consonants alone will count. 
  - A consonant without a vowel is to be ignored.

## syntax

The syntax is
  
    $> python main.py [--method=<brute>] [--mode=<single>] <number>
		
The कटपयादि (*katapayadi*) string is computed for the `number`. The method for generation of the 
कटपयादि string can be specified using the `method` option. The `mode` option is used to specify
the count of कटपयादि string generated. 

The supported values for the `method` option are
	
  - `brute`
  
    In this method, the characters for the digits of the `number` are determined 
	according to the कटपयादि scheme. From this, a list of all possible combination is
	computed. Each combination is further expanded, by adding *maathras* to each *akshara*
	in the combination. Again, for each *maathras* added combination, a maximum of 
	`n(=1, default)` *half vyanjanas* are added. Finally one of this expanded combination
	is chosen at random and given as output. Please be aware that, in this method,
	there is not checking whether the chosen output is a valid word in संस्कृतं. This is the
	default value for the `method` option.
    
The supported values for the `mode` option are 

  - `single`
  
    A single generated कटपयादि string is randomly selected and returned.

## install

Supported `python` version 3.x.

### Windows 

  - Create a virtual environment using `virtualenv`.
  - Activate the virtual environment.
  - Install the required packages
  
      $> pip install -r requirements.txt

## run

  - Start the python IDLE editor
  
        $> python -m idlelib.idle
	  
	This is required as I still havent figured out how to display unicode characters in
	Windows Command Prompt.    
	  
  - Open the main.py using the IDLE and press Shift+F5 to open a 
    text entry dialog to pass command line arguments. Enter the number for which the 
	कटपयादि sequence is required and optionally other options. Press Enter.
	
  - The कटपयादि sequence is printed in the IDLE shell.
  

## to do

  - Generate meaningful output by checking against a dictionary.
  
  
## acknowledgements

The inspiration for this work is the course titled **"Computational Thinking in Indic Tradition"**
delivered by **Prof.Gopinath Kanchi** (Dept.of CSA, IISc., Bangalore) and **Dr.Shailaja D.Sharma** (Adj.Prof., NIAS, Bangalore)
as the part of the Proficience Courses conducted by **Centre for Continuing Education (IISc.)** from August to December 2020.
