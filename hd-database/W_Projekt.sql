CREATE TABLE [dbo].[W_projekt]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [nazwa] NVARCHAR(100) NULL, 
    [tempo_realizacji] NVARCHAR(100) NULL, 
    [liczba_pracownikow] NVARCHAR(100) NULL, 
    [czas_trwania] NVARCHAR(100) NULL, 
    [data_rozpoczecia] INT NULL, 
    [data_zakonczenia] INT NULL,
    CONSTRAINT [FK_W_projekt_W_data_rozpoczecie] FOREIGN KEY ([data_rozpoczecia]) REFERENCES W_data([id]),
    CONSTRAINT [FK_W_projekt_w_projekcie_W_data_zakonczenie] FOREIGN KEY ([data_zakonczenia]) REFERENCES W_data([id])
)
