# -*- coding: utf-8 -*-
import pandas as pd

"""Main module."""


'''
  Data Segmenter class
'''
class data_segmenter:
  '''
    Creates a data_segmenter object from a metadata file.
  '''
  def __init__(metadata_filepath):
    self.metadata = open(metadata_filepath, "r")
    

  '''
    Function: segment_by_time()
    Description: Segments the data file underlying the data_segmenter based on timestamps. Assumes that the data file has a 
                  timestamp column for segmentation and a values column, which we are interested in extracting.
    Input: Python list where the columns are (t_start, t_end, label) of desired segment. 
            t_start and t_end are UNIX timestamps.
            label is for different summary statistics of values between t_start and t_end.
    Output: outputs the segments as a dataframe in the format: t_start, t_end, array of values contained in the defined interval.
  '''
  def segment_by_time(desired_segments):
    file_df = pd.read_csv(self.metadata.filepath) # TODO: add a filepath field to the metadata.json file + script
    segmented_df = pd.DataFrame(columns=['t_start', 't_end', 'values'])
    
    for segment in desired_segments:
      t_start, t_end, label = segment[0], segment[0], segment[2]

      # extract the values from the rows that lie within our interval 
      curr_segment_df = file_df[file_df['timestamp'].between(t_start, t_end, inclusive=True)]
      accepted_values = curr_segment_df['value'].tolist()
      
      segmented_df.append([t_start, t_end, accepted_values])

    return segmented_df

  def segment_by_sample_size():
    pass # to be implemented later








