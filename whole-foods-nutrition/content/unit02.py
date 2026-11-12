"""Unit 2 — Math in the Kitchen (Days 5-9, 2 labs).

Cert alignment: S3.5 (increase and decrease recipes by yield), S3.2 (measuring tools), S3.4 (resource management).
Spanish text is machine-assisted and has NOT had a fluent human review (see README).
"""
from .common import T

UNIT = {
    "number": 2,
    "slug": "math-in-the-kitchen",
    "title": T("Math in the Kitchen", "Matemáticas en la cocina"),
    "days": "5-9",
    "labs": 2,
    "cert": ["S3.5", "S3.2", "S3.4"],
    "essential_question": T(
        "How do cooks use math to get the same good result every time, for two people or for two hundred?",
        "¿Cómo usan los cocineros las matemáticas para obtener el mismo buen resultado cada vez, para dos personas o para doscientas?"),
    "overview": T(
        "Recipes are math. In this unit you will measure dry and liquid ingredients accurately, convert between "
        "units, work with fractions, and increase or decrease a recipe to match the number of servings you need. "
        "You will practice in two labs, and the second one is a performance task for the certification: you scale "
        "a recipe for your group and then cook it.",
        "Las recetas son matemáticas. En esta unidad medirás con exactitud ingredientes secos y líquidos, "
        "convertirás entre unidades, trabajarás con fracciones y aumentarás o disminuirás una receta para que "
        "coincida con el número de porciones que necesitas. Practicarás en dos laboratorios, y el segundo es una "
        "tarea de desempeño para la certificación: escalas una receta para tu grupo y luego la cocinas."),

    "vocab_bank": [
        {"term": T("Volume", "Volumen"),
         "definition": T("The amount of space an ingredient takes up, measured in cups, spoons, or fluid ounces.",
                         "La cantidad de espacio que ocupa un ingrediente, medida en tazas, cucharas u onzas líquidas.")},
        {"term": T("Level", "Nivelar"),
         "definition": T("To scrape the top of a measure flat with a straight edge so it holds the exact amount.",
                         "Rasar la parte superior de una medida con un borde recto para que contenga la cantidad exacta.")},
        {"term": T("Meniscus", "Menisco"),
         "definition": T("The curved surface of a liquid in a measuring cup. Read the bottom of the curve.",
                         "La superficie curva de un líquido en una taza medidora. Lee la parte inferior de la curva.")},
        {"term": T("Equivalent", "Equivalente"),
         "definition": T("A different measurement that means the same amount, such as 3 teaspoons and 1 tablespoon.",
                         "Una medida distinta que significa la misma cantidad, como 3 cucharaditas y 1 cucharada.")},
        {"term": T("Yield", "Rendimiento"),
         "definition": T("The total amount of food or number of servings a recipe makes.",
                         "La cantidad total de comida o el número de porciones que produce una receta.")},
        {"term": T("Conversion factor", "Factor de conversión"),
         "definition": T("The number you multiply every ingredient by to change a recipe's yield: wanted servings divided by original servings.",
                         "El número por el que multiplicas cada ingrediente para cambiar el rendimiento de una receta: porciones deseadas divididas entre porciones originales.")},
        {"term": T("Serving", "Porción"),
         "definition": T("One portion of food, the amount one person is expected to eat.",
                         "Una cantidad de comida, lo que se espera que coma una persona.")},
        {"term": T("Abbreviation", "Abreviatura"),
         "definition": T("A short form used in recipes: tsp (teaspoon), Tbsp (tablespoon), c (cup), oz (ounce), lb (pound).",
                         "Una forma corta usada en las recetas: cdta (cucharadita), cda (cucharada), t (taza), oz (onza), lb (libra).")},
    ],

    "reading": {
        "title": T("Why Cooks Measure", "Por qué los cocineros miden"),
        "body": [
            T("When you cook at home, you may toss in a little of this and a little of that. In a school kitchen, a restaurant, "
              "or a food factory, that does not work. A recipe must come out the same every time, no matter who makes it. "
              "Measuring makes that possible.",
              "Cuando cocinas en casa, tal vez eches un poco de esto y un poco de aquello. En una cocina escolar, un restaurante "
              "o una fábrica de alimentos, eso no funciona. Una receta debe salir igual cada vez, sin importar quién la prepare. "
              "Medir lo hace posible."),
            T("Even careful measuring can go wrong. If you scoop flour straight from the bag, it packs down into the cup, and you can "
              "end up with 20 percent more flour or even more than the recipe expects. The cake turns out dry and heavy. If you "
              "spoon flour into the cup and level it off, you get a result much closer to the recipe. Professional bakers often "
              "weigh ingredients on a scale because weight is more consistent than volume.",
              "Incluso medir con cuidado puede salir mal. Si sacas la harina directamente de la bolsa con la taza, se compacta y "
              "puedes terminar con un 20 por ciento más de harina, o incluso más, de lo que pide la receta. El pastel queda seco y "
              "pesado. Si pones la harina en la taza con una cuchara y la nivelas, obtienes un resultado mucho más cercano al de "
              "la receta. Los panaderos profesionales suelen pesar los ingredientes en una báscula porque el peso es más "
              "constante que el volumen."),
            T("Math also lets a cook change a recipe. A recipe for four people can be doubled for eight or cut in half for two. "
              "You multiply or divide every ingredient by the same number. A school cafeteria might scale a recipe from 8 servings "
              "to 800. Getting the math wrong wastes food and money, or leaves people hungry.",
              "Las matemáticas también permiten a un cocinero cambiar una receta. Una receta para cuatro personas puede duplicarse "
              "para ocho o reducirse a la mitad para dos. Se multiplica o divide cada ingrediente por el mismo número. Una cafetería "
              "escolar podría escalar una receta de 8 porciones a 800. Equivocarse en las matemáticas desperdicia comida y dinero, "
              "o deja a las personas con hambre."),
            T("Not everything scales perfectly. Cooking time, pan size, and the amount of salt or spice may need to be adjusted when "
              "you change a recipe a lot. Good cooks scale the math first, then use tasting and judgment, and they write down "
              "what worked so they can repeat it.",
              "No todo escala perfectamente. El tiempo de cocción, el tamaño de la sartén y la cantidad de sal o especias pueden "
              "necesitar ajustes cuando cambias mucho una receta. Los buenos cocineros primero escalan las matemáticas, luego usan "
              "el gusto y el criterio, y anotan lo que funcionó para poder repetirlo."),
        ],
        "questions": [
            {"q": T("Why does a recipe need exact measurements in a school kitchen?",
                    "¿Por qué una receta necesita medidas exactas en una cocina escolar?"),
             "answer": T("So it comes out the same every time, no matter who makes it.",
                         "Para que salga igual cada vez, sin importar quién la prepare.")},
            {"q": T("What happens if you scoop flour straight from the bag?",
                    "¿Qué pasa si sacas la harina directamente de la bolsa con la taza?"),
             "answer": T("It packs down and you use too much flour.", "Se compacta y usas demasiada harina.")},
            {"q": T("How do you change a recipe from 4 servings to 8?",
                    "¿Cómo cambias una receta de 4 porciones a 8?"),
             "answer": T("Multiply every ingredient by 2.", "Multiplica cada ingrediente por 2.")},
            {"q": T("Name two things that may need adjusting when a recipe changes a lot.",
                    "Nombra dos cosas que pueden necesitar ajustes cuando una receta cambia mucho."),
             "answer": T("Any two: cooking time, pan size, salt or spice.", "Dos cualesquiera: tiempo de cocción, tamaño de la sartén, sal o especias.")},
        ],
        "source_note": "Flour compaction varies by method; the 20 percent figure is a commonly cited estimate, so the text says 'can'.",
    },

    "lessons": [
        # ------------------------------------------------------------------ DAY 5
        {
            "day": 5, "kind": "lesson",
            "title": T("Measuring Tools and Techniques", "Herramientas y técnicas de medición"),
            "objectives": [T("I can choose the right measuring tool for dry and liquid ingredients.",
                             "Puedo elegir la herramienta de medición correcta para ingredientes secos y líquidos."),
                           T("I can measure accurately by leveling and by reading at eye level.",
                             "Puedo medir con exactitud nivelando y leyendo a la altura de los ojos."),
                           T("I can read recipe abbreviations.", "Puedo leer las abreviaturas de las recetas.")],
            "cert": ["S3.2", "S3.5"],
            "vocab": ["Volume", "Level", "Meniscus", "Abbreviation"],
            "bellringer": T("How much does a cup of flour weigh? Make a prediction. Then write how you could find out.",
                            "¿Cuánto pesa una taza de harina? Haz una predicción. Luego escribe cómo podrías averiguarlo."),
            "instruction": [
                {"heading": T("Dry and liquid measures are different tools", "Las medidas secas y líquidas son herramientas distintas"),
                 "body": T("Dry measuring cups are made to be filled to the top and leveled. Liquid measuring cups have a spout and a line below "
                           "the rim, so liquid can be poured without spilling. Using the wrong one gives a wrong amount.",
                           "Las tazas medidoras secas se llenan hasta el borde y se nivelan. Las tazas medidoras líquidas tienen pico y una "
                           "línea debajo del borde para verter sin derramar. Usar la equivocada da una cantidad incorrecta.")},
                {"heading": T("How to measure dry ingredients", "Cómo medir ingredientes secos"),
                 "body": T("Spoon flour or powder into the cup until it is heaping, then slide the back of a knife across the top to level it. "
                           "Do not tap or press it down. Pack brown sugar firmly into the cup. For spoons, fill and level the same way.",
                           "Pon la harina o el polvo con una cuchara en la taza hasta que sobresalga, luego pasa el dorso de un cuchillo por "
                           "encima para nivelarla. No la golpees ni la presiones. Compacta el azúcar morena firmemente en la taza. Con las "
                           "cucharas, llena y nivela de la misma manera.")},
                {"heading": T("How to measure liquids", "Cómo medir líquidos"),
                 "body": T("Set the liquid measuring cup on a flat counter. Pour to the line, then bend down so your eyes are level with the "
                           "line. Read the bottom of the curved surface, called the meniscus.",
                           "Coloca la taza medidora líquida sobre un mostrador plano. Vierte hasta la línea y agáchate para que tus ojos queden "
                           "a la altura de la línea. Lee la parte inferior de la superficie curva, llamada menisco.")},
                {"heading": T("Recipe abbreviations", "Abreviaturas de las recetas"),
                 "body": T("tsp means teaspoon. Tbsp means tablespoon. c means cup. oz means ounce. lb means pound. A capital T usually means "
                           "tablespoon and a small t means teaspoon, so always read carefully.",
                           "tsp significa cucharadita. Tbsp significa cucharada. c significa taza. oz significa onza. lb significa libra. "
                           "Una T mayúscula suele significar cucharada y una t minúscula significa cucharadita, así que lee siempre con cuidado.")},
            ],
            "guided": {
                "title": T("Scoop vs. Spoon Experiment", "Experimento: sacar con la taza vs. con la cuchara"),
                "steps": [T("Your teacher weighs one cup of flour scooped directly from the container. Record the weight in grams.",
                            "Tu maestra pesa una taza de harina sacada directamente del recipiente. Anota el peso en gramos."),
                          T("Your teacher weighs one cup of flour spooned into the cup and leveled. Record the weight.",
                            "Tu maestra pesa una taza de harina puesta con cuchara y nivelada. Anota el peso."),
                          T("Calculate the difference. What percent more flour was in the scooped cup?",
                            "Calcula la diferencia. ¿Qué porcentaje más de harina había en la taza sacada directamente?")],
            },
            "independent": {
                "kind": "activity",
                "title": T("Measuring Station Rotation", "Rotación por estaciones de medición"),
                "steps": [T("Visit four stations: dry cup, liquid cup, spoons, and kitchen scale. At each one, measure the amount on the card.",
                            "Visita cuatro estaciones: taza seca, taza líquida, cucharas y báscula de cocina. En cada una, mide la cantidad de la tarjeta."),
                          T("Have a partner check your measure and sign the card.", "Pide a un compañero que revise tu medida y firme la tarjeta."),
                          T("Match each abbreviation to its meaning on the abbreviation sheet.",
                            "Relaciona cada abreviatura con su significado en la hoja de abreviaturas.")],
            },
            "exit": [{"q": T("Which tool measures flour: a dry cup or a liquid cup? How do you measure it correctly?",
                             "¿Qué herramienta mide la harina: una taza seca o una líquida? ¿Cómo se mide correctamente?"),
                      "answer": T("A dry cup. Spoon it in and level it off.", "Una taza seca. Se pone con cuchara y se nivela.")},
                     {"q": T("What does Tbsp stand for?", "¿Qué significa Tbsp?"), "answer": T("Tablespoon.", "Cucharada.")}],
            "teacher": {
                "materials": ["Dry and liquid measuring cups", "Measuring spoons", "Kitchen scale (grams)", "Flour (about 1 lb for demo)",
                              "Station cards with amounts", "Abbreviation sheet"],
                "notes": ["Typical result: a scooped cup of flour weighs noticeably more than a spooned and leveled cup. Use your own scale readings; "
                          "do not tell students a fixed number.",
                          "Water, rice, or dried beans can substitute for flour at stations to save cost.",
                          "Egg allergy: not used today. Wheat allergy: use rice for the flour demo."],
            },
        },
        # ------------------------------------------------------------------ DAY 6
        {
            "day": 6, "kind": "lesson",
            "title": T("Equivalents, Fractions, and Conversions", "Equivalentes, fracciones y conversiones"),
            "objectives": [T("I can convert between common kitchen units.", "Puedo convertir entre unidades comunes de cocina."),
                           T("I can add and multiply fractions of a cup.", "Puedo sumar y multiplicar fracciones de una taza."),
                           T("I can find a measure that equals half or double an amount.",
                             "Puedo encontrar una medida que sea la mitad o el doble de una cantidad.")],
            "cert": ["S3.5"],
            "vocab": ["Equivalent", "Abbreviation"],
            "bellringer": T("You need 1/4 cup of oil but your only clean measure is a tablespoon. How many tablespoons could you use?",
                            "Necesitas 1/4 de taza de aceite pero tu única medida limpia es una cucharada. ¿Cuántas cucharadas podrías usar?"),
            "instruction": [
                {"heading": T("Common equivalents", "Equivalentes comunes"),
                 "body": T("3 tsp = 1 Tbsp. 4 Tbsp = 1/4 cup. 16 Tbsp = 1 cup. 8 fluid oz = 1 cup. 2 cups = 1 pint. 2 pints = 1 quart. "
                           "4 quarts = 1 gallon. 16 oz = 1 pound.",
                           "3 cdtas = 1 cda. 4 cdas = 1/4 de taza. 16 cdas = 1 taza. 8 onzas líquidas = 1 taza. 2 tazas = 1 pinta. "
                           "2 pintas = 1 cuarto. 4 cuartos = 1 galón. 16 oz = 1 libra.")},
                {"heading": T("Metric in the kitchen", "El sistema métrico en la cocina"),
                 "body": T("Many labels and recipes use metric units. About 5 mL equals 1 teaspoon, 15 mL equals 1 tablespoon, and 240 mL is "
                           "close to 1 cup. About 28 grams equals 1 ounce, and 454 grams equals 1 pound.",
                           "Muchas etiquetas y recetas usan unidades métricas. Aproximadamente 5 mL equivalen a 1 cucharadita, 15 mL a 1 cucharada "
                           "y 240 mL se acercan a 1 taza. Aproximadamente 28 gramos equivalen a 1 onza y 454 gramos a 1 libra.")},
                {"heading": T("Fractions of a cup", "Fracciones de una taza"),
                 "body": T("1/2 cup = 8 Tbsp. 1/3 cup = 5 Tbsp + 1 tsp. 1/4 cup = 4 Tbsp. To add fractions, use a common denominator: "
                           "1/2 + 1/4 = 2/4 + 1/4 = 3/4. To halve a fraction, multiply by 1/2: half of 3/4 is 3/8.",
                           "1/2 taza = 8 cdas. 1/3 de taza = 5 cdas + 1 cdta. 1/4 de taza = 4 cdas. Para sumar fracciones, usa un denominador "
                           "común: 1/2 + 1/4 = 2/4 + 1/4 = 3/4. Para sacar la mitad de una fracción, multiplica por 1/2: la mitad de 3/4 es 3/8.")},
                {"heading": T("Worked example", "Ejemplo resuelto"),
                 "body": T("Half of 3/4 cup is 3/8 cup. There is no 3/8 measuring cup, so convert: 3/4 cup is 12 Tbsp, and half of 12 Tbsp is 6 Tbsp. "
                           "Using the equivalent makes the measuring easy.",
                           "La mitad de 3/4 de taza es 3/8 de taza. No existe una taza medidora de 3/8, así que convierte: 3/4 de taza son 12 cdas, "
                           "y la mitad de 12 cdas es 6 cdas. Usar el equivalente facilita la medición.")},
            ],
            "guided": {
                "title": T("Convert It", "Conviértelo"),
                "steps": [T("As a class, solve: How many teaspoons are in 1/4 cup? (Use 4 Tbsp = 1/4 cup and 3 tsp = 1 Tbsp.)",
                            "Como clase, resuelvan: ¿Cuántas cucharaditas hay en 1/4 de taza? (Usen 4 cdas = 1/4 de taza y 3 cdtas = 1 cda.)"),
                          T("With a partner, solve three more conversions on the practice sheet.",
                            "Con un compañero, resuelve tres conversiones más en la hoja de práctica.")],
            },
            "independent": {
                "kind": "activity",
                "title": T("Fraction and Conversion Practice", "Práctica de fracciones y conversiones"),
                "steps": [T("Complete the conversion chart: fill in the missing equivalents.", "Completa la tabla de conversiones: llena los equivalentes que faltan."),
                          T("Find half of each amount and write it using the measure that is easiest to use.",
                            "Encuentra la mitad de cada cantidad y escríbela con la medida que sea más fácil de usar."),
                          T("Check your work with the answer strip your teacher gives you.", "Revisa tu trabajo con la tira de respuestas que te da tu maestra.")],
            },
            "exit": [{"q": T("How many tablespoons are in 1/4 cup?", "¿Cuántas cucharadas hay en 1/4 de taza?"), "answer": T("4.", "4.")},
                     {"q": T("What is half of 3/4 cup? Write it in tablespoons too.", "¿Cuánto es la mitad de 3/4 de taza? Escríbelo también en cucharadas."),
                      "answer": T("3/8 cup, which is 6 Tbsp.", "3/8 de taza, que son 6 cdas.")}],
            "teacher": {
                "materials": ["Conversion chart handout (with blanks)", "Practice sheet", "Answer strips", "Calculators optional"],
                "notes": ["Metric values are rounded kitchen equivalents (1 cup is exactly 236.6 mL; 240 mL is the common rounding).",
                          "Practice-sheet answers to prepare: 1/4 cup = 12 tsp; 1/2 cup = 8 Tbsp; 1 cup = 48 tsp; 1 pt = 2 cups = 16 fl oz; 1 qt = 4 cups; half of 1/2 cup = 1/4 cup = 4 Tbsp; half of 1 Tbsp = 1 1/2 tsp.",
                          "Struggling students: use the visual fraction strip; allow calculators for the final sheet."],
            },
        },
        # ------------------------------------------------------------------ DAY 7 (LAB)
        {
            "day": 7, "kind": "lab",
            "title": T("Lab 2: Measuring Mix (Snack Mix)", "Laboratorio 2: Mezcla para botanear (medición)"),
            "objectives": [T("I can measure dry ingredients accurately with the correct tools.", "Puedo medir ingredientes secos con exactitud usando las herramientas correctas."),
                           T("I can use equivalents when I do not have the exact measure.", "Puedo usar equivalentes cuando no tengo la medida exacta."),
                           T("I can follow clean, separate, and chill while I work.", "Puedo seguir limpiar, separar y enfriar mientras trabajo.")],
            "cert": ["S3.2", "S3.5", "S3.1"],
            "vocab": ["Level", "Equivalent"],
            "bellringer": T("Read the recipe. Which measures will you use? Circle any amount where you will need an equivalent.",
                            "Lee la receta. ¿Qué medidas usarás? Encierra en un círculo cualquier cantidad en la que necesitarás un equivalente."),
            "instruction": [
                {"heading": T("Lab brief", "Introducción del laboratorio"),
                 "body": T("Today's focus: accurate measuring. Wash hands first. Use dry cups and level them. Your Safety Officer checks that nothing "
                           "touches the counter without being sanitized, and checks every label for peanuts. Weigh one cup of your mix at the end to compare groups.",
                           "Enfoque de hoy: medir con exactitud. Lávate las manos primero. Usa tazas secas y nivélalas. Tu Oficial de seguridad "
                           "verifica que nada toque el mostrador sin desinfectarlo y revisa que cada etiqueta no tenga cacahuate. Al final pesa una taza de tu "
                           "mezcla para comparar entre grupos.")},
            ],
            "guided": {
                "title": T("Group Work Plan", "Plan de trabajo del grupo"),
                "steps": [T("Write who measures which ingredient and the order you will work in.", "Escribe quién mide cada ingrediente y el orden de trabajo."),
                          T("Decide which equivalents you will use and write them next to the recipe amounts.", "Decide qué equivalentes usarás y escríbelos junto a las cantidades de la receta.")],
            },
            "independent": {
                "kind": "lab",
                "recipe": "snackmix",
                "title": T("Cook: Measuring Mix", "Cocinar: Mezcla para botanear"),
                "steps": [T("Follow the recipe card. Your Safety Officer signs off each safety checkpoint.", "Sigue la tarjeta de receta. Tu Oficial de seguridad firma cada punto de control de seguridad."),
                          T("Weigh 1 cup of your finished mix on the scale. Record it, and compare with another group.", "Pesa 1 taza de tu mezcla terminada en la báscula. Anótalo y compáralo con otro grupo."),
                          T("Eat together, then complete cleanup and the station check.", "Coman juntos y luego completen la limpieza y la revisión de la estación.")],
            },
            "exit": [{"q": T("Which equivalent did you use today? Write it as an equation.", "¿Qué equivalente usaste hoy? Escríbelo como una ecuación."),
                      "answer": T("Answers vary, for example 4 Tbsp = 1/4 cup.", "Las respuestas varían, por ejemplo 4 cdas = 1/4 de taza.")},
                     {"q": T("Why might two groups' mix weigh different amounts per cup?", "¿Por qué la mezcla de dos grupos podría pesar cantidades diferentes por taza?"),
                      "answer": T("Different packing and leveling; pieces of different sizes.", "Diferente compactación y nivelación; piezas de distintos tamaños.")}],
            "teacher": {
                "materials": ["Recipe cards", "Ingredients (see recipe)", "Kitchen scale", "Station checklist", "Unit 2 practical rubric"],
                "notes": ["Peanut-free: check cereal, pretzel, and seed labels (shared-equipment warnings).", "Wheat allergy: use a gluten-free cereal and omit pretzels.",
                          "Estimated cost: about $2 per group, $16 for 8 groups. Verify against current prices.", "No heat today, so this is a good first lab for focusing on measurement and station routines."],
            },
        },
        # ------------------------------------------------------------------ DAY 8
        {
            "day": 8, "kind": "lesson",
            "title": T("Scaling Recipes Up and Down", "Escalar recetas hacia arriba y hacia abajo"),
            "objectives": [T("I can find a conversion factor for a new yield.", "Puedo encontrar un factor de conversión para un nuevo rendimiento."),
                           T("I can increase and decrease every ingredient in a recipe.", "Puedo aumentar y disminuir cada ingrediente de una receta."),
                           T("I can explain what does not scale directly.", "Puedo explicar qué no escala directamente.")],
            "cert": ["S3.5", "S3.4"],
            "vocab": ["Yield", "Conversion factor", "Serving"],
            "bellringer": T("A recipe makes 4 servings and you need 12. Without writing anything down, how would you change it?",
                            "Una receta rinde 4 porciones y necesitas 12. Sin escribir nada, ¿cómo la cambiarías?"),
            "instruction": [
                {"heading": T("The conversion factor", "El factor de conversión"),
                 "body": T("Conversion factor = wanted servings divided by original servings. A recipe serves 4 and you need 12: 12 divided by 4 is 3, "
                           "so multiply every ingredient by 3. A recipe serves 8 and you need 4: 4 divided by 8 is 1/2, so multiply every ingredient by 1/2.",
                           "Factor de conversión = porciones deseadas divididas entre porciones originales. Una receta rinde 4 y necesitas 12: "
                           "12 entre 4 es 3, así que multiplica cada ingrediente por 3. Una receta rinde 8 y necesitas 4: 4 entre 8 es 1/2, "
                           "así que multiplica cada ingrediente por 1/2.")},
                {"heading": T("Step by step", "Paso a paso"),
                 "body": T("Step 1: find the factor. Step 2: multiply each ingredient by the factor. Step 3: simplify using equivalents, for example "
                           "12 tsp becomes 4 Tbsp. Step 4: check that the amounts make sense. Step 5: adjust time and pan size.",
                           "Paso 1: encuentra el factor. Paso 2: multiplica cada ingrediente por el factor. Paso 3: simplifica usando equivalentes; por ejemplo, "
                           "12 cdtas se convierten en 4 cdas. Paso 4: verifica que las cantidades tengan sentido. Paso 5: ajusta el tiempo y el tamaño de la sartén.")},
                {"heading": T("What does not scale", "Qué no escala"),
                 "body": T("Cooking time, pan size, and oven temperature do not scale. An egg cannot be divided easily: beat it and measure about 3 "
                           "tablespoons for one whole large egg. Strong spices and salt are best added a little less than the math says, then tasted.",
                           "El tiempo de cocción, el tamaño de la sartén y la temperatura del horno no escalan. Un huevo no se puede dividir fácilmente: bátelo y mide "
                           "aproximadamente 3 cucharadas para un huevo grande entero. Las especias fuertes y la sal conviene agregarlas un poco menos de lo que dice "
                           "la matemática y luego probar.")},
                {"heading": T("Cost and shopping", "Costo y compras"),
                 "body": T("Scaling also tells you what to buy. If one group needs 1 1/2 cups of flour and 8 groups cook, the class needs 12 cups, which is "
                           "3 quarts. Cost per serving = total cost divided by number of servings.",
                           "Escalar también te dice qué comprar. Si un grupo necesita 1 1/2 tazas de harina y cocinan 8 grupos, la clase necesita 12 tazas, que "
                           "son 3 cuartos. Costo por porción = costo total dividido entre el número de porciones.")},
            ],
            "guided": {
                "title": T("Scale a Recipe Together", "Escalen una receta juntos"),
                "steps": [T("Use the practice recipe card. It serves 8. Scale it to serve 4 (factor 1/2). Do the first two ingredients together.",
                            "Usen la tarjeta de receta de práctica. Rinde 8. Escálenla para 4 porciones (factor 1/2). Hagan juntos los dos primeros ingredientes."),
                          T("Finish the rest with a partner. Use an equivalent to simplify at least one amount.", "Terminen el resto con un compañero. Usen un equivalente para simplificar al menos una cantidad.")],
            },
            "independent": {
                "kind": "activity",
                "title": T("Scale It: Three Problems", "Escálalo: tres problemas"),
                "steps": [T("Scale the pancake recipe from 8 servings to 4 servings (tomorrow's lab). Fill in your group's column on the recipe card.",
                            "Escala la receta de panqueques de 8 porciones a 4 porciones (el laboratorio de mañana). Llena la columna de tu grupo en la tarjeta de receta."),
                          T("Scale the same recipe to 32 servings for the whole class. How much flour, milk, and eggs does the teacher need to buy?",
                            "Escala la misma receta a 32 porciones para toda la clase. ¿Cuánta harina, leche y huevos debe comprar la maestra?"),
                          T("Explain in one sentence what you will adjust besides the amounts.", "Explica en una oración qué ajustarás además de las cantidades.")],
            },
            "exit": [{"q": T("A recipe serves 6 and you need 18. What is the conversion factor?", "Una receta rinde 6 y necesitas 18. ¿Cuál es el factor de conversión?"),
                      "answer": T("3 (18 divided by 6).", "3 (18 entre 6).")},
                     {"q": T("Name one thing that does not scale directly when you change a recipe.", "Nombra algo que no escala directamente cuando cambias una receta."),
                      "answer": T("Cooking time, pan size, or oven temperature.", "El tiempo de cocción, el tamaño de la sartén o la temperatura del horno.")}],
            "teacher": {
                "materials": ["Practice recipe card (serves 8)", "Pancake recipe card with blank column", "Calculators", "Answer key"],
                "notes": ["Key for pancakes serves 8 -> serves 4 (x 1/2): flour 3 c -> 1 1/2 c; baking powder 7 tsp -> 3 1/2 tsp; salt 2 tsp -> 1 tsp; "
                          "sugar 2 Tbsp -> 1 Tbsp; milk 2 1/2 c -> 1 1/4 c; eggs 2 -> 1; oil 6 Tbsp -> 3 Tbsp.",
                          "Key for serves 8 -> serves 32 (x 4): flour 12 c (3 qt); baking powder 28 tsp (9 Tbsp + 1 tsp); salt 8 tsp (2 Tbsp + 2 tsp); "
                          "sugar 8 Tbsp (1/2 c); milk 10 c (2 1/2 qt); eggs 8; oil 24 Tbsp (1 1/2 c).",
                          "This is the cert performance task for S3.5: score it with the Unit 2 practical rubric on Day 9."],
            },
        },
        # ------------------------------------------------------------------ DAY 9 (LAB)
        {
            "day": 9, "kind": "lab",
            "title": T("Lab 3: Scaled Pancakes (Performance Task)", "Laboratorio 3: Panqueques escalados (tarea de desempeño)"),
            "objectives": [T("I can use my scaled recipe to cook a successful batch.", "Puedo usar mi receta escalada para cocinar una tanda exitosa."),
                           T("I can use heat and a griddle or skillet safely.", "Puedo usar calor y una plancha o sartén de forma segura."),
                           T("I can work as a team and finish on time.", "Puedo trabajar en equipo y terminar a tiempo.")],
            "cert": ["S3.5", "S3.1", "S3.3", "S3.4"],
            "vocab": ["Yield", "Conversion factor"],
            "bellringer": T("Check your scaled amounts from yesterday against your partner's. Fix any differences before you start.",
                            "Compara tus cantidades escaladas de ayer con las de tu compañero. Corrige cualquier diferencia antes de empezar."),
            "instruction": [
                {"heading": T("Lab brief: safety focus is cook and clean", "Introducción: el enfoque de seguridad es cocinar y limpiar"),
                 "body": T("Turn pot and pan handles inward. Use dry oven mitts, never wet ones. If oil smokes, tell your teacher. Wash hands after cracking eggs, "
                           "and wash the bowl and whisk before using them for anything else. Pancakes are done when the middle is set and no raw batter shows.",
                           "Gira hacia adentro los mangos de ollas y sartenes. Usa guantes de horno secos, nunca mojados. Si el aceite echa humo, avisa a tu maestra. "
                           "Lávate las manos después de romper huevos, y lava el tazón y el batidor antes de usarlos para otra cosa. Los panqueques están listos cuando el "
                           "centro está firme y no se ve masa cruda.")},
            ],
            "guided": {
                "title": T("Group Work Plan", "Plan de trabajo del grupo"),
                "steps": [T("Divide the steps among the four jobs and write estimated minutes for each. Include 12 minutes for cooking pancakes in batches.",
                            "Divide los pasos entre las cuatro tareas y escribe los minutos estimados de cada una. Incluye 12 minutos para cocinar los panqueques por tandas."),
                          T("Have your teacher check your scaled amounts before you start.", "Pide a tu maestra que revise tus cantidades escaladas antes de empezar.")],
            },
            "independent": {
                "kind": "lab",
                "recipe": "pancakes",
                "title": T("Cook: Scaled Pancakes", "Cocinar: Panqueques escalados"),
                "steps": [T("Cook using your own scaled amounts, not the printed ones. Your Safety Officer signs off each safety checkpoint.",
                            "Cocina con tus propias cantidades escaladas, no con las impresas. Tu Oficial de seguridad firma cada punto de control de seguridad."),
                          T("Your teacher scores your scaled recipe and your lab using the Unit 2 practical rubric.", "Tu maestra califica tu receta escalada y tu laboratorio con la rúbrica de la práctica de la Unidad 2.")],
            },
            "exit": [{"q": T("Did your scaled amounts work? What would you change next time?", "¿Funcionaron tus cantidades escaladas? ¿Qué cambiarías la próxima vez?"),
                      "answer": T("Answers vary; look for a specific, honest reflection.", "Las respuestas varían; busca una reflexión específica y honesta.")},
                     {"q": T("What did you adjust besides the amounts?", "¿Qué ajustaste además de las cantidades?"),
                      "answer": T("Cooking time, heat, or number of batches.", "Tiempo de cocción, calor o número de tandas.")}],
            "teacher": {
                "materials": ["Pancake recipe cards", "Ingredients (see recipe)", "Griddles or skillets", "Oven mitts", "Practical rubric"],
                "notes": ["Egg allergy: use a prepared egg-free pancake mix scaled by the same factor, or have the student do the scaling task and join a group using non-egg roles.",
                          "Peanut-free: check baking powder, milk, and syrup labels.",
                          "Estimated cost: about $2 per group, $16 for 8 groups. Verify against current prices.",
                          "Do a quick stove safety demonstration first if students have not used the stove yet (handles inward, dry mitts, grease fire: cover, do not use water)."],
            },
        },
    ],

    "recipes": {
        "snackmix": {
            "title": T("Measuring Mix (Snack Mix)", "Mezcla para botanear"),
            "serves": 4, "active_minutes": 15,
            "allergens": T("May contain wheat, soy, and milk. Pumpkin seeds are a seed, not a tree nut. Read labels: all items must be peanut-free.",
                           "Puede contener trigo, soya y leche. Las semillas de calabaza son semillas, no nueces de árbol. Lee las etiquetas: todos los productos deben ser sin cacahuate."),
            "equipment": [T("Dry measuring cups", "Tazas medidoras secas"), T("Measuring spoons", "Cucharas medidoras"), T("Large mixing bowl", "Tazón grande para mezclar"),
                          T("Spoon", "Cuchara"), T("Kitchen scale", "Báscula de cocina"), T("4 small bowls", "4 tazones pequeños")],
            "ingredients": [
                {"qty": "2", "unit": T("cups", "tazas"), "item": T("O-shaped cereal", "cereal en forma de O")},
                {"qty": "1", "unit": T("cup", "taza"), "item": T("small pretzels", "pretzels pequeños")},
                {"qty": "1/2", "unit": T("cup", "taza"), "item": T("raisins", "pasas")},
                {"qty": "1/4", "unit": T("cup", "taza"), "item": T("pumpkin seeds (peanut-free)", "semillas de calabaza (sin cacahuate)")},
                {"qty": "1", "unit": T("tablespoon", "cucharada"), "item": T("cinnamon sugar", "azúcar con canela")},
            ],
            "steps": [
                {"text": T("Wash hands for 20 seconds. Wash, rinse, and sanitize the counter.", "Lávate las manos durante 20 segundos. Lava, enjuaga y desinfecta el mostrador."),
                 "checkpoint": T("CLEAN: Safety Officer checks hands and counter.", "LIMPIAR: el Oficial de seguridad revisa las manos y el mostrador.")},
                {"text": T("Read every label. Confirm each item says peanut-free.", "Lee cada etiqueta. Confirma que cada producto dice sin cacahuate."),
                 "checkpoint": T("ALLERGY: Safety Officer signs the label check.", "ALERGIA: el Oficial de seguridad firma la revisión de etiquetas.")},
                {"text": T("Measure each dry ingredient with a dry cup or spoon. Spoon in, then level off with the back of a knife.", "Mide cada ingrediente seco con una taza o cuchara seca. Pon con cuchara y nivela con el dorso de un cuchillo."),
                 "checkpoint": None},
                {"text": T("Use an equivalent for one amount, for example measure 1/4 cup as 4 tablespoons. Write it on your work plan.", "Usa un equivalente para una cantidad; por ejemplo, mide 1/4 de taza como 4 cucharadas. Anótalo en tu plan de trabajo."),
                 "checkpoint": None},
                {"text": T("Mix everything gently in the large bowl.", "Mezcla todo con suavidad en el tazón grande."), "checkpoint": None},
                {"text": T("Weigh 1 cup of your mix on the scale. Write the weight on your work plan.", "Pesa 1 taza de tu mezcla en la báscula. Anota el peso en tu plan de trabajo."),
                 "checkpoint": None},
                {"text": T("Divide into 4 small bowls and eat together.", "Divide en 4 tazones pequeños y coman juntos."), "checkpoint": None},
                {"text": T("Wash dishes, sanitize the counter, return equipment, and call for the station check.", "Lava los platos, desinfecta el mostrador, devuelve el equipo y pide la revisión de la estación."),
                 "checkpoint": T("CLEAN: Cleanup Manager signs the station check.", "LIMPIAR: el Encargado de limpieza firma la revisión de la estación.")},
            ],
            "cost_per_group": "$2.00 (estimate)",
        },
        "pancakes": {
            "title": T("Scaled Pancakes", "Panqueques escalados"),
            "serves": 8, "active_minutes": 25,
            "scale_col": True,
            "scale_note": T("This card is written for 8 servings (16 pancakes). Your group is cooking for 4. Scale every ingredient and write your group's amount in the last column before you start.",
                            "Esta tarjeta está escrita para 8 porciones (16 panqueques). Tu grupo cocina para 4. Escala cada ingrediente y escribe la cantidad de tu grupo en la última columna antes de empezar."),
            "allergens": T("Contains wheat, milk, and eggs. Check baking powder, milk, and syrup labels for peanut-free. Egg dishes must be cooked until set.",
                           "Contiene trigo, leche y huevos. Revisa las etiquetas del polvo de hornear, la leche y el jarabe para confirmar que no tienen cacahuate. Los platillos con huevo deben cocinarse hasta quedar firmes."),
            "equipment": [T("Dry and liquid measuring cups", "Tazas medidoras secas y líquidas"), T("Measuring spoons", "Cucharas medidoras"), T("Two mixing bowls", "Dos tazones para mezclar"),
                          T("Whisk", "Batidor"), T("Griddle or skillet", "Plancha o sartén"), T("Spatula", "Espátula"), T("Oven mitts", "Guantes de horno"), T("Plates and forks", "Platos y tenedores")],
            "ingredients": [
                {"qty": "3", "unit": T("cups", "tazas"), "item": T("all-purpose flour", "harina de trigo")},
                {"qty": "7", "unit": T("teaspoons", "cucharaditas"), "item": T("baking powder", "polvo de hornear")},
                {"qty": "2", "unit": T("teaspoons", "cucharaditas"), "item": T("salt", "sal")},
                {"qty": "2", "unit": T("tablespoons", "cucharadas"), "item": T("sugar", "azúcar")},
                {"qty": "2 1/2", "unit": T("cups", "tazas"), "item": T("milk", "leche")},
                {"qty": "2", "unit": T("large", "grandes"), "item": T("eggs", "huevos")},
                {"qty": "6", "unit": T("tablespoons", "cucharadas"), "item": T("vegetable oil", "aceite vegetal")},
            ],
            "steps": [
                {"text": T("Wash hands for 20 seconds. Wash, rinse, and sanitize the counter. Tie back hair.", "Lávate las manos durante 20 segundos. Lava, enjuaga y desinfecta el mostrador. Recógete el cabello."),
                 "checkpoint": T("CLEAN: Safety Officer checks hands and counter.", "LIMPIAR: el Oficial de seguridad revisa las manos y el mostrador.")},
                {"text": T("Scale the recipe for your group (4 servings) and have your teacher check your amounts.", "Escala la receta para tu grupo (4 porciones) y pide a tu maestra que revise tus cantidades."),
                 "checkpoint": T("MATH: Teacher initials the scaled amounts.", "MATEMÁTICAS: la maestra pone sus iniciales en las cantidades escaladas.")},
                {"text": T("In one bowl, whisk the flour, baking powder, salt, and sugar. Measure dry ingredients by spooning and leveling.", "En un tazón, bate la harina, el polvo de hornear, la sal y el azúcar. Mide los secos poniendo con cuchara y nivelando."),
                 "checkpoint": None},
                {"text": T("In the second bowl, whisk the milk, eggs, and oil. Wash hands after cracking eggs.", "En el segundo tazón, bate la leche, los huevos y el aceite. Lávate las manos después de romper los huevos."),
                 "checkpoint": T("CLEAN: Wash hands after touching raw egg.", "LIMPIAR: lávate las manos después de tocar huevo crudo.")},
                {"text": T("Pour the wet mixture into the dry mixture. Stir only until just combined; a few lumps are fine.", "Vierte la mezcla húmeda en la mezcla seca. Revuelve solo hasta combinar; unos grumos están bien."),
                 "checkpoint": None},
                {"text": T("Heat the griddle or skillet over medium heat. Pour about 1/4 cup of batter per pancake.", "Calienta la plancha o sartén a fuego medio. Vierte aproximadamente 1/4 de taza de masa por panqueque."),
                 "checkpoint": T("COOK: Handles inward. Dry oven mitts only.", "COCINAR: mangos hacia adentro. Solo guantes de horno secos.")},
                {"text": T("Flip when bubbles form and the edges look set, about 2 minutes. Cook until the middle is set and no raw batter shows.", "Voltea cuando se formen burbujas y los bordes se vean firmes, aproximadamente 2 minutos. Cocina hasta que el centro esté firme y no se vea masa cruda."),
                 "checkpoint": T("COOK: Pancakes are cooked through before serving.", "COCINAR: los panqueques están bien cocidos antes de servir.")},
                {"text": T("Eat together. Wash dishes, sanitize the counter, return equipment, and call for the station check.", "Coman juntos. Lava los platos, desinfecta el mostrador, devuelve el equipo y pide la revisión de la estación."),
                 "checkpoint": T("CLEAN: Cleanup Manager signs the station check.", "LIMPIAR: el Encargado de limpieza firma la revisión de la estación.")},
            ],
            "cost_per_group": "$2.00 (estimate)",
        },
    },

    "quiz": [
        {"cert": "S3.2", "q": T("Which tool should you use to measure flour?", "¿Qué herramienta debes usar para medir harina?"),
         "choices": [T("A dry measuring cup, leveled off", "Una taza medidora seca, nivelada"), T("A liquid measuring cup", "Una taza medidora líquida"),
                     T("A coffee mug", "Una taza de café"), T("Any bowl", "Cualquier tazón")], "answer": 0},
        {"cert": "S3.2", "q": T("How should you read a liquid measuring cup?", "¿Cómo debes leer una taza medidora líquida?"),
         "choices": [T("From above, holding it in the air", "Desde arriba, sosteniéndola en el aire"),
                     T("On a flat counter, at eye level, reading the bottom of the curve", "Sobre un mostrador plano, a la altura de los ojos, leyendo la parte inferior de la curva"),
                     T("By shaking it", "Agitándola"), T("By tasting it", "Probándola")], "answer": 1},
        {"cert": "S3.5", "q": T("How many teaspoons are in 1 tablespoon?", "¿Cuántas cucharaditas hay en 1 cucharada?"),
         "choices": [T("2", "2"), T("3", "3"), T("4", "4"), T("6", "6")], "answer": 1},
        {"cert": "S3.5", "q": T("How many tablespoons are in 1 cup?", "¿Cuántas cucharadas hay en 1 taza?"),
         "choices": [T("8", "8"), T("12", "12"), T("16", "16"), T("24", "24")], "answer": 2},
        {"cert": "S3.5", "q": T("How many cups are in 1 pint?", "¿Cuántas tazas hay en 1 pinta?"),
         "choices": [T("1", "1"), T("2", "2"), T("4", "4"), T("8", "8")], "answer": 1},
        {"cert": "S3.5", "q": T("How many ounces are in 1 pound?", "¿Cuántas onzas hay en 1 libra?"),
         "choices": [T("8", "8"), T("12", "12"), T("16", "16"), T("32", "32")], "answer": 2},
        {"cert": "S3.5", "q": T("What is half of 3/4 cup?", "¿Cuánto es la mitad de 3/4 de taza?"),
         "choices": [T("1/4 cup", "1/4 de taza"), T("3/8 cup", "3/8 de taza"), T("1/2 cup", "1/2 taza"), T("2/3 cup", "2/3 de taza")], "answer": 1},
        {"cert": "S3.5", "q": T("A recipe serves 4. You need 12 servings. What is the conversion factor?", "Una receta rinde 4. Necesitas 12 porciones. ¿Cuál es el factor de conversión?"),
         "choices": [T("2", "2"), T("3", "3"), T("4", "4"), T("8", "8")], "answer": 1},
        {"cert": "S3.5", "q": T("A recipe uses 1 1/2 cups of flour for 4 servings. How much flour for 8 servings?", "Una receta usa 1 1/2 tazas de harina para 4 porciones. ¿Cuánta harina para 8 porciones?"),
         "choices": [T("2 cups", "2 tazas"), T("2 1/2 cups", "2 1/2 tazas"), T("3 cups", "3 tazas"), T("4 cups", "4 tazas")], "answer": 2},
        {"cert": "S3.5", "q": T("A recipe for 8 uses 2 teaspoons of salt. How much salt for 4 servings?", "Una receta para 8 usa 2 cucharaditas de sal. ¿Cuánta sal para 4 porciones?"),
         "choices": [T("4 teaspoons", "4 cucharaditas"), T("1 teaspoon", "1 cucharadita"), T("1/4 teaspoon", "1/4 de cucharadita"), T("2 teaspoons", "2 cucharaditas")], "answer": 1},
        {"cert": "S3.5", "q": T("Which of these does NOT scale directly when you change a recipe?", "¿Cuál de estos NO escala directamente cuando cambias una receta?"),
         "choices": [T("Cups of flour", "Tazas de harina"), T("Teaspoons of baking powder", "Cucharaditas de polvo de hornear"),
                     T("Cooking time and pan size", "Tiempo de cocción y tamaño de la sartén"), T("Cups of milk", "Tazas de leche")], "answer": 2},
        {"cert": "S3.4", "q": T("Cost per serving equals:", "El costo por porción es igual a:"),
         "choices": [T("Total cost divided by number of servings", "Costo total dividido entre el número de porciones"),
                     T("Number of servings divided by total cost", "Número de porciones dividido entre el costo total"),
                     T("Total cost times number of servings", "Costo total por número de porciones"),
                     T("Total cost minus number of servings", "Costo total menos número de porciones")], "answer": 0},
    ],

    "practical": {
        "title": T("Unit 2 Practical: Scaling a Recipe", "Práctica de la Unidad 2: Escalar una receta"),
        "scale": "0-10 (cert performance scale). Target average: 8 or higher.",
        "criteria": [
            {"cert": "S3.5", "name": T("Scaling math", "Matemáticas de escalado"),
             "high": T("Correct factor; every ingredient correctly scaled and simplified with equivalents.", "Factor correcto; todos los ingredientes escalados correctamente y simplificados con equivalentes."),
             "mid": T("Correct factor; one or two ingredient errors.", "Factor correcto; uno o dos errores en ingredientes."),
             "low": T("Wrong factor or several errors.", "Factor incorrecto o varios errores.")},
            {"cert": "S3.2", "name": T("Measuring accuracy", "Exactitud al medir"),
             "high": T("Uses correct tools; levels dry ingredients; reads liquids at eye level.", "Usa las herramientas correctas; nivela los secos; lee los líquidos a la altura de los ojos."),
             "mid": T("Mostly correct technique.", "Técnica casi siempre correcta."),
             "low": T("Wrong tools or no leveling.", "Herramientas incorrectas o sin nivelar.")},
            {"cert": "S3.4", "name": T("Work plan and teamwork", "Plan de trabajo y trabajo en equipo"),
             "high": T("Plan complete; jobs done; finishes on time and helps others.", "Plan completo; tareas cumplidas; termina a tiempo y ayuda a otros."),
             "mid": T("Plan complete; needs reminders.", "Plan completo; necesita recordatorios."),
             "low": T("Plan missing or needs frequent redirection.", "Falta el plan o necesita redirección frecuente.")},
            {"cert": "S3.1", "name": T("Clean, cook, and station check", "Limpiar, cocinar y revisión de la estación"),
             "high": T("Washes hands after raw egg; cooks pancakes through; station passes the first time.", "Se lava las manos después del huevo crudo; cocina bien los panqueques; la estación aprueba a la primera."),
             "mid": T("Minor corrections needed.", "Se necesitan correcciones menores."),
             "low": T("Skips handwashing or station fails.", "Omite el lavado de manos o la estación no aprueba.")},
        ],
    },
}
