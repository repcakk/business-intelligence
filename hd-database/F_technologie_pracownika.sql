CREATE TABLE [dbo].[F_technologie_pracownika]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [pracownik_id] INT NULL, 
    [technologia_id] INT NULL, 
    CONSTRAINT [FK_F_technologie_pracownika_W_pracownik] FOREIGN KEY ([pracownik_id]) REFERENCES [W_pracownik]([id]),
    CONSTRAINT [FK_F_technologie_pracownika_W_technologia] FOREIGN KEY ([technologia_id]) REFERENCES [W_technologia]([id])
)
