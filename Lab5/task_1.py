import justpy as jp

def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(
        a = wp, text = "Analiza ocen kursów", classes = "text-h3 text-center q-pa-md"
    )

    p1 = jp.QDiv(
        a = wp, text = "Poszczególne wykresy z analizą kursów", classes = "text-h4"
    )
    return wp

jp.justpy(app)