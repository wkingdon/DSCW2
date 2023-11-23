CREATE TABLE dbo.sensorStats (
    [sensorId] INT NOT NULL PRIMARY KEY,
    CHECK (sensorId >= 1),
    CHECK (sensorId <= 20),
    [count] INT NOT NULL,
    CHECK (count >=0),
    [temperatureMin] FLOAT NOT NULL,
    [windMin] FLOAT NOT NULL,
    [humidityMin] FLOAT NOT NULL,
    [co2Min] FLOAT NOT NULL,
    CHECK (temperatureMin >= 8),
    CHECK (temperatureMin <= 15),
    CHECK (windMin >= 15),
    CHECK (windMin <= 25),
    CHECK (humidityMin >= 40),
    CHECK (humidityMin <= 70),
    CHECK (co2Min >= 500),
    CHECK (co2Min <= 1500),
    [temperatureMax] FLOAT NOT NULL,
    [windMax] FLOAT NOT NULL,
    [humidityMax] FLOAT NOT NULL,
    [co2Max] FLOAT NOT NULL,
    CHECK (temperatureMax >= 8),
    CHECK (temperatureMax <= 15),
    CHECK (windMax >= 15),
    CHECK (windMax <= 25),
    CHECK (humidityMax >= 40),
    CHECK (humidityMax <= 70),
    CHECK (co2Max >= 500),
    CHECK (co2Max <= 1500),
    [temperatureAvg] FLOAT NOT NULL,
    [windAvg] FLOAT NOT NULL,
    [humidityAvg] FLOAT NOT NULL,
    [co2Avg] FLOAT NOT NULL,
    CHECK (temperatureAvg >= 8),
    CHECK (temperatureAvg <= 15),
    CHECK (windAvg >= 15),
    CHECK (windAvg <= 25),
    CHECK (humidityAvg >= 40),
    CHECK (humidityAvg <= 70),
    CHECK (co2Avg >= 500),
    CHECK (co2Avg <= 1500)
);