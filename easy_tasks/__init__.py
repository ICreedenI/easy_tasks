from .closest_furthest_value import (closest_value_in_dict,
                                     closest_value_in_list,
                                     furthest_value_in_dict,
                                     furthest_value_in_list,
                                     get_first_from_list)
from .dublicates import find_dublicates, remove_dublicates
from .filesystem import (copied_paths_to_list, copy_and_integrate_directory,
                         copy_file, copy_with_metadata, copy_without_metadata,
                         copy_without_metadata_using_copyfile,
                         delete_empty_directories, delete_path,
                         get_all_subdir_sizes, get_directory_size,
                         get_disc_informations, get_file_size,
                         move_and_integrate_directory, move_file)
from .help_with_json import dump_as_json, get_from_json
from .help_with_pickle import pickle_pack, pickle_unpack
from .list_printer import (get_var_names, pretty_print_list,
                           pretty_print_nested_list)
from .percentage import (ProgressBar, get_percentage_as_fitted_string,
                         main_and_sub_progress_printer, progress_printer)
from .rounding import *
from .sorter import sorted_dict
from .stoppable_thread import StoppableThread, ThreadWithExc
from .string_transformation import (comment_lines_by_lineno,
                                    comment_lines_in_file, insert_into_file,
                                    insert_into_string, remove_lines_by_lineno,
                                    replace_in_file, replace_in_string,
                                    upper_case_first_letter_of_word,
                                    upper_case_first_letter_of_words)
from .types import *
from .unpack import unpack_list
from .zipping import (make_zip_archive_with_shutil,
                      unpack_zip_archive_with_shutil, unzip_with_zipfile,
                      zip_dir_with_zipfile)

__version__ = "0.0.59"
