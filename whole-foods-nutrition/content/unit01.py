"""Unit 1 — Lab Procedures and Safety Foundations (Days 1-4, 1 lab).

Cert alignment: S3.1 (foodborne illness; clean, separate, cook, chill), S3.2 (safe equipment use).
Spanish text is machine-assisted and has NOT had a fluent human review (see README).
"""
from .common import T

UNIT = {
    "number": 1,
    "slug": "lab-procedures",
    "title": T("Lab Procedures and Safety Foundations", "Procedimientos de laboratorio y bases de seguridad"),
    "days": "1-4",
    "labs": 1,
    "cert": ["S3.1", "S3.2"],
    "essential_question": T(
        "What habits keep everyone safe and healthy when we cook together?",
        "¿Qué hábitos mantienen a todos seguros y sanos cuando cocinamos juntos?"),
    "overview": T(
        "Before we cook, we learn how a professional kitchen stays safe. You will learn the course rules, "
        "how to wash your hands and clean a station, how germs spread, and the four steps that prevent foodborne "
        "illness: clean, separate, cook, and chill. On day 4 your group runs its first lab.",
        "Antes de cocinar, aprendemos cómo se mantiene segura una cocina profesional. Aprenderás las reglas del "
        "curso, cómo lavarte las manos y limpiar una estación, cómo se propagan los gérmenes y los cuatro pasos "
        "que previenen las enfermedades transmitidas por alimentos: limpiar, separar, cocinar y enfriar. En el "
        "día 4, tu grupo hace su primer laboratorio."),

    "vocab_bank": [
        {"term": T("Foodborne illness", "Enfermedad transmitida por alimentos"),
         "definition": T("Sickness caused by eating food that contains harmful germs or substances.",
                         "Enfermedad causada por comer alimentos que contienen gérmenes o sustancias dañinas.")},
        {"term": T("Pathogen", "Patógeno"),
         "definition": T("A germ, such as a bacterium or virus, that can make people sick.",
                         "Un germen, como una bacteria o un virus, que puede enfermar a las personas.")},
        {"term": T("Cross-contamination", "Contaminación cruzada"),
         "definition": T("The spread of germs from one food, surface, or hand to another.",
                         "La propagación de gérmenes de un alimento, superficie o mano a otro.")},
        {"term": T("Sanitize", "Desinfectar"),
         "definition": T("To reduce germs on a clean surface to a safe level.",
                         "Reducir los gérmenes de una superficie limpia hasta un nivel seguro.")},
        {"term": T("Temperature danger zone", "Zona de peligro de temperatura"),
         "definition": T("The range from 40°F to 140°F where bacteria grow fastest.",
                         "El rango de 40 °F a 140 °F donde las bacterias crecen más rápido.")},
        {"term": T("Internal temperature", "Temperatura interna"),
         "definition": T("The temperature at the center of the thickest part of a food.",
                         "La temperatura en el centro de la parte más gruesa de un alimento.")},
        {"term": T("Mise en place", "Mise en place (todo en su lugar)"),
         "definition": T("A French phrase meaning to gather and prepare everything before you start cooking.",
                         "Frase francesa que significa reunir y preparar todo antes de empezar a cocinar.")},
        {"term": T("Work plan", "Plan de trabajo"),
         "definition": T("A list of who does which job, and in what order, to finish a recipe on time.",
                         "Una lista de quién hace cada tarea, y en qué orden, para terminar una receta a tiempo.")},
    ],

    "reading": {
        "title": T("Why Kitchens Have Rules", "Por qué las cocinas tienen reglas"),
        "body": [
            T("Every year, about 48 million people in the United States get sick from something they ate, "
              "according to estimates from the Centers for Disease Control and Prevention (CDC). Most recover "
              "in a few days. But some people, such as young children, older adults, pregnant women, and people "
              "with weak immune systems, can become very sick.",
              "Cada año, unos 48 millones de personas en los Estados Unidos se enferman por algo que comieron, "
              "según estimaciones de los Centros para el Control y la Prevención de Enfermedades (CDC). La mayoría "
              "se recupera en unos días. Pero algunas personas, como los niños pequeños, los adultos mayores, las "
              "mujeres embarazadas y las personas con el sistema inmunitario débil, pueden enfermarse gravemente."),
            T("Foodborne illness is caused by pathogens: bacteria, viruses, and parasites. You cannot see, smell, "
              "or taste most of them. Food can look and smell fine and still make you sick. That is why a "
              "professional kitchen does not depend on guessing. It depends on habits that everyone follows every time.",
              "Las enfermedades transmitidas por alimentos son causadas por patógenos: bacterias, virus y parásitos. "
              "No puedes ver, oler ni saborear la mayoría de ellos. Un alimento puede verse y oler bien y aun así "
              "enfermarte. Por eso una cocina profesional no se basa en adivinar. Se basa en hábitos que todos "
              "siguen siempre."),
            T("Food safety experts teach four habits: clean, separate, cook, and chill. Clean means washing hands "
              "and surfaces often. Separate means keeping raw meat, poultry, seafood, and eggs away from foods "
              "that will not be cooked. Cook means heating food to a safe internal temperature. Chill means "
              "putting food in the refrigerator quickly, because bacteria grow fastest between 40°F and 140°F.",
              "Los expertos en seguridad alimentaria enseñan cuatro hábitos: limpiar, separar, cocinar y enfriar. "
              "Limpiar significa lavar las manos y las superficies con frecuencia. Separar significa mantener la "
              "carne cruda, las aves, los mariscos y los huevos lejos de los alimentos que no se van a cocinar. "
              "Cocinar significa calentar los alimentos hasta una temperatura interna segura. Enfriar significa "
              "refrigerar los alimentos rápidamente, porque las bacterias crecen más rápido entre 40 °F y 140 °F."),
            T("A kitchen is also a team. Each person has a job, and the jobs rotate so everyone learns every skill. "
              "When one person skips a step, the whole group is affected. In this class, you will practice these "
              "habits until they become automatic, the same way a restaurant cook or a hospital dietitian does.",
              "Una cocina también es un equipo. Cada persona tiene una tarea, y las tareas rotan para que todos "
              "aprendan todas las habilidades. Cuando una persona se salta un paso, todo el grupo se ve afectado. "
              "En esta clase practicarás estos hábitos hasta que sean automáticos, igual que un cocinero de "
              "restaurante o un dietista de hospital."),
        ],
        "questions": [
            {"q": T("Why can't you tell by looking or smelling whether food is safe?",
                    "¿Por qué no puedes saber con la vista o el olfato si un alimento es seguro?"),
             "answer": T("Most pathogens cannot be seen, smelled, or tasted.",
                         "La mayoría de los patógenos no se pueden ver, oler ni saborear.")},
            {"q": T("Name the four food safety habits.", "Nombra los cuatro hábitos de seguridad alimentaria."),
             "answer": T("Clean, separate, cook, chill.", "Limpiar, separar, cocinar, enfriar.")},
            {"q": T("Which people are at higher risk of becoming very sick from foodborne illness?",
                    "¿Qué personas tienen mayor riesgo de enfermarse gravemente por una enfermedad transmitida por alimentos?"),
             "answer": T("Young children, older adults, pregnant women, people with weak immune systems.",
                         "Niños pequeños, adultos mayores, mujeres embarazadas, personas con el sistema inmunitario débil.")},
            {"q": T("Why do group jobs rotate?", "¿Por qué rotan las tareas del grupo?"),
             "answer": T("So everyone learns every skill.", "Para que todos aprendan todas las habilidades.")},
        ],
        "source_note": "CDC estimate (about 48 million illnesses per year) and the four habits are from CDC and USDA/FDA Partnership for Food Safety Education (Fight BAC!).",
    },

    "lessons": [
        # ------------------------------------------------------------------ DAY 1
        {
            "day": 1, "kind": "lesson",
            "title": T("Welcome to the Kitchen", "Bienvenidos a la cocina"),
            "objectives": [T("I can explain how my grade is built and how to qualify for labs.",
                             "Puedo explicar cómo se calcula mi calificación y cómo calificar para los laboratorios."),
                           T("I can name the four group jobs in the kitchen.",
                             "Puedo nombrar las cuatro tareas del grupo en la cocina."),
                           T("I can find safety equipment in our kitchen.",
                             "Puedo encontrar el equipo de seguridad en nuestra cocina.")],
            "cert": ["S3.2", "S3.4"],
            "vocab": ["Work plan", "Mise en place"],
            "bellringer": T("Think about a time you cooked or helped cook. What went well? What went wrong? Write two sentences.",
                            "Piensa en una vez que cocinaste o ayudaste a cocinar. ¿Qué salió bien? ¿Qué salió mal? Escribe dos oraciones."),
            "instruction": [
                {"heading": T("What this class is", "Qué es esta clase"),
                 "body": T("Whole Foods and Nutrition studies where food comes from, what it does for your body, and how to "
                           "prepare it safely. We learn in the classroom and then practice in the kitchen. About four of every ten "
                           "days are cooking days.",
                           "Alimentos Integrales y Nutrición estudia de dónde viene la comida, qué hace por tu cuerpo y cómo "
                           "prepararla de forma segura. Aprendemos en el salón y luego practicamos en la cocina. Aproximadamente "
                           "cuatro de cada diez días son días de cocina.")},
                {"heading": T("How your grade works", "Cómo funciona tu calificación"),
                 "body": T("Your grade is 80 percent summative work (unit tests, lab performance, projects) and 20 percent "
                           "formative work (bellringers, practice, exit tickets). Unit tests are taken in Quia during Warrior Time. "
                           "You may retake a test one time, within two weeks, if all of the formative work for that unit is done.",
                           "Tu calificación es 80 por ciento trabajo sumativo (exámenes de unidad, desempeño en el laboratorio, "
                           "proyectos) y 20 por ciento trabajo formativo (actividades de inicio, práctica, boletos de salida). "
                           "Los exámenes de unidad se hacen en Quia durante Warrior Time. Puedes repetir un examen una vez, dentro "
                           "de dos semanas, si todo el trabajo formativo de esa unidad está completo.")},
                {"heading": T("Lab rules", "Reglas del laboratorio"),
                 "body": T("You need a C- or better to take part in foods lab. Missed labs must be made up within two weeks "
                           "using the makeup lab sheet in Canvas. Late work is not accepted more than two weeks after the due date.",
                           "Necesitas una C- o más para participar en el laboratorio de cocina. Los laboratorios que faltes deben "
                           "reponerse dentro de dos semanas con la hoja de reposición en Canvas. No se acepta trabajo tarde "
                           "después de dos semanas de la fecha de entrega.")},
                {"heading": T("Four jobs, every lab", "Cuatro tareas, cada laboratorio"),
                 "body": T("Each group has four people and four jobs: Head Chef, Sous Chef, Safety and Sanitation Officer, and "
                           "Supplies and Cleanup Manager. Jobs rotate each lab so everyone practices every skill.",
                           "Cada grupo tiene cuatro personas y cuatro tareas: Jefe de cocina, Ayudante de cocina, Oficial de "
                           "seguridad e higiene y Encargado de materiales y limpieza. Las tareas rotan en cada laboratorio para "
                           "que todos practiquen todas las habilidades.")},
            ],
            "guided": {
                "title": T("Kitchen Safety Walk", "Recorrido de seguridad de la cocina"),
                "steps": [T("Follow your teacher around the kitchen. At each stop, write down what you see and what it is for.",
                            "Sigue a tu maestra por la cocina. En cada parada, anota lo que ves y para qué sirve."),
                          T("Stops: handwashing sink, fire extinguisher, first aid kit, fire blanket or shutoff, emergency exits, "
                            "sanitizer station, knife storage, and the refrigerator.",
                            "Paradas: lavamanos, extintor, botiquín de primeros auxilios, manta o corte de emergencia, salidas de "
                            "emergencia, estación de desinfectante, almacenamiento de cuchillos y refrigerador.")],
            },
            "independent": {
                "kind": "activity",
                "title": T("Safety Scavenger Hunt", "Búsqueda del tesoro de seguridad"),
                "steps": [T("With your group, find each item on the Safety Map and mark where it is on a drawing of the kitchen.",
                            "Con tu grupo, encuentra cada elemento del Mapa de seguridad y márcalo en un dibujo de la cocina."),
                          T("Write the one rule that goes with each item. Example: \"Never use water on a grease fire.\"",
                            "Escribe la regla que corresponde a cada elemento. Ejemplo: \"Nunca uses agua en un fuego de grasa.\""),
                          T("Choose roles for your first lab. Write each person's job on your group card.",
                            "Elige los roles para tu primer laboratorio. Escribe la tarea de cada persona en la tarjeta del grupo.")],
            },
            "exit": [{"q": T("Name two things you need to do to take part in lab.",
                             "Nombra dos cosas que debes hacer para participar en el laboratorio."),
                      "answer": T("Examples: keep a C- or better; wash hands; follow your group job; make up missed labs within two weeks.",
                                  "Ejemplos: mantener una C- o más; lavarse las manos; cumplir con la tarea del grupo; reponer los laboratorios en dos semanas.")},
                     {"q": T("Where is the fire extinguisher?", "¿Dónde está el extintor?"),
                      "answer": T("Teacher fills in your kitchen's location.", "La maestra anota la ubicación en su cocina.")}],
            "teacher": {
                "materials": ["Course syllabus (confirm policies match current syllabus)", "Group cards (8)", "Kitchen map handout",
                              "Clipboards"],
                "notes": ["Confirm every policy on this page matches the current syllabus before using it.",
                          "Do the kitchen walk before students touch any equipment.",
                          "Record student allergies on the group cards; peanut-free kitchen. Check labels on every packaged item."],
            },
        },
        # ------------------------------------------------------------------ DAY 2
        {
            "day": 2, "kind": "lesson",
            "title": T("Clean: Hands and Surfaces", "Limpiar: manos y superficies"),
            "objectives": [T("I can wash my hands correctly.", "Puedo lavarme las manos correctamente."),
                           T("I can list when to wash hands in a kitchen.", "Puedo enumerar cuándo lavarme las manos en una cocina."),
                           T("I can clean and sanitize a work surface in the right order.",
                             "Puedo limpiar y desinfectar una superficie de trabajo en el orden correcto.")],
            "cert": ["S3.1"],
            "vocab": ["Pathogen", "Foodborne illness", "Sanitize"],
            "bellringer": T("List three things you touched today before you got to class. Could any of them carry germs?",
                            "Haz una lista de tres cosas que tocaste hoy antes de llegar a clase. ¿Alguna podría tener gérmenes?"),
            "instruction": [
                {"heading": T("How food makes people sick", "Cómo los alimentos enferman a las personas"),
                 "body": T("Foodborne illness is caused by pathogens. Bacteria such as Salmonella and E. coli, and viruses such as "
                           "norovirus, can get onto food from hands, surfaces, and other food. Symptoms include vomiting, diarrhea, "
                           "stomach cramps, and fever.",
                           "Las enfermedades transmitidas por alimentos son causadas por patógenos. Bacterias como Salmonella y "
                           "E. coli, y virus como el norovirus, pueden llegar a los alimentos desde las manos, las superficies y "
                           "otros alimentos. Los síntomas incluyen vómito, diarrea, cólicos estomacales y fiebre.")},
                {"heading": T("Handwashing in five steps", "Lavado de manos en cinco pasos"),
                 "body": T("1. Wet hands with clean running water. 2. Add soap and lather the backs of hands, between fingers, and under "
                           "nails. 3. Scrub for at least 20 seconds. 4. Rinse well. 5. Dry with a clean paper towel, then use the towel "
                           "to turn off the faucet.",
                           "1. Moja las manos con agua corriente limpia. 2. Agrega jabón y haz espuma en el dorso de las manos, entre "
                           "los dedos y debajo de las uñas. 3. Frota durante al menos 20 segundos. 4. Enjuaga bien. 5. Seca con una "
                           "toalla de papel limpia y úsala para cerrar el grifo.")},
                {"heading": T("When to wash", "Cuándo lavarse"),
                 "body": T("Wash before you start cooking, after using the restroom, after touching your face, hair, or phone, after "
                           "handling raw meat, poultry, seafood, or eggs, after taking out trash, after sneezing or coughing, and any "
                           "time your hands are dirty.",
                           "Lávate antes de empezar a cocinar, después de usar el baño, después de tocarte la cara, el cabello o el "
                           "teléfono, después de manipular carne cruda, aves, mariscos o huevos, después de sacar la basura, después "
                           "de estornudar o toser, y siempre que tus manos estén sucias.")},
                {"heading": T("Clean, then sanitize", "Primero limpiar, luego desinfectar"),
                 "body": T("Cleaning removes dirt and food. Sanitizing reduces germs. Always do them in this order: wash with soap and "
                           "water, rinse, then sanitize. Use the school's approved sanitizer at the strength on its label and let the "
                           "surface air dry.",
                           "Limpiar quita la suciedad y los restos de comida. Desinfectar reduce los gérmenes. Hazlos siempre en este "
                           "orden: lava con agua y jabón, enjuaga y luego desinfecta. Usa el desinfectante aprobado por la escuela en "
                           "la concentración indicada en la etiqueta y deja secar la superficie al aire.")},
                {"heading": T("Personal readiness", "Preparación personal"),
                 "body": T("Tie back long hair, wear a clean apron, remove rings and bracelets, keep nails short and clean, wear "
                           "closed-toe shoes, and cover any cut with a bandage and a glove. If you are sick, tell your teacher "
                           "and do not handle food.",
                           "Recógete el cabello largo, usa un delantal limpio, quítate anillos y pulseras, mantén las uñas cortas y "
                           "limpias, usa zapatos cerrados y cubre cualquier cortada con una curita y un guante. Si estás enfermo, "
                           "avísale a tu maestra y no manipules alimentos.")},
            ],
            "guided": {
                "title": T("Handwashing Practice", "Práctica de lavado de manos"),
                "steps": [T("Watch the demonstration. Your teacher shows the five steps while you follow along with your wet-and-soap "
                            "hands up at your seat (no sink yet).",
                            "Observa la demostración. Tu maestra muestra los cinco pasos mientras sigues con las manos en el aire "
                            "en tu asiento (todavía sin lavamanos)."),
                          T("Hum \"Happy Birthday\" twice, or count to 20, to feel how long 20 seconds is.",
                            "Tararea \"Cumpleaños feliz\" dos veces, o cuenta hasta 20, para sentir cuánto dura 20 segundos."),
                          T("Complete the sequencing card: put the five steps in order.",
                            "Completa la tarjeta de secuencia: pon los cinco pasos en orden.")],
            },
            "independent": {
                "kind": "activity",
                "title": T("Wash It, Clean It, Sanitize It", "Lávalo, límpialo, desinféctalo"),
                "steps": [T("Each person washes hands at the sink for 20 seconds while a partner times it and checks the five steps.",
                            "Cada persona se lava las manos en el lavamanos durante 20 segundos mientras un compañero cronometra y revisa los cinco pasos."),
                          T("At your station, wash a section of counter with soap and water, rinse, then sanitize. Your Safety Officer "
                            "checks the order using the station checklist.",
                            "En tu estación, lava una parte del mostrador con agua y jabón, enjuaga y luego desinfecta. Tu Oficial de seguridad "
                            "revisa el orden con la lista de verificación."),
                          T("Fill in the \"When do I wash?\" chart with at least six times.",
                            "Completa la tabla \"¿Cuándo me lavo?\" con al menos seis momentos.")],
            },
            "exit": [{"q": T("Put in order: sanitize, rinse, wash with soap and water.",
                             "Pon en orden: desinfectar, enjuagar, lavar con agua y jabón."),
                      "answer": T("Wash with soap and water, rinse, sanitize.", "Lavar con agua y jabón, enjuagar, desinfectar.")},
                     {"q": T("Name two times you must wash your hands when cooking.",
                             "Nombra dos momentos en que debes lavarte las manos al cocinar."),
                      "answer": T("Any two: before cooking, after the restroom, after touching face/hair/phone, after raw meat or eggs, after trash.",
                                  "Dos cualesquiera: antes de cocinar, después del baño, después de tocarte la cara/cabello/teléfono, después de carne cruda o huevos, después de la basura.")}],
            "teacher": {
                "materials": ["Sinks, soap, paper towels", "School-approved sanitizer and test strips", "Timer",
                              "Handwashing sequence cards", "Station checklist"],
                "notes": ["Optional glitter or lotion demo: put a little lotion mixed with glitter on one student's hands, have them shake hands "
                          "with others, then show how it spread.",
                          "Use the sanitizer and concentration your district approves. Check with test strips; do not state a ppm here unless it matches your product label.",
                          "Never allow students to mix cleaning chemicals."],
            },
        },
        # ------------------------------------------------------------------ DAY 3
        {
            "day": 3, "kind": "lesson",
            "title": T("Separate, Cook, Chill", "Separar, cocinar, enfriar"),
            "objectives": [T("I can prevent cross-contamination.", "Puedo prevenir la contaminación cruzada."),
                           T("I can state the temperature danger zone and safe cooking temperatures.",
                             "Puedo indicar la zona de peligro de temperatura y las temperaturas seguras de cocción."),
                           T("I can explain how to chill and store food safely.",
                             "Puedo explicar cómo enfriar y almacenar los alimentos de forma segura.")],
            "cert": ["S3.1"],
            "vocab": ["Cross-contamination", "Temperature danger zone", "Internal temperature"],
            "bellringer": T("A cook cuts raw chicken on a board and then slices tomatoes on the same board without washing it. What could go wrong?",
                            "Un cocinero corta pollo crudo en una tabla y luego rebana tomates en la misma tabla sin lavarla. ¿Qué podría salir mal?"),
            "instruction": [
                {"heading": T("Separate", "Separar"),
                 "body": T("Cross-contamination is when germs move from one place to another. Prevent it by using separate cutting boards and "
                           "utensils for raw meat, poultry, seafood, and eggs; by storing raw foods on the lowest refrigerator shelf so "
                           "juices cannot drip onto other foods; and by washing hands and tools between tasks.",
                           "La contaminación cruzada ocurre cuando los gérmenes pasan de un lugar a otro. Se previene usando tablas de "
                           "cortar y utensilios separados para carne cruda, aves, mariscos y huevos; guardando los alimentos crudos en "
                           "el estante más bajo del refrigerador para que los jugos no goteen sobre otros alimentos; y lavando las "
                           "manos y las herramientas entre tareas.")},
                {"heading": T("Cook", "Cocinar"),
                 "body": T("You cannot tell if food is safe by color. Use a clean food thermometer in the thickest part. USDA safe "
                           "internal temperatures: poultry 165°F; ground meats 160°F; beef, pork, lamb, and fish 145°F (with a "
                           "3-minute rest for beef, pork, and lamb); egg dishes 160°F; leftovers 165°F.",
                           "No puedes saber si un alimento es seguro por su color. Usa un termómetro limpio en la parte más gruesa. "
                           "Temperaturas internas seguras del USDA: aves 165 °F; carnes molidas 160 °F; res, cerdo, cordero y pescado "
                           "145 °F (con 3 minutos de reposo para res, cerdo y cordero); platos con huevo 160 °F; sobras 165 °F.")},
                {"heading": T("Chill", "Enfriar"),
                 "body": T("Bacteria grow fastest in the temperature danger zone, 40°F to 140°F. Keep the refrigerator at 40°F or below. "
                           "Refrigerate perishable food within 2 hours (within 1 hour if the room is above 90°F). Thaw food in the "
                           "refrigerator, in cold water, or in the microwave, not on the counter.",
                           "Las bacterias crecen más rápido en la zona de peligro de temperatura, de 40 °F a 140 °F. Mantén el "
                           "refrigerador a 40 °F o menos. Refrigera los alimentos perecederos dentro de 2 horas (dentro de 1 hora si "
                           "la temperatura ambiente pasa de 90 °F). Descongela en el refrigerador, en agua fría o en el microondas, "
                           "no sobre el mostrador.")},
            ],
            "guided": {
                "title": T("Spot the Mistakes", "Encuentra los errores"),
                "steps": [T("Read the kitchen scene card as a class. There are five safety mistakes in it.",
                            "Lean juntos la tarjeta de la escena de la cocina. Hay cinco errores de seguridad."),
                          T("With a partner, circle each mistake and write which habit it breaks: clean, separate, cook, or chill.",
                            "Con un compañero, encierra en un círculo cada error y escribe qué hábito rompe: limpiar, separar, cocinar o enfriar."),
                          T("Write the fix next to each mistake.", "Escribe la solución junto a cada error.")],
            },
            "independent": {
                "kind": "activity",
                "title": T("Danger Zone Detectives", "Detectives de la zona de peligro"),
                "steps": [T("Sort the 12 food cards by safe internal temperature using the chart.",
                            "Clasifica las 12 tarjetas de alimentos por temperatura interna segura con la tabla."),
                          T("Answer the three scenarios: a lunch left in a backpack, a casserole left on the counter, and thawing a "
                            "turkey. Decide what is safe and why.",
                            "Responde los tres casos: un almuerzo olvidado en una mochila, una cazuela dejada en el mostrador y "
                            "descongelar un pavo. Decide qué es seguro y por qué."),
                          T("Make a one-page \"Clean, Separate, Cook, Chill\" poster for your kitchen station. Use words and symbols, not color alone.",
                            "Haz un cartel de una página \"Limpiar, separar, cocinar, enfriar\" para tu estación. Usa palabras y símbolos, no solo color.")],
            },
            "exit": [{"q": T("Name the temperature danger zone.", "Nombra la zona de peligro de temperatura."),
                      "answer": T("40°F to 140°F.", "De 40 °F a 140 °F.")},
                     {"q": T("What is the safe internal temperature for chicken?", "¿Cuál es la temperatura interna segura para el pollo?"),
                      "answer": T("165°F.", "165 °F.")},
                     {"q": T("Name one way to prevent cross-contamination.", "Nombra una forma de prevenir la contaminación cruzada."),
                      "answer": T("Separate cutting boards; store raw foods on the bottom shelf; wash hands and tools between tasks.",
                                  "Tablas separadas; guardar lo crudo en el estante inferior; lavar manos y herramientas entre tareas.")}],
            "teacher": {
                "materials": ["Scene card (5 planted errors)", "Food temperature cards", "Poster paper and markers",
                              "Food thermometer for demo"],
                "notes": ["Temperatures are USDA FSIS safe minimum internal temperatures; confirm before printing.",
                          "Scene card errors suggested: no handwashing before cooking; same board for raw chicken and salad; "
                          "chicken left on the counter for 3 hours; leftovers stored warm in a deep pot; thermometer not used.",
                          "Do a live thermometer demo in water of different temperatures if you have time."],
            },
        },
        # ------------------------------------------------------------------ DAY 4 (LAB)
        {
            "day": 4, "kind": "lab",
            "title": T("Lab 1: Fruit and Yogurt Parfait", "Laboratorio 1: Parfait de fruta y yogur"),
            "objectives": [T("I can work with my group using a work plan and assigned jobs.",
                             "Puedo trabajar con mi grupo usando un plan de trabajo y tareas asignadas."),
                           T("I can apply clean, separate, and chill while I prepare food.",
                             "Puedo aplicar limpiar, separar y enfriar mientras preparo alimentos."),
                           T("I can measure ingredients accurately.", "Puedo medir ingredientes con exactitud.")],
            "cert": ["S3.1", "S3.2", "S3.3", "S3.4"],
            "vocab": ["Mise en place", "Work plan"],
            "bellringer": T("Read today's recipe. Which job do you have? Write the first thing you will do.",
                            "Lee la receta de hoy. ¿Qué tarea tienes? Escribe lo primero que harás."),
            "instruction": [
                {"heading": T("Lab brief", "Introducción del laboratorio"),
                 "body": T("Today's safety focus: clean and chill. Wash your hands before you touch food. Keep yogurt in the refrigerator "
                           "until it is time to assemble. Check every package label for peanuts. Fill in your work plan before you start.",
                           "Enfoque de seguridad de hoy: limpiar y enfriar. Lávate las manos antes de tocar los alimentos. Mantén el "
                           "yogur en el refrigerador hasta el momento de armar. Revisa la etiqueta de cada paquete para ver si tiene "
                           "cacahuate. Completa tu plan de trabajo antes de empezar.")},
            ],
            "guided": {
                "title": T("Group Work Plan", "Plan de trabajo del grupo"),
                "steps": [T("Write who does each step and how many minutes it will take.", "Escribe quién hace cada paso y cuántos minutos tomará."),
                          T("Check that all 28 minutes of cooking time are planned.", "Verifica que se planifiquen los 28 minutos de cocina.")],
            },
            "independent": {
                "kind": "lab",
                "recipe": "parfait",
                "title": T("Cook: Fruit and Yogurt Parfait", "Cocinar: Parfait de fruta y yogur"),
                "steps": [T("Follow the recipe card. Your Safety Officer signs off each safety checkpoint.",
                            "Sigue la tarjeta de receta. Tu Oficial de seguridad firma cada punto de control de seguridad."),
                          T("When finished, eat together at your station, then complete cleanup. Your Cleanup Manager calls the station check.",
                            "Al terminar, coman juntos en su estación y luego completen la limpieza. Tu Encargado de limpieza llama a la revisión de la estación.")],
            },
            "exit": [{"q": T("Which of clean, separate, cook, or chill did your group do best? Give one example.",
                             "¿Cuál de limpiar, separar, cocinar o enfriar hizo mejor tu grupo? Da un ejemplo."),
                      "answer": T("Answers vary; look for a specific action.", "Las respuestas varían; busca una acción específica.")},
                     {"q": T("What is one thing your group will do differently next lab?",
                             "¿Qué hará tu grupo de manera diferente en el próximo laboratorio?"),
                      "answer": T("Answers vary.", "Las respuestas varían.")}],
            "teacher": {
                "materials": ["Recipe cards (1 per group)", "Ingredients (see recipe)", "Station checklist", "Lab rubric (Unit 1 practical)"],
                "notes": ["Peanut-free kitchen: read every label (granola especially). If a student has a milk allergy, use a dairy-free yogurt.",
                          "Use the Unit 1 practical rubric to score hands, sanitizing, separation, and teamwork.",
                          "Estimated cost: about $3 per group, $24 for 8 groups. Verify against current prices."],
            },
        },
    ],

    "recipes": {
        "parfait": {
            "title": T("Fruit and Yogurt Parfait", "Parfait de fruta y yogur"),
            "serves": 4, "active_minutes": 20,
            "allergens": T("Contains milk. Granola may contain wheat, oats, soy, or tree nuts: read the label. The label must say it is peanut-free.",
                           "Contiene leche. La granola puede contener trigo, avena, soya o nueces de árbol: lee la etiqueta. La etiqueta debe indicar que no tiene cacahuate."),
            "equipment": [T("4 clear cups or bowls", "4 vasos o tazones transparentes"),
                          T("Dry measuring cups", "Tazas medidoras para ingredientes secos"),
                          T("Liquid measuring cup", "Taza medidora para líquidos"),
                          T("Cutting board and table knife", "Tabla de cortar y cuchillo de mesa"),
                          T("Colander", "Colador"), T("Spoons", "Cucharas"), T("Paper towels", "Toallas de papel")],
            "ingredients": [
                {"qty": 2, "unit": T("cups", "tazas"), "item": T("plain or vanilla yogurt (kept cold)", "yogur natural o de vainilla (mantenido frío)")},
                {"qty": 1, "unit": T("cup", "taza"), "item": T("peanut-free granola", "granola sin cacahuate")},
                {"qty": 2, "unit": T("medium", "medianos"), "item": T("bananas", "plátanos")},
                {"qty": 1, "unit": T("cup", "taza"), "item": T("berries, fresh or thawed frozen", "frutos rojos, frescos o congelados descongelados")},
            ],
            "steps": [
                {"text": T("Wash your hands for 20 seconds. Tie back hair and put on an apron.",
                           "Lávate las manos durante 20 segundos. Recógete el cabello y ponte un delantal."),
                 "checkpoint": T("CLEAN: Safety Officer checks that everyone washed.", "LIMPIAR: el Oficial de seguridad verifica que todos se lavaron.")},
                {"text": T("Wash the counter with soap and water, rinse, then sanitize. Let it air dry.",
                           "Lava el mostrador con agua y jabón, enjuaga y luego desinfecta. Déjalo secar al aire."),
                 "checkpoint": T("CLEAN: Safety Officer checks the order.", "LIMPIAR: el Oficial de seguridad verifica el orden.")},
                {"text": T("Gather your tools. Read the label on the granola and yogurt. Fill in your work plan.",
                           "Reúne tus herramientas. Lee la etiqueta de la granola y del yogur. Completa tu plan de trabajo."),
                 "checkpoint": T("ALLERGY: Confirm every label says peanut-free.", "ALERGIA: confirma que cada etiqueta dice sin cacahuate.")},
                {"text": T("Rinse the berries in the colander under cool running water. Pat dry with a paper towel.",
                           "Enjuaga los frutos rojos en el colador con agua fría corriente. Sécalos con una toalla de papel."),
                 "checkpoint": None},
                {"text": T("Peel the bananas and slice them with the table knife on the cutting board. Wash your hands again.",
                           "Pela los plátanos y rebánalos con el cuchillo de mesa sobre la tabla. Lávate las manos de nuevo."),
                 "checkpoint": T("CLEAN: Rinse hands after handling fruit and before touching yogurt.", "LIMPIAR: enjuágate las manos después de la fruta y antes del yogur.")},
                {"text": T("Take the yogurt out of the refrigerator only now. Measure 1/4 cup yogurt into each cup.",
                           "Saca el yogur del refrigerador solo ahora. Mide 1/4 de taza de yogur en cada vaso."),
                 "checkpoint": T("CHILL: Yogurt stays cold until this step.", "ENFRIAR: el yogur permanece frío hasta este paso.")},
                {"text": T("Add a layer of banana and berries, then 2 tablespoons of granola. Repeat the layers once more.",
                           "Agrega una capa de plátano y frutos rojos, luego 2 cucharadas de granola. Repite las capas una vez más."),
                 "checkpoint": None},
                {"text": T("Eat together. Put leftover yogurt back in the refrigerator right away.",
                           "Coman juntos. Devuelve el yogur sobrante al refrigerador de inmediato."),
                 "checkpoint": T("CHILL: Leftovers go back in the refrigerator within 2 hours.", "ENFRIAR: las sobras vuelven al refrigerador dentro de 2 horas.")},
                {"text": T("Wash dishes, sanitize the counter, return equipment, and call for the station check.",
                           "Lava los platos, desinfecta el mostrador, devuelve el equipo y pide la revisión de la estación."),
                 "checkpoint": T("CLEAN: Cleanup Manager signs the station check.", "LIMPIAR: el Encargado de limpieza firma la revisión de la estación.")},
            ],
            "cost_per_group": "$3.00 (estimate)",
        },
    },

    "quiz": [
        {"cert": "S3.1", "q": T("What is a pathogen?", "¿Qué es un patógeno?"),
         "choices": [T("A germ that can make people sick", "Un germen que puede enfermar a las personas"),
                     T("A type of cooking pan", "Un tipo de sartén"),
                     T("A safe food temperature", "Una temperatura segura de los alimentos"),
                     T("A cleaning chemical", "Un producto de limpieza")], "answer": 0},
        {"cert": "S3.1", "q": T("What are the four food safety habits?", "¿Cuáles son los cuatro hábitos de seguridad alimentaria?"),
         "choices": [T("Clean, separate, cook, chill", "Limpiar, separar, cocinar, enfriar"),
                     T("Wash, mix, bake, serve", "Lavar, mezclar, hornear, servir"),
                     T("Measure, cut, season, taste", "Medir, cortar, sazonar, probar"),
                     T("Buy, store, cook, eat", "Comprar, guardar, cocinar, comer")], "answer": 0},
        {"cert": "S3.1", "q": T("How long should you scrub your hands with soap?", "¿Cuánto tiempo debes frotarte las manos con jabón?"),
         "choices": [T("5 seconds", "5 segundos"), T("10 seconds", "10 segundos"),
                     T("At least 20 seconds", "Al menos 20 segundos"), T("2 minutes", "2 minutos")], "answer": 2},
        {"cert": "S3.1", "q": T("What is the correct order for cleaning a counter?", "¿Cuál es el orden correcto para limpiar un mostrador?"),
         "choices": [T("Sanitize, rinse, wash", "Desinfectar, enjuagar, lavar"),
                     T("Wash with soap and water, rinse, sanitize", "Lavar con agua y jabón, enjuagar, desinfectar"),
                     T("Rinse, sanitize, wash", "Enjuagar, desinfectar, lavar"),
                     T("Sanitize only", "Solo desinfectar")], "answer": 1},
        {"cert": "S3.1", "q": T("Which action is cross-contamination?", "¿Qué acción es contaminación cruzada?"),
         "choices": [T("Cutting raw chicken and then lettuce on the same unwashed board", "Cortar pollo crudo y luego lechuga en la misma tabla sin lavar"),
                     T("Washing hands before cooking", "Lavarse las manos antes de cocinar"),
                     T("Chilling leftovers quickly", "Enfriar rápidamente las sobras"),
                     T("Using a food thermometer", "Usar un termómetro de alimentos")], "answer": 0},
        {"cert": "S3.1", "q": T("What is the temperature danger zone?", "¿Cuál es la zona de peligro de temperatura?"),
         "choices": [T("0°F to 32°F", "0 °F a 32 °F"), T("40°F to 140°F", "40 °F a 140 °F"),
                     T("140°F to 212°F", "140 °F a 212 °F"), T("70°F to 100°F", "70 °F a 100 °F")], "answer": 1},
        {"cert": "S3.1", "q": T("What is the safe internal temperature for poultry?", "¿Cuál es la temperatura interna segura para las aves?"),
         "choices": [T("145°F", "145 °F"), T("155°F", "155 °F"), T("165°F", "165 °F"), T("185°F", "185 °F")], "answer": 2},
        {"cert": "S3.1", "q": T("Where should raw meat be stored in the refrigerator?", "¿Dónde debe guardarse la carne cruda en el refrigerador?"),
         "choices": [T("On the top shelf", "En el estante superior"), T("On the lowest shelf", "En el estante más bajo"),
                     T("Next to fresh fruit", "Junto a la fruta fresca"), T("On the door", "En la puerta")], "answer": 1},
        {"cert": "S3.1", "q": T("Within how many hours should perishable food be refrigerated (normal room temperature)?",
                                "¿Dentro de cuántas horas deben refrigerarse los alimentos perecederos (temperatura ambiente normal)?"),
         "choices": [T("1 hour", "1 hora"), T("2 hours", "2 horas"), T("4 hours", "4 horas"), T("8 hours", "8 horas")], "answer": 1},
        {"cert": "S3.1", "q": T("Why should you use a thermometer instead of color to check meat?",
                                "¿Por qué debes usar un termómetro en lugar del color para revisar la carne?"),
         "choices": [T("Color does not show whether germs are destroyed", "El color no muestra si los gérmenes fueron destruidos"),
                     T("Thermometers make food taste better", "Los termómetros mejoran el sabor"),
                     T("Meat is always the same color", "La carne siempre tiene el mismo color"),
                     T("It is faster to guess", "Es más rápido adivinar")], "answer": 0},
        {"cert": "S3.4", "q": T("What does a work plan include?", "¿Qué incluye un plan de trabajo?"),
         "choices": [T("Who does each job and in what order", "Quién hace cada tarea y en qué orden"),
                     T("Only the recipe name", "Solo el nombre de la receta"),
                     T("The grocery receipt", "El recibo del supermercado"),
                     T("The grade scale", "La escala de calificaciones")], "answer": 0},
        {"cert": "S3.2", "q": T("What should you do if you cut yourself in the kitchen?",
                                "¿Qué debes hacer si te cortas en la cocina?"),
         "choices": [T("Keep working and ignore it", "Seguir trabajando e ignorarlo"),
                     T("Tell your teacher, wash the cut, and cover it before returning to food work",
                       "Decirle a tu maestra, lavar la cortada y cubrirla antes de volver a trabajar con alimentos"),
                     T("Wipe it on your apron", "Limpiarla con el delantal"),
                     T("Put a bandage over it and keep handling food without a glove",
                       "Ponerse una curita y seguir manipulando alimentos sin guante")], "answer": 1},
    ],

    "practical": {
        "title": T("Unit 1 Practical: Safe Kitchen Habits", "Práctica de la Unidad 1: Hábitos de cocina segura"),
        "scale": "0-10 (cert performance scale). Target average: 8 or higher.",
        "criteria": [
            {"cert": "S3.1", "name": T("Clean: hands and surfaces", "Limpiar: manos y superficies"),
             "high": T("Washes 20 seconds at every required time; cleans, rinses, then sanitizes in order.",
                       "Se lava 20 segundos en todos los momentos requeridos; limpia, enjuaga y luego desinfecta en orden."),
             "mid": T("Washes at most required times; sometimes skips a step.", "Se lava en la mayoría de los momentos requeridos; a veces omite un paso."),
             "low": T("Washes rarely or out of order.", "Se lava rara vez o en desorden.")},
            {"cert": "S3.1", "name": T("Separate and chill", "Separar y enfriar"),
             "high": T("Keeps foods separate and cold; returns food to the refrigerator on time.",
                       "Mantiene los alimentos separados y fríos; devuelve los alimentos al refrigerador a tiempo."),
             "mid": T("Mostly separate and cold; one lapse.", "Casi siempre separados y fríos; un descuido."),
             "low": T("Foods mixed or left out.", "Alimentos mezclados o dejados afuera.")},
            {"cert": "S3.4", "name": T("Teamwork and work plan", "Trabajo en equipo y plan de trabajo"),
             "high": T("Does the assigned job, helps others, finishes on time.", "Hace su tarea asignada, ayuda a otros y termina a tiempo."),
             "mid": T("Does the assigned job with reminders.", "Hace su tarea con recordatorios."),
             "low": T("Needs frequent redirection.", "Necesita redirección frecuente.")},
            {"cert": "S3.2", "name": T("Equipment and cleanup", "Equipo y limpieza"),
             "high": T("Uses tools correctly; station passes inspection the first time.", "Usa las herramientas correctamente; la estación aprueba la inspección a la primera."),
             "mid": T("Minor corrections needed.", "Se necesitan correcciones menores."),
             "low": T("Station fails inspection.", "La estación no aprueba la inspección.")},
        ],
    },
}
