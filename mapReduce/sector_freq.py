from mrjob.job import MRJob
import csv

class SectorFrequency(MRJob):
    
    def mapper(self, _, line):
        # Parse the CSV line
        row = next(csv.reader([line]))
        
        sector = row[9]  # Sector is at index 9
        
        # If sector is found, emit it with frequency 1
        if sector:
            yield sector, 1
        
    def reducer(self, sector, frequencies):
        # Calculate the total frequency for each sector
        total_frequency = sum(frequencies)
        
        # Emit sector and its total frequency
        yield sector, total_frequency

if __name__ == '__main__':
    SectorFrequency.run()
