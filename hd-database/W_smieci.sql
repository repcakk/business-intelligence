CREATE TABLE [dbo].[W_smieci]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [czy_odszedl] NCHAR(3) NULL,
    [tempo_pracy] NVARCHAR(100) NULL, 
    [etap] NVARCHAR(100) NULL
)
