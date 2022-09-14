# easy_taks

To not get annoyed by simple recurring tasks I created this small library.  

## Content
- Usage  

## Usage
- **furthest_value_in_list**  
  Function returning the closest number of a list to a given value

- **closest_value_in_list**  
  Function returning the closest number of a list to a given value

- **furthest_value_in_dict**  
  Function returning the closest number of a dicts values to a given value

- **closest_value_in_dict**  
  Function returning the closest number of a dicts values to a given value

- **find_dublicates**  
  Function returning a list of Dubs objects which have the properties: *value*, *number_of_dublicates* and *indices*

- **remove_dublicates**  
  Function returning a copy of the given list in which only the first occurrence of every value remains

- **get_percentage_as_fitted_string**  
  Function returning the calculated percentage from the inout count and total fittet to the string lenght of 100.00 %  
  args:
  - count: current counting value
  - total: total value 
  - round_to: rounding digits, default: 2
  - with_percentage_symbol: boolean, adds ' %' if True

- **progress_printer**  
  Call this funciton in a loop with index+1 as count to monitor your progress.  
  Will automatically switch to a new line when 100 % is reached.
  Remember to call print once if you break since the cursor will not move to the next line till 100 % are reached.

- **main_and_sub_progress_printer**  
  Basically the progress_printer with one susbprocess. 

- **upper_case_first_letter_of_word**  
  Function returning a string in which the word begins with an upper case letter.

- **upper_case_first_letter_of_words**  
  Function returning a string in which every word begins with an upper case letter.

- **unpack_list**  
  Dissolve inner lists and tuples of nested list and tuples.


## Links
[GitHub](https://github.com/ICreedenI/easy_tasks) | either [PyPI](https://pypi.org/project/easy_tasks/) or [PyPI](https://pypi.org/project/easy-tasks/)