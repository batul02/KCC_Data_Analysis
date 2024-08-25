from mrjob.job import MRJob
import csv

class CropFrequency(MRJob):
    
    def mapper(self, _, line):
        # Parse the CSV line
        row = next(csv.reader([line]))
        
        # Extract the Crop and its frequency
        crop = row[5]  # Crop is at index 5
        frequency = 1
        
        # Emit Crop as key and frequency as value
        yield crop, frequency
        
    def reducer(self, crop, frequencies):
        # Calculate the total frequency for each Crop
        total_frequency = sum(frequencies)
        
        # Emit Crop and its total frequency
        yield crop, total_frequency

if __name__ == '__main__':
    CropFrequency.run()
