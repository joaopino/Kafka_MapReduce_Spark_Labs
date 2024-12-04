# Average Number of Friends by Age - Task #1
# Hadoop MapReduce

# Importing the libraries
from mrjob.job import MRJob
from mrjob.step import MRStep

# Creating the class
class MinTemperatureByCapital(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.get_temperature_mapper, reducer=self.minimum_temperature_reducer),
            # MRStep(reducer=self.output_reducer)
        ]

    # Maps in key-value pairs of Register of capital: Min Value
    def get_temperature_mapper(self, _, line):
        station, _, type, temperature,_,_,_,_ = line.split(',')
        capital = ''.join(filter(str.isalpha, station))
        if type == "TMIN":
            yield capital, int(temperature)

    # Reduces to only min value per capital
    def minimum_temperature_reducer(self, capital, temperature):
        # defines the positive infinite as the value of min_float
        yield capital, min(temperature)

    # Output the results
    # def output_reducer(self, capital, min_temperature):
    #     yield capital, min_temperature

if __name__ == '__main__':
    MinTemperatureByCapital.run()