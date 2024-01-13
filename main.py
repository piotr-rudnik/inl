from collections import defaultdict

from pandas import DataFrame

from base import CHARS
from datasets import get_df_train_in, get_df_train_expected, get_train_df
import re

from model import calculate_average_word_gap, count_punctuation_around_words_for_chars


# ok
def model_show_probs(text: str):

    df_train: DataFrame = get_train_df()
    avg_word_gap = calculate_average_word_gap(df_train, "with", ".")
    count_around = count_punctuation_around_words_for_chars(df_train, "with", CHARS)

    # for i, word in enumerate(text.split()):
    #     print(f"Word {i}: {word}")
    #     for c in CHARS:
    #         try:
    #             print(f"Char: {c}", count_around[c][word])
    #         except:
    #             print(f"Char: {c}", 0)

    for c in [".", ","]:
        print("Probabilities for char: ", c)
        words = text.split()
        for i, word in enumerate(words):

            next_word = words[i + 1] if i + 1 < len(words) else None

            try:
                before = count_around[c][next_word]['before_chance'] / 2
            except:
                before = 0

            try:
                after = count_around[c][word]['after_chance'] / 2
            except:
                after = 0

            sum = before + after

            force_skip_dot__before = word in ["i", "oraz", "ale", "jednak", "więc", "dlatego", "czyli", "albo", "ani", "lecz", "ponieważ", "natomiast", "chociaż", "gdyż"]
            force_skip_dot_after = next_word in ["który", "która", "które", "którzy", "których", "którym", "co", "czego", "czemu", "kim", "kto", "kogo", "komu"]

            if (before > 0.4 or after > 0.4) or ():
                print(f"{word} '{before:.2f}|{after:.2f}' ", end="")
            else:
                print(f"{word} ", end="")
        print()


if __name__ == '__main__':
    df_test: DataFrame = get_df_train_expected()

    model_show_probs("w meczu o trzecie miejsce turnieju finałowego ligi światowej polska przegrała z kubą 2 3 pierwszy set zaczął się spokojnie każdy zespół starał się rozpoznać taktykę rywala na obydwie przerwy techniczne z przewagą dwóch punktów schodzili polacy zdobyli oni kilka punktów kiwką kubańczycy zaś konsekwentnie serwowali na gruszkę który nie umiał sobie poradzić z ich serwisami pod koniec seta podobieczki garsii zyskali przewagę dwóch punktów i utrzymalą ją do ostatniej piłki druga część meczu rozpoczęła się od czteropunktowej przewagi biało czerwonych pierwsza przerwa techniczna zakończyła się rezultatem 8 5 dla polaków kubańczycy nie zdołali odrobić 3 punktów przewagi i dotrwała ona w takim sam stanie do końca setu w trzecim secie było widać obydwa zespoły zdobywały punkty seriami na początku kuba prowadziła 5 1 po to by zejść na przerwę techniczną z jednym punktem straty seryjna wymiana trwała przez cały mecz w końcówce piłkę setową wykorzystał dawid murek zdobywając asa serwisowego gra polaków w czwartym secie nie mogła zachwycać byli wyraźnie zmęczeni i znużeni grą nie potrafili kończyć dobrze wybronionych piłek czego efektem było wyraźne odskoczenie kubańczyków w końcówce czwartej części meczu popełnili serię błędów kuba była bezlitosna i wykorzystywała każde potknięcie polskiej drużyny zwycięstwo przypieczętowali asem serwisowym tie break rozpoczął się od dwóch znakomitych zagrywek grzegorza szymańskiego potem cztery punkty z rzędu zdobyli kubańczycy głównie za sprawą trudnych serwisów juantoreny przy stanie 5 4 arkadiusz gołaś minimalnie nie trafił przy serwisie w plac gry dalej nie było dla poslkich graczy lepiej zmienili połowę tracąc do rywala trzy punkty pomimo tego że zmniejszyli przewagę a nawet udało im się wyrównać pewni siebie kubańczycy nie odpuścili i szybko zakończyli spotkanie zdobywając dwa punkty zwycięska drużyna zainkasowała 280 tysięcy dolarów podopieczni raula lozano zaś wzbogacili się o 150 tysięcy dolarów")
    # model_show_probs("trwa hossa na światowych giełdach na nowojorskiej giełdzie papierów wartościowych w wtorek 17 lipca najstarszy indeks giełdowy dow jones industrial average ustanowił nowy rekord w histori")
    # model_show_probs("w krakowskim szpitalu przy ul skawińskiej w wieku 74 lat zmarł profesor andrzej szczeklik wybitny lekarz i naukowiec kierownik ii katedry chorób wewnętrznych collegium medicum uniwersytetu jagiellońskiego odznaczony krzyżem komandorskim z gwiazdą orderu odrodzenia polski oraz orderem ecce homo szczeklik zmarł po krótkiej chorobie przyczyną zgonu był zawał serca połączony z zapaleniem płuc andrzej szczeklik był autorem i współautorem ok 600 prac naukowych publikowanych w czasopismach międzynarodowych i krajowych wydał również kilka monografii i podręczników także za granicą autor książek katharsis o uzdrowicielskiej mocy nauki i sztuki oraz kore o chorych chorobach i poszukiwaniu duszy medycyny przetłumaczonych na język angielski niemiecki hiszpański węgierski i litewski był członkiem papieskiej akademii nauk pau pan oraz innych towarzystw naukowych był żonaty miał dwóch synów i córkę do jego najważniejszych osiągnięć zawodowych można zaliczyć badania chorób serca rozwijających się na podłożu miażdżycy i chorób płuc o podłożu immunologicznym w 1976 roku opisał działanie prostacykliny na ustrój ludzki i wprowadził ją do leczenia chorób tętnic w 1997 roku otrzymał wraz z doktorem markiem sanakiem i nagrodę czasopisma lancet za odkrycie podłoża genetycznego astmy oskrzelowej rok później royal college of physicians w londynie wyróżniło go nagrodą specjalną i przyjęło w poczet swoich członków")

    # for c in CHARS:
    #     count = calculate_average_word_gap(df_test, "text", c)
    #     print(f"'{c}': {count}")
        # a = count_punctuation_around_words(df_test, "text", ".")
        # b = filter_words_by_count(a)
        # print(b)

