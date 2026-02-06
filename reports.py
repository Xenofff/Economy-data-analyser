from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self, data):
        pass

class AverageGDPReport(Report):
    def generate(self, data):
        if not data: return []
        stats = {}
        for row in data:
            country = row['country']
            gdp = float(row['gdp'])
            if country not in stats:
                stats[country] = []
            stats[country].append(gdp)

        result = []
        for country, values in stats.items():
            avg = sum(values) / len(values)
            result.append([country, avg])

        return sorted(result, key=lambda x: x[1], reverse=True)