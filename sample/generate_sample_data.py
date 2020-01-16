#!/usr/bin/env python3

import datetime
import random


# Generic generators

IMIONA = (
    'Adam',
    'Adrianna',
    'Bartek',
    'Basia',
    'Cezary',
    'Cecylia',
    'Damian',
    'Daria',
    'Dagmara',
    'Ernest',
    'Emilia',
    'Franek',
    'Francja',
    'Grzesiek',
    'Grażyna',
    'Kacper',
    'Marek',
    'Zbyszek',
    'Zuzanna',
)

NAZWISKA = (
    'Adamowicz',
    'Bem',
    'Cerkask+',
    'Dworsk+',
    'Testowsk+',
    'Kleczewsk+',
    'Mareck+',
    'Kowalsk+',
    'Iwanienko',
)

def imie_nazwisko():
    imie = random.choice(IMIONA)
    nazwisko = random.choice(NAZWISKA)

    if nazwisko[-1] == '+':
        nazwisko = nazwisko[:-1] + ('a' if imie[-1] == 'a' else 'i')

    return '{} {}'.format(imie, nazwisko)

def pesel():
    y = random.randint(70, 100)
    m = (lambda x: ('0{}' if x < 10 else '{}').format(x))(random.randint(1, 13))
    d = (lambda x: ('0{}' if x < 10 else '{}').format(x))(random.randint(1, 32))
    filler = random.randint(10000, 100000)
    return '{}{}{}{}'.format(y, m, d, filler)

# Table generators
def inhibit_emission(values):
    return values[0] == "()"


def F_pracownik_w_projekcie(pracownik, projekt, klient, all_dates):
    insert_statement = "INSERT INTO F_pracownik_w_projekcie values\n  {}\n;"

    all_projekts = set(map(lambda x: x['id'], projekt))
    matched_projekts = set()
    projekts_for = {}

    values = []
    for each in pracownik:
        prs = set()

        for _ in range(random.randint(2, 6)):
            pr = random.choice(projekt)
            matched_projekts.add(pr['id'])
            if pr['id'] in prs:
                continue
            prs.add(pr['id'])

            pr_begin = all_dates[pr['data_rozpoczecia'] - 1][2]
            pr_end = all_dates[pr['data_zakonczenia'] - 1][2]

            valid_dates = list(filter(
                lambda each: (each[2] >= pr_begin and each[2] <= pr_end),
                all_dates,
            ))
            if len(valid_dates) < 2:
                print(len(valid_dates))
                print(pr, pr_begin, pr_end)
                continue

            pr_pr_begin = random.choice(valid_dates[: (len(valid_dates)//2)])
            pr_pr_end = random.choice(valid_dates[(len(valid_dates)//2) :])
            czas_trwania = (pr_pr_end[2] - pr_pr_begin[2]).days

            values_line = (
                "({czas_trwania}, {pracownik_id}, {projekt_id}, {smieci_id}"
                ", {klient_id}, {etap}, {data_rozpoczecia}, {data_zakonczenia}"
                ", {tempo_pracy}, {uzyskany_dochod}"
                ")"
            ).format(
                czas_trwania = czas_trwania,
                pracownik_id = each['id'],
                projekt_id = pr['id'],
                smieci_id = 2,  # FIXME Niech nikt nie odchodzi. Zapewnienie spójności
                                # między datami odejścia w różnych projektach byłoby
                                # okrutnie czasochłonne.
                klient_id = random.choice(klient)['id'],
                etap = repr(random.choice(('projektowanie', 'prototyp', 'implementacja',))),
                data_rozpoczecia = pr_pr_begin[0],
                data_zakonczenia = pr_pr_end[0],
                tempo_pracy = repr(random.choice(('niskie', 'średnie', 'wysokie',))),
                uzyskany_dochod = random.randint(100_000, 10_000_000),
            )
            values.append(values_line)

    for each in sorted(all_projekts - matched_projekts):
        pr = list(filter(lambda x: x['id'] == each, projekt))[0]
        each = random.choice(pracownik)

        pr_begin = all_dates[pr['data_rozpoczecia'] - 1][2]
        pr_end = all_dates[pr['data_zakonczenia'] - 1][2]

        valid_dates = list(filter(
            lambda each: (each[2] >= pr_begin and each[2] <= pr_end),
            all_dates,
        ))
        if len(valid_dates) < 2:
            print(len(valid_dates))
            print(pr, pr_begin, pr_end)
            continue

        pr_pr_begin = random.choice(valid_dates[: (len(valid_dates)//2)])
        pr_pr_end = random.choice(valid_dates[(len(valid_dates)//2) :])
        czas_trwania = (pr_pr_end[2] - pr_pr_begin[2]).days

        values_line = (
            "({czas_trwania}, {pracownik_id}, {projekt_id}, {smieci_id}"
            ", {klient_id}, {etap}, {data_rozpoczecia}, {data_zakonczenia}"
            ", {tempo_pracy}, {uzyskany_dochod}"
            ")"
        ).format(
            czas_trwania = czas_trwania,
            pracownik_id = each['id'],
            projekt_id = pr['id'],
            smieci_id = 2,  # FIXME Niech nikt nie odchodzi. Zapewnienie spójności
                            # między datami odejścia w różnych projektach byłoby
                            # okrutnie czasochłonne.
            klient_id = random.choice(klient)['id'],
            etap = repr(random.choice(('projektowanie', 'prototyp', 'implementacja',))),
            data_rozpoczecia = pr_pr_begin[0],
            data_zakonczenia = pr_pr_end[0],
            tempo_pracy = repr(random.choice(('niskie', 'średnie', 'wysokie',))),
            uzyskany_dochod = random.randint(100_000, 10_000_000),
        )
        values.append(values_line)

    if inhibit_emission(values): return
    print(insert_statement.format("\n, ".join(values)))

    return values

def F_technologie_pracownika(pracownik_no, technologia_no):
    insert_statement = "INSERT INTO F_technologie_pracownika values\n  {}\n;"

    values = []
    for i in range(1, pracownik_no + 1):
        techs = random.sample(range(1, technologia_no + 1), random.randint(2, 5))
        for t in techs:
            values_line = "({pracownik_id}, {technologia_id})".format(
                pracownik_id = i,
                technologia_id = t,
            )
            values.append(values_line)

    if inhibit_emission(values): return
    print(insert_statement.format("\n, ".join(values)))

    return values

def W_data(): # done
    insert_statement = "INSERT INTO W_data values\n  {}\n;"

    PORA_ROKU = {
        0: 'wiosna',
        1: 'lato',
        2: 'jesień',
        3: 'zima',
    }
    MIESIACE = {
        0: { 3: 'marzec', 4: 'kwiecień', 5: 'maj', }, # wiosna
        1: { 6: 'czerwiec', 7: 'lipiec', 8: 'sierpień', }, # lato
        2: { 9: 'wrzesień', 10: 'październik', 11: 'listopad', }, # jesień
        3: { 12: 'grudzień', 1: 'styczeń', 2: 'luty', }, # zima
    }
    REV_MIESIACE_PORA_ROKU = {
         1: 3,
         2: 3,
         3: 0,
         4: 0,
         5: 0,
         6: 1,
         7: 1,
         8: 1,
         9: 2,
        10: 2,
        11: 2,
        12: 3,
    }
    DNI = {
         1: 31,
         2: 28,
         3: 31,
         4: 30,
         5: 31,
         6: 30,
         7: 31,
         8: 31,
         9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    raw_values = []

    lower_dates = []
    N = 20
    for i in range(1, N + 1):
        y = random.randint(2014, 2017)

        p = random.randint(0, 3)
        pp = PORA_ROKU[p]

        m = random.choice(list(MIESIACE[p].keys()))
        mp = MIESIACE[p][m]

        d = random.randint(1, DNI[m])

        dt = datetime.datetime.strptime(
            '{}-{}-{}'.format(y, m, d),
            '%Y-%m-%d',
        )
        values_line = "({rok}, {pora_roku}, {miesiac}, {dzien})".format(
            rok = y,
            pora_roku = repr(pp),
            miesiac = repr(mp),
            dzien = d,
        )
        lower_dates.append((i, values_line, dt))
        raw_values.append(lower_dates[-1])

    upper_dates = []
    M = (N + 1 + (N // 2))
    for i in range(N + 1, M):
        y = random.randint(2018, 2019)

        p = random.randint(0, 3)
        pp = PORA_ROKU[p]

        m = random.choice(list(MIESIACE[p].keys()))
        mp = MIESIACE[p][m]

        d = random.randint(1, DNI[m])

        dt = datetime.datetime.strptime(
            '{}-{}-{}'.format(y, m, d),
            '%Y-%m-%d',
        )
        values_line = "({rok}, {pora_roku}, {miesiac}, {dzien})".format(
            rok = y,
            pora_roku = repr(pp),
            miesiac = repr(mp),
            dzien = d,
        )
        upper_dates.append((i, values_line, dt))
        raw_values.append(upper_dates[-1])

    values = []
    values.extend(lower_dates)
    values.extend(upper_dates)

    if inhibit_emission(values): return

    only_dates = set(map(lambda x: x[2], values))
    min_date = min(only_dates)
    max_date = max(only_dates)

    days_apart = (max_date - min_date)
    for i in range(M + 1, ((M + 1) + (days_apart.days + 1))):
        days_since = datetime.timedelta(days = i)
        dt = (min_date + days_since)
        if dt not in only_dates:
            p = REV_MIESIACE_PORA_ROKU[dt.month]
            pp = PORA_ROKU[p]
            mp = MIESIACE[p][dt.month]
            values_line = "({rok}, {pora_roku}, {miesiac}, {dzien})".format(
                rok = dt.year,
                pora_roku = repr(pp),
                miesiac = repr(mp),
                dzien = dt.day,
            )
            values.append((i + 1, values_line, dt))
            raw_values.append((i + 1, values_line, dt))

    print(insert_statement.format("\n, ".join(map(lambda x: x[1], values))))

    return lower_dates, upper_dates, raw_values

def W_klient(): # done
    insert_statement = "INSERT INTO W_klient values\n  {}\n;"

    A = (
        'Turbo',
        'Super',
        'Best',
        'Most',
        None,
        None,
        None,
    )
    B = (
        'Szym',
        'Ziom',
        'Mur',
        'Pol',
        'Beton',
        'Cement',
        'Kop',
        'Mosto',
        'Rud',
    )
    C = (
        'bud',
        'ex',
        'ix'
        'stal',
        'most',
        'szyb',
    )
    D = (
        ', Inc.',
        ' Sp. z. o.o.',
        ' Sp.j. sp.k.',
        ' Sp.j.',
        ' S.A.',
        None,
        None,
    )

    BRANZA = (
        'entertainment',
        'film',
        'music production',
        'construction',
        'farming',
        'it',
        'public sector',
        'defence',
        'military',
        'turism',
        'engineering',
        'mining',
    )

    def nazwa():
        a = random.choice(A)
        b = random.choice(B)
        c = random.choice(C)
        d = random.choice(D)

        n = '{}{}'.format(b, c)
        if a is not None:
            n = '{}-{}'.format(a, n)
        if d is not None:
            n = '{}{}'.format(n, d)

        return n

    raw_values = []
    values = []
    N = 30
    for i in range(1, N + 1):
        raw_values.append({
            'id': i,
            'nazwa': repr(nazwa()),
            'branza': repr(random.choice(BRANZA)),
        })
        values_line = "({nazwa}, {branza})"
        values.append(values_line.format(**raw_values[-1]))

    if inhibit_emission(values): return
    print(insert_statement.format("\n, ".join(values)))

    return raw_values

def W_pracownik(): # done
    insert_statement = "INSERT INTO W_pracownik values\n  {}\n;"

    raw_values = []
    values = []
    N = 10
    for i in range(1, N + 1):
        raw_values.append({
            'id': i,
            'imie_nazwisko': repr(imie_nazwisko()),
            'pesel': pesel(),
            'doswiadczenie': repr(random.choice(('junior', 'regular', 'senior',))),
            'wynagrodzenie': repr(random.choice(('niskie', 'srednie', 'wysokie',))),
            'szef_id': 1,  # nieistorne, bo nie pojawia się w pytaniach
        })
        values_line = '({imie_nazwisko}, {pesel}, {doswiadczenie}, {wynagrodzenie}, {szef_id})'
        values.append(values_line.format(**raw_values[-1]))

    if inhibit_emission(values): return
    print(insert_statement.format("\n, ".join(values)))

    return raw_values

def W_projekt(lower_dates, upper_dates): # done
    insert_statement = "INSERT INTO W_projekt values\n  {}\n;"

    STARTUP_TEMPLATE = (
        'Uber for {}',
        'Super {}',
        'Space {}',
        '{} X',
        'Turbo {}',
        '{} 3000',
        'New-Generation {}',
        '{} Reimagined',
        'Redesigned {}',
        '{} XL',
        'Awesome {}',
        '{} of the future',
        '{} of tomorrow',
    )
    WHAT_FOR = (
        'Food',
        'Hamsters',
        'Data Warehsouses',
        'Pascal',
        'Kelvin',
        'Watt',
        'University',
        'Academia',
        'Industry',
        'Mining',
        'Gaming',
        'Musical',
        'Men',
        'Women',
        'Children',
        'Animals',
        'Shrews',
        'Pirates',
        'Tools',
        'Sharks',
        'Tornados',
        'Water',
    )
    def nazwa():
        return random.choice(STARTUP_TEMPLATE).format(random.choice(WHAT_FOR))

    raw_values = []
    values = []
    for i in range(1, 41):
        data_rozpoczecia = random.choice(lower_dates)
        data_zakonczenia = random.choice(list(filter(
            lambda each: each[2] > data_rozpoczecia[2],
            lower_dates + upper_dates,
        )))
        if data_rozpoczecia[2] >= data_zakonczenia[2]:
            print(data_rozpoczecia, data_zakonczenia)
            print('FUCKUP')
            exit(127)

        raw_values.append({
            'id': i,
            'nazwa': repr(nazwa()),
            'tempo_realizacji': repr(random.choice(('przed czasem', 'o czasie', 'po czasie',))),
            'liczba_pracownikow': repr(random.choice(('mała', 'średnia', 'duża',))),
            'czas_trwania': (data_zakonczenia[2] - data_rozpoczecia[2]).days,
            'data_rozpoczecia': data_rozpoczecia[0],
            'data_zakonczenia': data_zakonczenia[0],
        })
        values_line = (
            "({nazwa}, {tempo_realizacji}, {liczba_pracownikow}, {czas_trwania}"
            ", {data_rozpoczecia}, {data_zakonczenia}) -- {dt_b} - {dt_e}"
        )
        values.append(values_line.format(
            dt_b = data_rozpoczecia[2],
            dt_e = data_zakonczenia[2],
            **raw_values[-1]
        ))

    if inhibit_emission(values): return
    print(insert_statement.format("\n, ".join(values)))

    return raw_values

def W_smieci(): # done
    insert_statement = "INSERT INTO W_smieci values\n  {}\n;"

    values = ["('tak')", "('nie')",]

    if inhibit_emission(values): return
    print(insert_statement.format("\n, ".join(values)))

    return values

def W_technologia(): # done
    insert_statement = "INSERT INTO W_technologia values\n  {}\n;"

    class Category:
        Programming_language = 'programming language'
        DSL = 'domain-specific language'
        API = 'API'
        Framework = 'framework'
        Game_engine = 'game engine'

    values = [
        (Category.Programming_language, 'x86 assembly', '',),
        (Category.Programming_language, 'amd64 assembly', ''),
        (Category.Programming_language, 'C++98', ''),
        (Category.Programming_language, 'C++11', ''),
        (Category.Programming_language, 'C++14', ''),
        (Category.Programming_language, 'C++17', ''),
        (Category.Programming_language, 'C89', ''),
        (Category.Programming_language, 'C11', ''),
        (Category.Programming_language, 'Python 2', ''),
        (Category.Programming_language, 'Python 3', '3.4'),
        (Category.Programming_language, 'Python 3', '3.5'),
        (Category.Programming_language, 'Python 3', '3.6'),
        (Category.Programming_language, 'JavaScript', ''),
        (Category.Programming_language, 'ECMAScript', ''),
        (Category.Programming_language, 'Java', ''),
        (Category.Programming_language, 'FORTRAN', ''),
        (Category.Programming_language, 'COBOL', ''),
        (Category.Programming_language, 'Ada', ''),
        (Category.Programming_language, 'Turbo Pascal', ''),
        (Category.Programming_language, 'OCaml', ''),
        (Category.Programming_language, 'Erlang', ''),
        (Category.Programming_language, 'Elixir', ''),
        (Category.DSL, 'HTML 5', ''),
        (Category.API, 'OpenGL', ''),
        (Category.API, 'Vulkan', ''),
        (Category.API, 'WebGL', ''),
        (Category.Framework, 'Angular', '1.6'),
        (Category.Framework, 'Angular', '2'),
        (Category.Framework, 'Angular', '8'),
        (Category.Framework, 'Ember', ''),
        (Category.Framework, 'Backbone.js', ''),
        (Category.Framework, 'Django', '1.7'),
        (Category.Game_engine, 'Unity', ''),
        (Category.Game_engine, 'Unreal', ''),
        (Category.Game_engine, 'OpenMW', ''),
    ]
    values = [
        '({typ}, {nazwa}, {wersja})'.format(
            typ = repr(each[0]),
            nazwa = repr(each[1]),
            wersja = repr(each[2]),
        )
        for each
        in values
    ]

    if inhibit_emission(values): return
    print(insert_statement.format("\n, ".join(values)))

    return values



# Main function

def main():
    lower_dates, upper_dates, raw_dates = W_data()
    klient = W_klient()
    pracownik = W_pracownik()
    projekt = W_projekt(lower_dates, upper_dates)
    W_smieci()
    technologia = W_technologia()

    F_technologie_pracownika(len(pracownik), len(technologia))
    F_pracownik_w_projekcie(pracownik, projekt, klient, raw_dates)


if __name__ == "__main__":
    main()
