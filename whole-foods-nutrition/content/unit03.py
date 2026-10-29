"""Unit 3 — Kitchen Equipment, Utensils and Knife Skills (Days 10-14, 3 labs).

Cert alignment: S3.2 (safe use and care of equipment, tools, knives), S3.3 (basic methods), S3.1 (thermometer, clean/cook).
Spanish text is machine-assisted and has NOT had a fluent human review (see README).
"""
from .common import T

UNIT = {
    "number": 3,
    "slug": "equipment-and-knives",
    "title": T("Kitchen Equipment, Utensils, and Knife Skills", "Equipo, utensilios y técnicas con cuchillo"),
    "days": "10-14",
    "labs": 3,
    "cert": ["S3.2", "S3.3", "S3.1"],
    "essential_question": T(
        "How do the right tool and the right technique make cooking safer, faster, and better?",
        "¿Cómo hacen el cocinar más seguro, más rápido y mejor la herramienta y la técnica correctas?"),
    "overview": T(
        "A kitchen is full of tools that can burn, cut, or pinch if they are used the wrong way. In this unit you will "
        "learn the tools and appliances in our kitchen, how to use and clean them safely, and how to cut food with a knife "
        "using a claw grip. You will practice knife cuts, stovetop cooking, and a blender in three labs.",
        "Una cocina está llena de herramientas que pueden quemar, cortar o pellizcar si se usan de manera incorrecta. En esta "
        "unidad aprenderás las herramientas y los aparatos de nuestra cocina, cómo usarlos y limpiarlos con seguridad, y cómo "
        "cortar alimentos con un cuchillo usando la posición de garra. Practicarás cortes de cuchillo, cocina en estufa y el uso de "
        "una licuadora en tres laboratorios."),

    "vocab_bank": [
        {"term": T("Utensil", "Utensilio"),
         "definition": T("A hand tool used to prepare, cook, or serve food, such as a whisk, spatula, or tongs.",
                         "Una herramienta manual para preparar, cocinar o servir alimentos, como un batidor, una espátula o unas pinzas.")},
        {"term": T("Appliance", "Aparato eléctrico"),
         "definition": T("A machine that uses electricity or gas to do a kitchen job, such as a blender, oven, or microwave.",
                         "Una máquina que usa electricidad o gas para hacer un trabajo en la cocina, como una licuadora, un horno o un microondas.")},
        {"term": T("Claw grip", "Posición de garra"),
         "definition": T("A safe way to hold food by curling your fingertips under so your knuckles guide the knife.",
                         "Una forma segura de sujetar los alimentos doblando las yemas de los dedos hacia adentro para que los nudillos guíen el cuchillo.")},
        {"term": T("Dice", "Cortar en cubos"),
         "definition": T("To cut food into small, even cubes.", "Cortar los alimentos en cubos pequeños y uniformes.")},
        {"term": T("Julienne", "Juliana"),
         "definition": T("To cut food into thin matchstick strips.", "Cortar los alimentos en tiras delgadas como palitos de fósforo.")},
        {"term": T("Mince", "Picar finamente"),
         "definition": T("To cut food into very tiny pieces.", "Cortar los alimentos en pedazos muy pequeños.")},
        {"term": T("Grease fire", "Fuego de grasa"),
         "definition": T("A fire fueled by cooking oil or fat. Never put water on it; cover it with a lid and turn off the heat.",
                         "Un fuego alimentado por aceite o grasa de cocina. Nunca le eches agua; tápalo con una tapa y apaga el calor.")},
        {"term": T("Food thermometer", "Termómetro de cocina"),
         "definition": T("A tool that measures the internal temperature of food to show whether it is safe.",
                         "Una herramienta que mide la temperatura interna de los alimentos para mostrar si son seguros.")},
    ],

    "reading": {
        "title": T("The Sharp Truth About Knives", "La verdad sobre los cuchillos afilados"),
        "body": [
            T("It may sound backward, but a sharp knife is safer than a dull one. A sharp blade cuts with little pressure, so it goes where "
              "you aim it. A dull blade needs a lot of force, and it can slip off a tomato or a carrot and cut your hand.",
              "Puede sonar al revés, pero un cuchillo afilado es más seguro que uno sin filo. Una hoja afilada corta con poca presión, así que va "
              "adonde la diriges. Una hoja sin filo necesita mucha fuerza y puede resbalar sobre un tomate o una zanahoria y cortarte la mano."),
            T("Professional cooks protect themselves with habits. They put a damp towel under the cutting board so it does not slide. They tuck "
              "their fingertips back so their knuckles guide the blade, a position called the claw grip. They cut a flat side on round foods so "
              "the food does not roll. They carry a knife at their side with the point down, and they never try to catch a falling knife.",
              "Los cocineros profesionales se protegen con hábitos. Ponen una toalla húmeda debajo de la tabla de cortar para que no se deslice. "
              "Doblan las yemas de los dedos hacia atrás para que los nudillos guíen la hoja, una posición llamada garra. Cortan un lado plano en "
              "los alimentos redondos para que no rueden. Llevan el cuchillo a su costado con la punta hacia abajo y nunca intentan atrapar un "
              "cuchillo que cae."),
            T("Every tool in a kitchen has a safe way to use it. A blender must have its lid on before it starts. A hot pan has its handle turned "
              "inward so no one bumps it. A microwave can make steam that burns, so cooks lift lids away from their faces. A grease fire must "
              "never be put out with water, because water makes burning oil splash.",
              "Cada herramienta de una cocina tiene una forma segura de usarse. Una licuadora debe tener la tapa puesta antes de encenderse. Una "
              "sartén caliente tiene el mango girado hacia adentro para que nadie la golpee. Un microondas puede producir vapor que quema, así que "
              "los cocineros levantan las tapas alejándolas de la cara. Un fuego de grasa nunca debe apagarse con agua, porque el agua hace que el "
              "aceite ardiendo salpique."),
            T("Taking care of tools matters too. A knife is washed by hand, dried, and stored safely. Wooden tools and sharp knives usually "
              "stay out of the dishwasher. Good habits keep the kitchen safe and the tools working for years.",
              "Cuidar las herramientas también importa. Un cuchillo se lava a mano, se seca y se guarda de forma segura. Las herramientas de madera "
              "y los cuchillos afilados normalmente no van al lavavajillas. Los buenos hábitos mantienen la cocina segura y las herramientas "
              "funcionando durante años."),
        ],
        "questions": [
            {"q": T("Why is a sharp knife safer than a dull one?", "¿Por qué un cuchillo afilado es más seguro que uno sin filo?"),
             "answer": T("It needs less pressure, so it is less likely to slip.", "Necesita menos presión, así que es menos probable que resbale.")},
            {"q": T("What is the claw grip?", "¿Qué es la posición de garra?"),
             "answer": T("Fingertips curled under so knuckles guide the knife.", "Las yemas de los dedos dobladas hacia adentro para que los nudillos guíen el cuchillo.")},
            {"q": T("Why should you never use water on a grease fire?", "¿Por qué nunca debes usar agua en un fuego de grasa?"),
             "answer": T("Water makes burning oil splash and spread the fire.", "El agua hace que el aceite ardiendo salpique y extienda el fuego.")},
            {"q": T("How should a knife be carried?", "¿Cómo se debe llevar un cuchillo?"),
             "answer": T("At your side, point down.", "A tu costado, con la punta hacia abajo.")},
        ],
        "source_note": "Knife and fire safety practices are standard culinary and fire-safety guidance (for example USDA, NFPA).",
    },

    "lessons": [
        # ------------------------------------------------------------------ DAY 10
        {
            "day": 10, "kind": "lesson",
            "title": T("Know Your Kitchen: Tools and Appliances", "Conoce tu cocina: herramientas y aparatos"),
            "objectives": [T("I can name common kitchen tools and appliances and what each is used for.",
                             "Puedo nombrar herramientas y aparatos comunes de cocina y para qué sirve cada uno."),
                           T("I can use the stove, oven, microwave, and blender safely.",
                             "Puedo usar la estufa, el horno, el microondas y la licuadora con seguridad."),
                           T("I can clean and store tools so they last.", "Puedo limpiar y guardar las herramientas para que duren.")],
            "cert": ["S3.2"],
            "vocab": ["Utensil", "Appliance", "Grease fire"],
            "bellringer": T("List five tools or appliances you have used in a kitchen. For each, name one way it could hurt someone.",
                            "Haz una lista de cinco herramientas o aparatos que has usado en una cocina. Para cada uno, nombra una forma en que podría lastimar a alguien."),
            "instruction": [
                {"heading": T("Utensils, cookware, and appliances", "Utensilios, ollas y sartenes, y aparatos"),
                 "body": T("Utensils are hand tools such as whisks, spatulas, tongs, peelers, and graters. Cookware includes pots, skillets, and sheet pans. "
                           "Appliances use electricity or gas, such as the stove, oven, microwave, blender, and mixer. Choose the tool that fits the job.",
                           "Los utensilios son herramientas manuales como batidores, espátulas, pinzas, pelapapas y ralladores. Las ollas y sartenes incluyen "
                           "cacerolas, sartenes y charolas para hornear. Los aparatos usan electricidad o gas, como la estufa, el horno, el microondas, la licuadora "
                           "y la batidora. Elige la herramienta que corresponde al trabajo.")},
                {"heading": T("Stove and oven safety", "Seguridad en la estufa y el horno"),
                 "body": T("Turn pot handles inward. Never leave a burner unattended. Keep towels and sleeves away from flames and hot coils. Use dry oven mitts. "
                           "Lift lids away from your face so steam does not burn you. Open the oven door slowly and pull the rack out with two hands.",
                           "Gira hacia adentro los mangos de las ollas. Nunca dejes un quemador sin atención. Mantén toallas y mangas lejos de las llamas y de las "
                           "resistencias calientes. Usa guantes de horno secos. Levanta las tapas alejándolas de la cara para que el vapor no te queme. Abre la puerta del "
                           "horno lentamente y saca la rejilla con las dos manos.")},
                {"heading": T("Grease fire and emergencies", "Fuego de grasa y emergencias"),
                 "body": T("For a small grease fire: turn off the heat, slide a lid over the pan, and leave it covered. Never use water. Tell your teacher right away. "
                           "For a burn, run cool water over it for several minutes and tell your teacher.",
                           "Para un fuego pequeño de grasa: apaga el calor, desliza una tapa sobre la sartén y déjala tapada. Nunca uses agua. Avisa a tu maestra de "
                           "inmediato. Para una quemadura, deja correr agua fresca sobre ella durante varios minutos y avisa a tu maestra.")},
                {"heading": T("Microwave and blender safety", "Seguridad con el microondas y la licuadora"),
                 "body": T("Use only microwave-safe containers and never metal. Vent lids and let food stand before you check it. For a blender, put the lid on before "
                           "you start, keep hands and utensils out while it runs, and unplug it before you clean the blades. Do not fill it more than halfway with hot liquid.",
                           "Usa solo recipientes aptos para microondas y nunca metal. Ventila las tapas y deja reposar los alimentos antes de revisarlos. En una licuadora, "
                           "pon la tapa antes de encenderla, mantén las manos y los utensilios fuera mientras funciona y desconéctala antes de limpiar las cuchillas. No la "
                           "llenes más de la mitad con líquido caliente.")},
                {"heading": T("Care and cleaning", "Cuidado y limpieza"),
                 "body": T("Wash tools with hot, soapy water, rinse, and dry. Use only plastic or wood tools on nonstick pans. Keep wooden tools and sharp knives out of the "
                           "dishwasher. Unplug appliances before cleaning and never put the motor base in water.",
                           "Lava las herramientas con agua caliente y jabón, enjuaga y seca. Usa solo herramientas de plástico o madera en sartenes antiadherentes. Mantén "
                           "las herramientas de madera y los cuchillos afilados fuera del lavavajillas. Desconecta los aparatos antes de limpiarlos y nunca sumerjas la base "
                           "del motor en agua.")},
            ],
            "guided": {
                "title": T("Match the Tool to the Job", "Relaciona la herramienta con el trabajo"),
                "steps": [T("Look at the tool cards with your partner. Match each tool to its job on the sheet.", "Mira las tarjetas de herramientas con tu compañero. Relaciona cada herramienta con su trabajo en la hoja."),
                          T("Choose three tools and write one safety rule for each.", "Elige tres herramientas y escribe una regla de seguridad para cada una.")],
            },
            "independent": {
                "kind": "activity",
                "title": T("Equipment Circuit", "Circuito de equipo"),
                "steps": [T("Visit eight stations in the kitchen. At each one, name the tool or appliance, its job, and one safety rule.", "Visita ocho estaciones en la cocina. En cada una, nombra la herramienta o el aparato, su trabajo y una regla de seguridad."),
                          T("Draw or label the parts of one appliance.", "Dibuja o etiqueta las partes de un aparato."),
                          T("Write how you would clean and store each item.", "Escribe cómo limpiarías y guardarías cada artículo.")],
            },
            "exit": [{"q": T("What is one safety rule for the stove?", "¿Cuál es una regla de seguridad para la estufa?"),
                      "answer": T("Any: handles inward; do not leave unattended; dry mitts; towels away from flame.", "Cualquiera: mangos hacia adentro; no dejarla sin atención; guantes secos; toallas lejos de la llama.")},
                     {"q": T("What do you do for a small grease fire?", "¿Qué haces ante un fuego pequeño de grasa?"),
                      "answer": T("Turn off the heat, cover with a lid, never use water, tell the teacher.", "Apagar el calor, tapar con una tapa, nunca usar agua, avisar a la maestra.")}],
            "teacher": {
                "materials": ["Tool cards (picture and name)", "Tool-to-job matching sheet", "Eight labeled stations with real tools", "Fire extinguisher location reminder"],
                "notes": ["Demonstrate a lid on a pan for a grease fire; do not light a real fire in class.",
                          "Confirm your school's fire-safety rules and extinguisher type before teaching what to use.",
                          "Use picture-supported tool cards for students who need vocabulary support; they are in the slide deck notes."],
            },
        },
        # ------------------------------------------------------------------ DAY 11
        {
            "day": 11, "kind": "lesson",
            "title": T("Knife Safety and Basic Cuts", "Seguridad con cuchillos y cortes básicos"),
            "objectives": [T("I can hold and carry a knife safely.", "Puedo sostener y llevar un cuchillo con seguridad."),
                           T("I can use a claw grip and a stable cutting board.", "Puedo usar la posición de garra y una tabla de cortar estable."),
                           T("I can name and describe slice, dice, julienne, and mince.", "Puedo nombrar y describir rebanar, cortar en cubos, juliana y picar finamente.")],
            "cert": ["S3.2", "S3.3"],
            "vocab": ["Claw grip", "Dice", "Julienne", "Mince"],
            "bellringer": T("Why might a dull knife cause more cuts than a sharp one? Write your idea in one or two sentences.",
                            "¿Por qué un cuchillo sin filo podría causar más cortadas que uno afilado? Escribe tu idea en una o dos oraciones."),
            "instruction": [
                {"heading": T("Setting up", "Preparación"),
                 "body": T("Place the cutting board on a damp towel so it cannot slide. Choose the right knife: a chef's knife for most cutting, a paring knife for small "
                           "jobs, and a serrated knife for bread and tomatoes. Make sure the blade is sharp.",
                           "Coloca la tabla de cortar sobre una toalla húmeda para que no se deslice. Elige el cuchillo correcto: un cuchillo de chef para casi todo, un "
                           "cuchillo mondador para trabajos pequeños y un cuchillo de sierra para pan y tomates. Asegúrate de que la hoja esté afilada.")},
                {"heading": T("Safe handling rules", "Reglas para manejar el cuchillo con seguridad"),
                 "body": T("Carry a knife at your side with the point down. Cut away from your body. Never wave a knife or point it at anyone. Do not try to catch a falling knife; "
                           "step back. Never leave a knife in a sink of soapy water. Set it down on the board and let others pick it up themselves.",
                           "Lleva el cuchillo a tu costado con la punta hacia abajo. Corta alejándote de tu cuerpo. Nunca agites un cuchillo ni apuntes a nadie. No intentes "
                           "atrapar un cuchillo que cae; da un paso atrás. Nunca dejes un cuchillo en un fregadero con agua jabonosa. Déjalo sobre la tabla y deja que otros lo "
                           "recojan por sí mismos.")},
                {"heading": T("The claw grip", "La posición de garra"),
                 "body": T("Curl your fingertips under, like a claw, on the food you are holding. Your knuckles touch the side of the blade and guide it. Move the knife in a rocking "
                           "or slicing motion and keep the tip on the board. For round foods, cut a thin slice off one side and lay that flat side down.",
                           "Dobla las yemas de los dedos hacia adentro, como una garra, sobre el alimento que sujetas. Tus nudillos tocan el costado de la hoja y la guían. Mueve el "
                           "cuchillo con un movimiento de balanceo o de rebanado y mantén la punta sobre la tabla. En alimentos redondos, corta una rebanada delgada de un lado y "
                           "apoya ese lado plano hacia abajo.")},
                {"heading": T("Cuts to know", "Cortes que debes conocer"),
                 "body": T("Slice: cut into flat pieces. Dice: cut into small, even cubes, about 1/4 inch for small dice. Julienne: cut into thin matchsticks, about 1/8 inch thick "
                           "and 1 to 2 inches long. Mince: cut into very tiny pieces. Even cuts cook evenly and look better.",
                           "Rebanar: cortar en piezas planas. Cortar en cubos: cubos pequeños y uniformes, de aproximadamente 1/4 de pulgada para cubos pequeños. Juliana: tiras delgadas "
                           "como palitos de fósforo, de unos 1/8 de pulgada de grosor y de 1 a 2 pulgadas de largo. Picar finamente: pedazos muy pequeños. Los cortes uniformes "
                           "se cocinan parejos y se ven mejor.")},
                {"heading": T("Care of knives", "Cuidado de los cuchillos"),
                 "body": T("Wash knives by hand, one at a time, with the blade facing away from you. Dry them and store them in a block or sheath. Keep them sharp; ask your teacher "
                           "to sharpen them when they are dull.",
                           "Lava los cuchillos a mano, uno por uno, con la hoja alejada de ti. Sécalos y guárdalos en un bloque o funda. Manténlos afilados; pide a tu maestra que los "
                           "afile cuando pierdan el filo.")},
            ],
            "guided": {
                "title": T("Practice With Safe Props", "Práctica con materiales seguros"),
                "steps": [T("Watch your teacher demonstrate the claw grip and a rocking cut on a banana with a table knife.", "Observa a tu maestra demostrar la posición de garra y un corte de balanceo en un plátano con un cuchillo de mesa."),
                          T("Practice the claw grip on a lump of modeling clay with a plastic knife while your teacher checks each person.", "Practica la posición de garra en un trozo de plastilina con un cuchillo de plástico mientras tu maestra revisa a cada persona."),
                          T("Sign the knife safety agreement before you use a real knife.", "Firma el acuerdo de seguridad con cuchillos antes de usar un cuchillo de verdad.")],
            },
            "independent": {
                "kind": "activity",
                "title": T("Cut Cards and Safety Agreement", "Tarjetas de cortes y acuerdo de seguridad"),
                "steps": [T("Match each cut name to its picture and size on the cut card.", "Relaciona el nombre de cada corte con su imagen y tamaño en la tarjeta de cortes."),
                          T("Write the safe knife rules in your own words and sign the agreement.", "Escribe las reglas de seguridad con cuchillos con tus propias palabras y firma el acuerdo."),
                          T("Prepare your work plan for tomorrow's lab: which person cuts which vegetable?", "Prepara tu plan de trabajo para el laboratorio de mañana: ¿qué persona corta qué verdura?")],
            },
            "exit": [{"q": T("Describe the claw grip in one sentence.", "Describe la posición de garra en una oración."),
                      "answer": T("Fingertips curled under so knuckles guide the blade.", "Yemas de los dedos dobladas hacia adentro para que los nudillos guíen la hoja.")},
                     {"q": T("Name one cut and describe it.", "Nombra un corte y descríbelo."),
                      "answer": T("Any: slice, dice, julienne, or mince with its description.", "Cualquiera: rebanar, cubos, juliana o picar con su descripción.")}],
            "teacher": {
                "materials": ["Modeling clay and plastic knives (1 per student)", "Bananas and table knives for demo", "Knife safety agreement (signed before any real knife)", "Cut cards"],
                "notes": ["No student uses a real knife until the safety agreement is signed.",
                          "Offer cut-resistant gloves if your school has them, and let a student hold produce with a fork if they have limited hand control.",
                          "Check that every knife in the lab is sharp and in good repair before tomorrow."],
            },
        },
        # ------------------------------------------------------------------ DAY 12 (LAB)
        {
            "day": 12, "kind": "lab",
            "title": T("Lab 4: Veggie Sticks and Yogurt Dip (Knife Skills)", "Laboratorio 4: Palitos de verdura y dip de yogur (técnicas con cuchillo)"),
            "objectives": [T("I can use a knife safely with a claw grip.", "Puedo usar un cuchillo con seguridad con la posición de garra."),
                           T("I can slice, julienne, and dice vegetables evenly.", "Puedo rebanar, cortar en juliana y en cubos las verduras de forma uniforme."),
                           T("I can wash produce and prevent cross-contamination.", "Puedo lavar los productos frescos y prevenir la contaminación cruzada.")],
            "cert": ["S3.2", "S3.3", "S3.1"],
            "vocab": ["Claw grip", "Dice", "Julienne"],
            "bellringer": T("Read today's recipe. Which cut will you make? Write the safety rule you will follow.", "Lee la receta de hoy. ¿Qué corte harás? Escribe la regla de seguridad que seguirás."),
            "instruction": [
                {"heading": T("Lab brief", "Introducción del laboratorio"),
                 "body": T("Today's safety focus: knives and separate. Damp towel under every board. One person cuts at a time while the others stay out of the cutting zone. "
                           "Wash vegetables before cutting and wash hands before touching the yogurt. Check labels for peanuts.",
                           "Enfoque de seguridad de hoy: cuchillos y separar. Una toalla húmeda debajo de cada tabla. Una persona corta a la vez mientras las demás se mantienen fuera "
                           "de la zona de corte. Lava las verduras antes de cortarlas y lávate las manos antes de tocar el yogur. Revisa las etiquetas para ver si tienen cacahuate.")},
            ],
            "guided": {
                "title": T("Group Work Plan", "Plan de trabajo del grupo"),
                "steps": [T("Write which person cuts which vegetable and who makes the dip.", "Escribe qué persona corta qué verdura y quién hace el dip."),
                          T("Plan time for cleanup of knives and boards.", "Planifica el tiempo para limpiar los cuchillos y las tablas.")],
            },
            "independent": {
                "kind": "lab",
                "recipe": "veggiesticks",
                "title": T("Cook: Veggie Sticks and Yogurt Dip", "Cocinar: Palitos de verdura y dip de yogur"),
                "steps": [T("Follow the recipe card. Your Safety Officer signs off each safety checkpoint.", "Sigue la tarjeta de receta. Tu Oficial de seguridad firma cada punto de control de seguridad."),
                          T("Show your teacher one cut from each vegetable for a skill check before you eat.", "Muestra a tu maestra un corte de cada verdura para una revisión de habilidades antes de comer."),
                          T("Complete cleanup. Knives are washed by hand one at a time and returned to storage.", "Completa la limpieza. Los cuchillos se lavan a mano uno por uno y se devuelven al almacén.")],
            },
            "exit": [{"q": T("Which cut was hardest for you? What will you try next time?", "¿Qué corte te resultó más difícil? ¿Qué intentarás la próxima vez?"),
                      "answer": T("Answers vary.", "Las respuestas varían.")},
                     {"q": T("How did your group keep produce safe?", "¿Cómo mantuvo tu grupo seguros los productos frescos?"),
                      "answer": T("Washed produce, clean board, handwashing, chilled the dip.", "Lavó los productos, usó tabla limpia, se lavó las manos y mantuvo frío el dip.")}],
            "teacher": {
                "materials": ["Recipe cards", "Ingredients (see recipe)", "Sharp knives and cutting boards", "Damp towels", "Peelers", "Skill check sheet (Unit 3 practical)"],
                "notes": ["Cost estimate: about $2.50 per group, $20 for 8 groups. Verify against current prices.",
                          "Milk allergy: use a dairy-free yogurt.",
                          "Teacher stays near cutting stations; use a one-cutter-at-a-time rule per table.",
                          "Peanut-free: confirm yogurt and seasoning labels."],
            },
        },
        # ------------------------------------------------------------------ DAY 13 (LAB)
        {
            "day": 13, "kind": "lab",
            "title": T("Lab 5: Bean and Cheese Quesadillas (Stovetop)", "Laboratorio 5: Quesadillas de frijol y queso (estufa)"),
            "objectives": [T("I can use a skillet and stove safely.", "Puedo usar una sartén y la estufa con seguridad."),
                           T("I can use a food thermometer to check that food is hot enough.", "Puedo usar un termómetro de cocina para verificar que los alimentos estén lo bastante calientes."),
                           T("I can grate cheese safely.", "Puedo rallar queso con seguridad.")],
            "cert": ["S3.2", "S3.3", "S3.1"],
            "vocab": ["Food thermometer", "Utensil"],
            "bellringer": T("Which stove safety rules will matter most in today's recipe? List two.", "¿Qué reglas de seguridad de la estufa serán más importantes en la receta de hoy? Anota dos."),
            "instruction": [
                {"heading": T("Lab brief", "Introducción del laboratorio"),
                 "body": T("Today's safety focus: cook. Handles inward. Dry mitts. Use a clean thermometer in the center of the quesadilla: it should read 165°F because we are heating "
                           "already-cooked beans. Grate cheese slowly and stop when the piece gets small. Let the skillet cool before washing.",
                           "Enfoque de seguridad de hoy: cocinar. Mangos hacia adentro. Guantes secos. Usa un termómetro limpio en el centro de la quesadilla: debe marcar 165 °F porque "
                           "calentamos frijoles ya cocidos. Ralla el queso despacio y deja de rallar cuando el trozo sea pequeño. Deja enfriar la sartén antes de lavarla.")},
            ],
            "guided": {
                "title": T("Group Work Plan", "Plan de trabajo del grupo"),
                "steps": [T("Write who grates, who rinses beans, who cooks, and who checks the temperature.", "Escribe quién ralla, quién enjuaga los frijoles, quién cocina y quién revisa la temperatura."),
                          T("Plan to cook the quesadillas in two rounds so the skillet is not crowded.", "Planifica cocinar las quesadillas en dos rondas para no llenar demasiado la sartén.")],
            },
            "independent": {
                "kind": "lab",
                "recipe": "quesadillas",
                "title": T("Cook: Bean and Cheese Quesadillas", "Cocinar: Quesadillas de frijol y queso"),
                "steps": [T("Follow the recipe card. Your Safety Officer signs off each safety checkpoint.", "Sigue la tarjeta de receta. Tu Oficial de seguridad firma cada punto de control de seguridad."),
                          T("Record the thermometer reading for each quesadilla.", "Anota la lectura del termómetro de cada quesadilla."),
                          T("Complete cleanup and the station check; the skillet cools before it goes in water.", "Completa la limpieza y la revisión de la estación; la sartén se enfría antes de ir al agua.")],
            },
            "exit": [{"q": T("What temperature did the quesadillas reach, and why did we check?", "¿Qué temperatura alcanzaron las quesadillas y por qué la revisamos?"),
                      "answer": T("At least 165°F; to be sure heated food is safe.", "Al menos 165 °F; para asegurar que el alimento calentado sea seguro.")},
                     {"q": T("Name one stove safety habit your group used.", "Nombra un hábito de seguridad en la estufa que usó tu grupo."),
                      "answer": T("Handles inward, dry mitts, or no unattended burner.", "Mangos hacia adentro, guantes secos o ningún quemador sin atención.")}],
            "teacher": {
                "materials": ["Recipe cards", "Ingredients (see recipe)", "Skillets", "Box graters", "Food thermometers", "Sanitizer wipes for thermometers"],
                "notes": ["Cost estimate: about $3 per group, $24 for 8 groups. Verify against current prices.",
                          "Milk allergy: use a dairy-free cheese or omit cheese and increase beans. Wheat allergy: use corn tortillas.",
                          "Peanut-free: check tortilla, bean, and salsa labels.",
                          "Sanitize the thermometer between uses."],
            },
        },
        # ------------------------------------------------------------------ DAY 14 (LAB)
        {
            "day": 14, "kind": "lab",
            "title": T("Lab 6: Fruit Smoothies (Blender)", "Laboratorio 6: Licuados de fruta (licuadora)"),
            "objectives": [T("I can assemble, run, and clean a blender safely.", "Puedo armar, usar y limpiar una licuadora con seguridad."),
                           T("I can layer ingredients so a blender works well.", "Puedo poner los ingredientes en capas para que la licuadora funcione bien."),
                           T("I can work as a team and finish on time.", "Puedo trabajar en equipo y terminar a tiempo.")],
            "cert": ["S3.2", "S3.3", "S3.4"],
            "vocab": ["Appliance"],
            "bellringer": T("Before you start the blender, what must you check first? List three things.", "Antes de encender la licuadora, ¿qué debes revisar primero? Anota tres cosas."),
            "instruction": [
                {"heading": T("Lab brief", "Introducción del laboratorio"),
                 "body": T("Today's safety focus: appliances. Check the blender is assembled correctly and the motor base is dry. Put the lid on and hold it down with a folded towel. "
                           "Never put a spoon or hand in a running blender. Unplug before cleaning. Add liquid first, then soft foods, then frozen foods on top.",
                           "Enfoque de seguridad de hoy: aparatos. Verifica que la licuadora esté bien armada y que la base del motor esté seca. Pon la tapa y sujétala con una toalla doblada. "
                           "Nunca pongas una cuchara ni la mano en una licuadora en funcionamiento. Desconecta antes de limpiar. Agrega primero el líquido, luego los alimentos suaves y al final "
                           "los congelados encima.")},
            ],
            "guided": {
                "title": T("Group Work Plan", "Plan de trabajo del grupo"),
                "steps": [T("Write who assembles the blender, who cuts bananas, who runs it, and who cleans it.", "Escribe quién arma la licuadora, quién corta los plátanos, quién la enciende y quién la limpia."),
                          T("If blenders are shared, write your group's turn on the schedule.", "Si se comparten las licuadoras, escribe el turno de tu grupo en el horario.")],
            },
            "independent": {
                "kind": "lab",
                "recipe": "smoothie",
                "title": T("Cook: Fruit Smoothies", "Cocinar: Licuados de fruta"),
                "steps": [T("Follow the recipe card. Your Safety Officer signs off each safety checkpoint.", "Sigue la tarjeta de receta. Tu Oficial de seguridad firma cada punto de control de seguridad."),
                          T("Taste and write one way you would change the recipe.", "Prueba y escribe una forma en que cambiarías la receta."),
                          T("Clean the blender using the soapy water method and complete the station check.", "Limpia la licuadora con el método de agua con jabón y completa la revisión de la estación.")],
            },
            "exit": [{"q": T("Why does the lid go on before the blender starts?", "¿Por qué la tapa se pone antes de encender la licuadora?"),
                      "answer": T("So food does not fly out and cause injury or a mess.", "Para que la comida no salga disparada y cause lesiones o desorden.")},
                     {"q": T("What order do ingredients go into the blender?", "¿En qué orden se ponen los ingredientes en la licuadora?"),
                      "answer": T("Liquid, then soft foods, then frozen foods.", "Líquido, luego alimentos suaves y al final los congelados.")}],
            "teacher": {
                "materials": ["Recipe cards", "Ingredients (see recipe)", "Blenders", "Folded towels", "Cups"],
                "notes": ["Cost estimate: about $2.50 per group, $20 for 8 groups. Verify against current prices.",
                          "If you have fewer than 8 blenders, schedule groups in two rounds or have two groups share. Unit total for Labs 4-6 is about $64 against the course budget.",
                          "Milk allergy: use a fortified soy or oat beverage and dairy-free yogurt.",
                          "Peanut-free: check frozen fruit and yogurt labels."],
            },
        },
    ],

    "recipes": {
        "veggiesticks": {
            "title": T("Veggie Sticks and Yogurt Dip", "Palitos de verdura y dip de yogur"),
            "serves": 4, "active_minutes": 25,
            "allergens": T("Contains milk (yogurt). All items must be peanut-free; check seasoning labels.",
                           "Contiene leche (yogur). Todos los productos deben ser sin cacahuate; revisa las etiquetas de los condimentos."),
            "equipment": [T("Chef's or paring knife", "Cuchillo de chef o mondador"), T("Cutting board and damp towel", "Tabla de cortar y toalla húmeda"), T("Vegetable peeler", "Pelapapas"),
                          T("Colander", "Colador"), T("Small mixing bowl", "Tazón pequeño para mezclar"), T("Measuring cups and spoons", "Tazas y cucharas medidoras"), T("Serving plate", "Plato para servir")],
            "ingredients": [
                {"qty": "3", "unit": T("medium", "medianas"), "item": T("carrots", "zanahorias")},
                {"qty": "1", "unit": T("medium", "mediano"), "item": T("cucumber", "pepino")},
                {"qty": "3", "unit": T("ribs", "tallos"), "item": T("celery", "apio")},
                {"qty": "1", "unit": T("cup", "taza"), "item": T("plain yogurt (kept cold)", "yogur natural (mantenido frío)")},
                {"qty": "1", "unit": T("tablespoon", "cucharada"), "item": T("lemon juice", "jugo de limón")},
                {"qty": "1/2", "unit": T("teaspoon", "cucharadita"), "item": T("dried dill or garlic powder", "eneldo seco o ajo en polvo")},
                {"qty": "1/4", "unit": T("teaspoon", "cucharadita"), "item": T("salt", "sal")},
            ],
            "steps": [
                {"text": T("Wash hands for 20 seconds. Wash, rinse, and sanitize the counter. Set a damp towel under each cutting board.", "Lávate las manos durante 20 segundos. Lava, enjuaga y desinfecta el mostrador. Pon una toalla húmeda debajo de cada tabla de cortar."),
                 "checkpoint": T("CLEAN: Safety Officer checks hands, counter, and towels.", "LIMPIAR: el Oficial de seguridad revisa las manos, el mostrador y las toallas.")},
                {"text": T("Read every label. Confirm peanut-free.", "Lee cada etiqueta. Confirma que sea sin cacahuate."),
                 "checkpoint": T("ALLERGY: Safety Officer signs the label check.", "ALERGIA: el Oficial de seguridad firma la revisión de etiquetas.")},
                {"text": T("Scrub and rinse carrots, cucumber, and celery under cool running water. Pat dry with a clean towel.", "Frota y enjuaga las zanahorias, el pepino y el apio con agua fría corriente. Seca con una toalla limpia."),
                 "checkpoint": T("CLEAN: Wash produce before cutting.", "LIMPIAR: lava los productos antes de cortarlos.")},
                {"text": T("Peel the carrots. Cut a flat side so each carrot lies steady, then julienne it into matchsticks.", "Pela las zanahorias. Corta un lado plano para que cada zanahoria quede firme y luego córtala en juliana."),
                 "checkpoint": T("KNIFE: Claw grip. One cutter at a time.", "CUCHILLO: posición de garra. Un solo cortador a la vez.")},
                {"text": T("Slice the cucumber into rounds, then cut each round in half.", "Rebana el pepino en rodajas y corta cada rodaja por la mitad."),
                 "checkpoint": None},
                {"text": T("Cut the celery into sticks about 3 inches long. Dice two of the sticks into small cubes for the dip topping.", "Corta el apio en palitos de unas 3 pulgadas. Corta dos palitos en cubos pequeños para decorar el dip."),
                 "checkpoint": None},
                {"text": T("Show your teacher one cut from each vegetable for the skill check. Wash hands and the board before touching the yogurt.", "Muestra a tu maestra un corte de cada verdura para la revisión de habilidades. Lávate las manos y la tabla antes de tocar el yogur."),
                 "checkpoint": T("TEACHER: Skill check initials.", "MAESTRA: iniciales de la revisión de habilidades.")},
                {"text": T("Take the yogurt out of the refrigerator now. Stir the yogurt, lemon juice, dill, and salt in a bowl. Top with the diced celery.", "Saca ahora el yogur del refrigerador. Mezcla el yogur, el jugo de limón, el eneldo y la sal en un tazón. Decora con el apio en cubos."),
                 "checkpoint": T("CHILL: Yogurt stays cold until this step.", "ENFRIAR: el yogur permanece frío hasta este paso.")},
                {"text": T("Arrange the vegetables on the plate and eat together. Put leftover dip in the refrigerator right away.", "Acomoda las verduras en el plato y coman juntos. Pon el dip sobrante en el refrigerador de inmediato."),
                 "checkpoint": T("CHILL: Leftovers go back within 2 hours.", "ENFRIAR: las sobras vuelven dentro de 2 horas.")},
                {"text": T("Wash knives by hand one at a time, blade facing away. Sanitize boards and counter, return equipment, and call for the station check.", "Lava los cuchillos a mano uno por uno, con la hoja alejada de ti. Desinfecta las tablas y el mostrador, devuelve el equipo y pide la revisión de la estación."),
                 "checkpoint": T("CLEAN: Cleanup Manager signs the station check.", "LIMPIAR: el Encargado de limpieza firma la revisión de la estación.")},
            ],
            "cost_per_group": "$2.50 (estimate)",
        },
        "quesadillas": {
            "title": T("Bean and Cheese Quesadillas", "Quesadillas de frijol y queso"),
            "serves": 4, "active_minutes": 25,
            "allergens": T("Contains wheat and milk. Check tortilla, bean, and salsa labels for peanut-free.",
                           "Contiene trigo y leche. Revisa las etiquetas de la tortilla, los frijoles y la salsa para confirmar que no tienen cacahuate."),
            "equipment": [T("Skillet and spatula", "Sartén y espátula"), T("Box grater", "Rallador de caja"), T("Colander", "Colador"), T("Fork and bowl", "Tenedor y tazón"),
                          T("Cutting board and pizza cutter or knife", "Tabla de cortar y cortador de pizza o cuchillo"), T("Food thermometer", "Termómetro de cocina"), T("Oven mitts", "Guantes de horno")],
            "ingredients": [
                {"qty": "4", "unit": T("8-inch", "de 8 pulgadas"), "item": T("flour tortillas", "tortillas de harina")},
                {"qty": "1", "unit": T("can (15 oz)", "lata (15 oz)"), "item": T("black beans, drained and rinsed", "frijoles negros, escurridos y enjuagados")},
                {"qty": "1", "unit": T("cup", "taza"), "item": T("shredded cheese (grate from a block)", "queso rallado (ralla de un bloque)")},
                {"qty": "1/2", "unit": T("cup", "taza"), "item": T("salsa", "salsa")},
                {"qty": "1", "unit": T("teaspoon", "cucharadita"), "item": T("oil for the pan", "aceite para la sartén")},
            ],
            "steps": [
                {"text": T("Wash hands for 20 seconds. Wash, rinse, and sanitize the counter.", "Lávate las manos durante 20 segundos. Lava, enjuaga y desinfecta el mostrador."),
                 "checkpoint": T("CLEAN: Safety Officer checks hands and counter.", "LIMPIAR: el Oficial de seguridad revisa las manos y el mostrador.")},
                {"text": T("Read every label. Confirm peanut-free.", "Lee cada etiqueta. Confirma que sea sin cacahuate."),
                 "checkpoint": T("ALLERGY: Safety Officer signs the label check.", "ALERGIA: el Oficial de seguridad firma la revisión de etiquetas.")},
                {"text": T("Drain and rinse the beans in the colander. Mash about half with a fork in a bowl.", "Escurre y enjuaga los frijoles en el colador. Machaca aproximadamente la mitad con un tenedor en un tazón."),
                 "checkpoint": None},
                {"text": T("Grate the cheese away from your fingertips. Stop when the piece is small.", "Ralla el queso alejando las yemas de los dedos. Deja de rallar cuando el trozo sea pequeño."),
                 "checkpoint": T("TOOL SAFETY: Grate away from fingers.", "SEGURIDAD CON HERRAMIENTAS: ralla alejando los dedos.")},
                {"text": T("Spread beans and cheese on half of each tortilla and fold it over.", "Extiende frijoles y queso en la mitad de cada tortilla y dóblala."),
                 "checkpoint": None},
                {"text": T("Heat the skillet over medium heat with a little oil. Cook each quesadilla 2 to 3 minutes per side until golden and the cheese melts.", "Calienta la sartén a fuego medio con un poco de aceite. Cocina cada quesadilla de 2 a 3 minutos por lado hasta que esté dorada y el queso se derrita."),
                 "checkpoint": T("COOK: Handles inward. Dry mitts only.", "COCINAR: mangos hacia adentro. Solo guantes secos.")},
                {"text": T("Put a clean thermometer in the center. It must read 165°F. Record it. Sanitize the thermometer.", "Pon un termómetro limpio en el centro. Debe marcar 165 °F. Anótalo. Desinfecta el termómetro."),
                 "checkpoint": T("COOK: 165°F in the center.", "COCINAR: 165 °F en el centro.")},
                {"text": T("Cut into wedges on the board and serve with salsa. Eat together.", "Corta en triángulos sobre la tabla y sirve con salsa. Coman juntos."),
                 "checkpoint": None},
                {"text": T("Let the skillet cool, then wash dishes, sanitize the counter, return equipment, and call for the station check.", "Deja enfriar la sartén y luego lava los platos, desinfecta el mostrador, devuelve el equipo y pide la revisión de la estación."),
                 "checkpoint": T("CLEAN: Cleanup Manager signs the station check.", "LIMPIAR: el Encargado de limpieza firma la revisión de la estación.")},
            ],
            "cost_per_group": "$3.00 (estimate)",
        },
        "smoothie": {
            "title": T("Fruit Smoothie", "Licuado de fruta"),
            "serves": 4, "active_minutes": 15,
            "allergens": T("Contains milk. Use fortified soy or oat beverage and dairy-free yogurt if needed. All items must be peanut-free.",
                           "Contiene leche. Usa bebida de soya u avena fortificada y yogur sin lácteos si es necesario. Todos los productos deben ser sin cacahuate."),
            "equipment": [T("Blender", "Licuadora"), T("Folded towel", "Toalla doblada"), T("Cutting board and table knife", "Tabla de cortar y cuchillo de mesa"),
                          T("Measuring cups", "Tazas medidoras"), T("4 cups", "4 vasos"), T("Rubber spatula (for use only when the blender is off)", "Espátula de goma (solo para usar con la licuadora apagada)")],
            "ingredients": [
                {"qty": "1", "unit": T("cup", "taza"), "item": T("milk or fortified soy beverage", "leche o bebida de soya fortificada")},
                {"qty": "3/4", "unit": T("cup", "taza"), "item": T("plain yogurt", "yogur natural")},
                {"qty": "2", "unit": T("medium", "medianos"), "item": T("ripe bananas", "plátanos maduros")},
                {"qty": "1 1/2", "unit": T("cups", "tazas"), "item": T("frozen fruit, no added sugar", "fruta congelada, sin azúcar añadida")},
            ],
            "steps": [
                {"text": T("Wash hands for 20 seconds. Wash, rinse, and sanitize the counter.", "Lávate las manos durante 20 segundos. Lava, enjuaga y desinfecta el mostrador."),
                 "checkpoint": T("CLEAN: Safety Officer checks hands and counter.", "LIMPIAR: el Oficial de seguridad revisa las manos y el mostrador.")},
                {"text": T("Read every label. Confirm peanut-free.", "Lee cada etiqueta. Confirma que sea sin cacahuate."),
                 "checkpoint": T("ALLERGY: Safety Officer signs the label check.", "ALERGIA: el Oficial de seguridad firma la revisión de etiquetas.")},
                {"text": T("Check that the blender is assembled with the blade and jar locked in place, and the base is dry and plugged in.", "Verifica que la licuadora esté armada con la cuchilla y la jarra bien colocadas, y que la base esté seca y conectada."),
                 "checkpoint": T("APPLIANCE: Teacher checks assembly.", "APARATO: la maestra revisa el armado.")},
                {"text": T("Peel and slice the bananas with the table knife.", "Pela y rebana los plátanos con el cuchillo de mesa."), "checkpoint": None},
                {"text": T("Add the milk first, then the yogurt and bananas, then the frozen fruit on top.", "Agrega primero la leche, luego el yogur y los plátanos y al final la fruta congelada encima."),
                 "checkpoint": T("CHILL: Yogurt and milk stay cold until this step.", "ENFRIAR: el yogur y la leche permanecen fríos hasta este paso.")},
                {"text": T("Put the lid on firmly and hold it with a folded towel. Pulse a few times, then blend on high for 30 to 45 seconds until smooth.", "Pon la tapa firmemente y sujétala con una toalla doblada. Pulsa varias veces y luego licúa a velocidad alta de 30 a 45 segundos hasta que quede suave."),
                 "checkpoint": T("APPLIANCE: Lid on. Nothing in the jar while it runs.", "APARATO: tapa puesta. Nada en la jarra mientras funciona.")},
                {"text": T("Turn off the blender and wait for the blade to stop. Pour into 4 cups. Taste and record one change you would make.", "Apaga la licuadora y espera a que la cuchilla se detenga. Sirve en 4 vasos. Prueba y anota un cambio que harías."),
                 "checkpoint": None},
                {"text": T("Unplug the blender. Fill the jar halfway with warm soapy water, put the lid on, and blend 20 seconds. Pour out and rinse. Wipe the base with a damp cloth; never put the base in water.", "Desconecta la licuadora. Llena la jarra hasta la mitad con agua tibia y jabón, pon la tapa y licúa 20 segundos. Vacía y enjuaga. Limpia la base con un paño húmedo; nunca sumerjas la base en agua."),
                 "checkpoint": T("APPLIANCE: Unplug before cleaning.", "APARATO: desconecta antes de limpiar.")},
                {"text": T("Wash dishes, sanitize the counter, return equipment, and call for the station check.", "Lava los platos, desinfecta el mostrador, devuelve el equipo y pide la revisión de la estación."),
                 "checkpoint": T("CLEAN: Cleanup Manager signs the station check.", "LIMPIAR: el Encargado de limpieza firma la revisión de la estación.")},
            ],
            "cost_per_group": "$2.50 (estimate)",
        },
    },

    "quiz": [
        {"cert": "S3.2", "q": T("Why is a sharp knife safer than a dull one?", "¿Por qué un cuchillo afilado es más seguro que uno sin filo?"),
         "choices": [T("It needs less force, so it is less likely to slip", "Necesita menos fuerza, así que es menos probable que resbale"),
                     T("It cuts faster, so you can cut without looking", "Corta más rápido, así que puedes cortar sin mirar"),
                     T("It is lighter", "Es más ligero"), T("It never cuts skin", "Nunca corta la piel")], "answer": 0},
        {"cert": "S3.2", "q": T("What is the claw grip?", "¿Qué es la posición de garra?"),
         "choices": [T("Curling fingertips under so knuckles guide the knife", "Doblar las yemas de los dedos para que los nudillos guíen el cuchillo"),
                     T("Holding the knife like a pencil", "Sostener el cuchillo como un lápiz"),
                     T("Gripping the blade with your hand", "Agarrar la hoja con la mano"), T("Cutting toward your body", "Cortar hacia tu cuerpo")], "answer": 0},
        {"cert": "S3.2", "q": T("How should you carry a knife?", "¿Cómo debes llevar un cuchillo?"),
         "choices": [T("At your side with the point down", "A tu costado con la punta hacia abajo"), T("Over your shoulder", "Sobre tu hombro"),
                     T("With the point up in front of you", "Con la punta hacia arriba delante de ti"), T("In your pocket", "En tu bolsillo")], "answer": 0},
        {"cert": "S3.2", "q": T("What should you do if a knife falls?", "¿Qué debes hacer si se cae un cuchillo?"),
         "choices": [T("Step back and let it fall", "Dar un paso atrás y dejar que caiga"), T("Try to catch it", "Intentar atraparlo"),
                     T("Kick it away", "Patearlo lejos"), T("Pick it up by the blade", "Recogerlo por la hoja")], "answer": 0},
        {"cert": "S3.3", "q": T("Which cut makes thin matchstick strips?", "¿Qué corte produce tiras delgadas como palitos de fósforo?"),
         "choices": [T("Julienne", "Juliana"), T("Mince", "Picar finamente"), T("Dice", "Cortar en cubos"), T("Slice", "Rebanar")], "answer": 0},
        {"cert": "S3.3", "q": T("Which cut makes very tiny pieces?", "¿Qué corte produce pedazos muy pequeños?"),
         "choices": [T("Mince", "Picar finamente"), T("Slice", "Rebanar"), T("Julienne", "Juliana"), T("Halve", "Partir por la mitad")], "answer": 0},
        {"cert": "S3.2", "q": T("What should you do first for a small grease fire in a pan?", "¿Qué debes hacer primero ante un fuego pequeño de grasa en una sartén?"),
         "choices": [T("Turn off the heat and cover it with a lid", "Apagar el calor y taparlo con una tapa"), T("Pour water on it", "Echarle agua"),
                     T("Carry the pan to the sink", "Llevar la sartén al fregadero"), T("Fan the flames", "Abanicar las llamas")], "answer": 0},
        {"cert": "S3.2", "q": T("Which way should pot handles point on the stove?", "¿Hacia dónde deben apuntar los mangos de las ollas en la estufa?"),
         "choices": [T("Inward, over the stove", "Hacia adentro, sobre la estufa"), T("Out over the edge", "Hacia afuera, sobre el borde"),
                     T("Toward the nearest person", "Hacia la persona más cercana"), T("It does not matter", "No importa")], "answer": 0},
        {"cert": "S3.2", "q": T("What must you do before you start a blender?", "¿Qué debes hacer antes de encender una licuadora?"),
         "choices": [T("Put the lid on firmly", "Poner la tapa firmemente"), T("Put a spoon in to stir", "Meter una cuchara para revolver"),
                     T("Remove the lid for steam", "Quitar la tapa para el vapor"), T("Fill it to the very top", "Llenarla hasta el borde")], "answer": 0},
        {"cert": "S3.2", "q": T("What should you do before cleaning a blender's blades?", "¿Qué debes hacer antes de limpiar las cuchillas de una licuadora?"),
         "choices": [T("Unplug it", "Desconectarla"), T("Run it dry", "Encenderla en seco"), T("Wash the motor base in the sink", "Lavar la base del motor en el fregadero"), T("Nothing", "Nada")], "answer": 0},
        {"cert": "S3.1", "q": T("What internal temperature should reheated foods like quesadillas reach?", "¿Qué temperatura interna deben alcanzar los alimentos recalentados como las quesadillas?"),
         "choices": [T("165°F", "165 °F"), T("100°F", "100 °F"), T("125°F", "125 °F"), T("145°F", "145 °F")], "answer": 0},
        {"cert": "S3.2", "q": T("How should you wash a sharp knife?", "¿Cómo debes lavar un cuchillo afilado?"),
         "choices": [T("By hand, one at a time, blade facing away", "A mano, uno por uno, con la hoja alejada de ti"), T("In a sink of soapy water with other dishes", "En un fregadero de agua jabonosa con otros platos"),
                     T("In the dishwasher with the blade up", "En el lavavajillas con la hoja hacia arriba"), T("Do not wash it", "No lavarlo")], "answer": 0},
    ],

    "practical": {
        "title": T("Unit 3 Practical: Safe Tools and Cuts", "Práctica de la Unidad 3: Herramientas y cortes seguros"),
        "scale": "0-10 (cert performance scale). Target average: 8 or higher.",
        "criteria": [
            {"cert": "S3.2", "name": T("Knife safety and technique", "Seguridad y técnica con el cuchillo"),
             "high": T("Claw grip, stable board, safe carrying, and correct cuts every time.", "Posición de garra, tabla estable, transporte seguro y cortes correctos siempre."),
             "mid": T("Mostly safe; one reminder needed.", "Casi siempre seguro; se necesitó un recordatorio."),
             "low": T("Unsafe habits or repeated redirection.", "Hábitos inseguros o redirección repetida.")},
            {"cert": "S3.2", "name": T("Appliance and stove safety", "Seguridad con aparatos y estufa"),
             "high": T("Handles inward, dry mitts, lid on blender, unplugs before cleaning.", "Mangos hacia adentro, guantes secos, tapa en la licuadora, desconecta antes de limpiar."),
             "mid": T("Minor lapses corrected quickly.", "Pequeños descuidos corregidos rápido."),
             "low": T("Repeated unsafe use.", "Uso inseguro repetido.")},
            {"cert": "S3.3", "name": T("Method and food quality", "Método y calidad de los alimentos"),
             "high": T("Food is evenly cut, properly cooked or blended, and meets the recipe's temperature.", "Los alimentos están cortados parejos, bien cocidos o licuados y cumplen la temperatura de la receta."),
             "mid": T("Acceptable; some uneven cuts.", "Aceptable; algunos cortes irregulares."),
             "low": T("Undercooked or very uneven.", "Poco cocido o muy irregular.")},
            {"cert": "S3.1", "name": T("Clean, cook, and station check", "Limpiar, cocinar y revisión de la estación"),
             "high": T("Uses the thermometer correctly; station passes the first time.", "Usa bien el termómetro; la estación aprueba a la primera."),
             "mid": T("Minor corrections needed.", "Se necesitan correcciones menores."),
             "low": T("Skips thermometer or station fails.", "Omite el termómetro o la estación no aprueba.")},
        ],
    },
}
