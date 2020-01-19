CREATE TABLE [dbo].[F_pracownik_w_projekcie]
(
	[Id] INT NOT NULL PRIMARY KEY, 
    [czas_trwania] INT NULL, 
    [pracownik_id] INT NULL, 
    [projekt_id] INT NULL, 
    [czy_odszedl_smieci_id] INT NULL, 
    [klient_id] INT NULL, 
    [etap_smieci_id] INT NULL, 
    [data_rozpoczecia] INT NULL, 
    [data_zakonczenia] INT NULL, 
    [tempo_pracy_smieci_id] INT NULL, 
    [uzyskany_dochod] INT NULL, 
    CONSTRAINT [FK_F_pracownik_w_projekcie_W_pracownik] FOREIGN KEY ([pracownik_id]) REFERENCES [W_pracownik]([id]), 
    CONSTRAINT [FK_F_pracownik_w_projekcie_W_projekt] FOREIGN KEY ([projekt_id]) REFERENCES W_projekt([id]),
    CONSTRAINT [FK_F_pracownik_w_projekcie_W_smieci_czy_odszedl] FOREIGN KEY ([czy_odszedl_smieci_id]) REFERENCES W_smieci([id]),
    CONSTRAINT [FK_F_pracownik_w_projekcie_W_klient] FOREIGN KEY ([klient_id]) REFERENCES W_klient([id]),
    CONSTRAINT [FK_F_pracownik_w_projekcie_W_smieci_etap] FOREIGN KEY ([etap_smieci_id]) REFERENCES W_smieci([id]),
    CONSTRAINT [FK_F_pracownik_w_projekcie_W_data_rozpoczecie] FOREIGN KEY ([data_rozpoczecia]) REFERENCES W_data([id]),
    CONSTRAINT [FK_F_pracownik_w_projekcie_W_data_zakonczenie] FOREIGN KEY ([data_zakonczenia]) REFERENCES W_data([id]),
    CONSTRAINT [FK_F_pracownik_w_projekcie_W_smieci_tempo] FOREIGN KEY ([tempo_pracy_smieci_id]) REFERENCES W_smieci([id])
)
