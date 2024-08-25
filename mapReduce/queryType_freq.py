from mrjob.job import MRJob
import csv

class QueryTypeFrequency(MRJob):
    
    def mapper(self, _, line):
        # Parse the CSV line
        row = next(csv.reader([line]))
        
        # Extract the QueryType and its frequency
        query_type = row[7]  # QueryType is at index 7
        frequency = 1
        
        # Emit QueryType as key and frequency as value
        yield query_type, frequency
        
    def reducer(self, query_type, frequencies):
        # Calculate the total frequency for each QueryType
        total_frequency = sum(frequencies)
        
        # Emit QueryType and its total frequency
        yield query_type, total_frequency

if __name__ == '__main__':
    QueryTypeFrequency.run()
