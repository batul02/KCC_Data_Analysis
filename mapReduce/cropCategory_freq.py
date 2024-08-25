from mrjob.job import MRJob
import csv

class CropCategoryFrequency(MRJob):
    
    def mapper(self, _, line):
        # Parse the CSV line
        row = next(csv.reader([line]))
        
        # Extract the Crop Category and its frequency
        category = row[1]  # Category is at index 1
        frequency = 1
        
        # Emit Crop Category as key and frequency as value
        yield category, frequency
        
    def reducer(self, category, frequencies):
        # Calculate the total frequency for each Crop Category
        total_frequency = sum(frequencies)
        
        # Emit Crop Category and its total frequency
        yield category, total_frequency

if __name__ == '__main__':
    CropCategoryFrequency.run()
