CREATE TABLE dbo.sensorData (
    [entryId] INT IDENTITY(1,1) PRIMARY KEY,
    [sensorId] INT NOT NULL,
    [temperature] FLOAT NOT NULL,
    [wind] FLOAT NOT NULL,
    [humidity] FLOAT NOT NULL,
    [co2] FLOAT NOT NULL,
    CHECK (sensorId >= 1),
    CHECK (sensorId <= 20),
    CHECK (temperature >= 8),
    CHECK (temperature <= 15),
    CHECK (wind >= 15),
    CHECK (wind <= 25),
    CHECK (humidity >= 40),
    CHECK (humidity <= 70),
    CHECK (co2 >= 500),
    CHECK (co2 <= 1500)
);