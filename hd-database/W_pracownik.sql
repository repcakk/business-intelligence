CREATE TABLE [dbo].[W_pracownik]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [imie_nazwisko] NVARCHAR(100) NULL, 
    [pesel] NCHAR(11) NULL, 
    [doswiadczenie] NVARCHAR(100) NULL, 
    [wynagrodzenie] NVARCHAR(100) NULL, 
    [szef_id] INT NULL, 
    CONSTRAINT [FK_W_pracownik_W_pracownik] FOREIGN KEY ([szef_id]) REFERENCES [W_pracownik]([id])
)
