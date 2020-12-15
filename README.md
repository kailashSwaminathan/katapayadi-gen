# katapayadi-gen
Generator of word sequences in संस्कृतं for numerical input based on the कटपयादि schema

The कटपयादि is a scheme used to encode numerical entities (like date of composition, value of pi, etc)
in prose/poetry.

## introduction

Following verse found in Śaṅkaravarman's Sadratnamāla explains this scheme. 

    नञावचश्च शून्यानि संख्या: कटपयादय:। 
    मिश्रे तूपान्त्यहल् संख्या न च चिन्त्यो हलस्वर:॥
	
Rules 

  - *na* (न), *nya* (ञ) and *a* (अ)-s, i.e., vowels represent zero. 
  - The nine integers are represented by consonant group beginning with*ka*, *ṭa*, *pa*, *ya*. 
  - In a conjunct consonant, the last of the consonants alone will count. 
  - A consonant without a vowel is to be ignored.

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
	  
  - Open the main.py using the IDLE and press Shift+F5 to open a 
    text entry dialog to pass command line arguments.
  - 
  
## acknowledgements

The inspiration for this work is the course titled "Computational Thinking in Indic Tradition"
delivered by Prof.Gopinath Kanchi (Dept.of CSA, IISc., Bangalore) and Dr.Shailaja D.Sharma(Adj.Prof., NIAS, Bangalore)
as the part of the Centre for Continuing Education (IISc.) Proficience Courses conducted from August to December 2020.
