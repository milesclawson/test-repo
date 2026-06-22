// Language Quiz Game — Unit 5
// Ojibwe words from MIIN (miinojibwe.org), Dakota from Dakhota.org
(function() {
  const words = [
    { word: 'Boozhoo',        lang: 'Ojibwe (MIIN)',    meaning: 'Hello / Greetings',          distractors: ['Thank you', 'Goodbye', 'Water'] },
    { word: 'Miigwech',       lang: 'Ojibwe (MIIN)',    meaning: 'Thank you',                  distractors: ['Hello', 'Run!', 'Eagle'] },
    { word: 'Aaniish',        lang: 'Ojibwe (MIIN)',    meaning: 'How are you? / What\'s up?', distractors: ['Goodbye', 'Thank you', 'Winter'] },
    { word: 'Manoomin',       lang: 'Ojibwe (MIIN)',    meaning: 'Wild rice',                  distractors: ['Maple syrup', 'Lake', 'Eagle'] },
    { word: 'Zaaga\'igan',    lang: 'Ojibwe (MIIN)',    meaning: 'Lake',                       distractors: ['River', 'Winter', 'Wild rice'] },
    { word: 'Biboon',         lang: 'Ojibwe (MIIN)',    meaning: 'Winter',                     distractors: ['Spring', 'Summer', 'Fall'] },
    { word: 'Nokomis',        lang: 'Ojibwe (MIIN)',    meaning: 'Grandmother',                distractors: ['Grandfather', 'Sister', 'Friend'] },
    { word: 'Jiimaan',        lang: 'Ojibwe (MIIN)',    meaning: 'Canoe / Boat',               distractors: ['Fish', 'Paddle', 'River'] },
    { word: 'Awenen giin?',   lang: 'Ojibwe (MIIN)',    meaning: 'Who are you?',               distractors: ['Where are you?', 'How old are you?', 'What is your name?'] },
    { word: 'Indizhinikaaz',  lang: 'Ojibwe (MIIN)',    meaning: 'My name is...',              distractors: ['I live at...', 'I am...', 'My family is...'] },
    { word: 'Pidamayaye',     lang: 'Dakota (Dakhota.org)', meaning: 'Thank you',              distractors: ['Hello', 'Goodbye', 'Water'] },
    { word: 'Mní',            lang: 'Dakota (Dakhota.org)', meaning: 'Water',                  distractors: ['Land', 'River', 'Lake'] },
    { word: 'Uŋčí',           lang: 'Dakota (Dakhota.org)', meaning: 'Grandmother',            distractors: ['Grandfather', 'Mother', 'Aunt'] },
    { word: 'Makoce',         lang: 'Dakota (Dakhota.org)', meaning: 'Land / Earth / Homeland',distractors: ['Water', 'Sky', 'Animal'] },
    { word: 'Wóčhaŋtognake',  lang: 'Dakota (Dakhota.org)', meaning: 'Generosity / Open-heartedness', distractors: ['Strength', 'Speed', 'Silence'] },
    { word: 'Čhaŋtéčhiŋza',  lang: 'Dakota (Dakhota.org)', meaning: 'Brave / Strong-hearted', distractors: ['Fast', 'Quiet', 'Generous'] },
    { word: 'Psin',           lang: 'Dakota (Dakhota.org)', meaning: 'Wild rice',              distractors: ['Corn', 'Lake', 'Water'] },
    { word: 'Ziigwan',        lang: 'Ojibwe (MIIN)',    meaning: 'Spring',                     distractors: ['Winter', 'Summer', 'Fall'] },
  ];

  let deck = [], currentIdx = 0, score = 0, total = 0, answered = false;

  function shuffle(arr) { return [...arr].sort(() => Math.random() - 0.5); }

  function buildDeck() {
    deck = shuffle(words).slice(0, 10);
    currentIdx = 0; score = 0; total = 0; answered = false;
    showQuestion();
  }

  function showQuestion() {
    if (currentIdx >= deck.length) { showFinal(); return; }
    answered = false;
    const q = deck[currentIdx];
    document.getElementById('lgWord').textContent = q.word;
    document.getElementById('lgType').textContent = `Language: ${q.lang}`;
    document.getElementById('lgFeedback').textContent = '';
    document.getElementById('lgNext').style.display = 'none';
    document.getElementById('lgScore').innerHTML = `Score: <strong>${score}</strong> / <strong>${total}</strong>`;

    const allOptions = shuffle([q.meaning, ...q.distractors]).slice(0, 4);
    const choicesEl = document.getElementById('lgChoices');
    choicesEl.innerHTML = '';
    allOptions.forEach(opt => {
      const btn = document.createElement('button');
      btn.className = 'lang-choice';
      btn.textContent = opt;
      btn.addEventListener('click', () => handleAnswer(btn, opt, q.meaning));
      choicesEl.appendChild(btn);
    });
  }

  function handleAnswer(btn, chosen, correct) {
    if (answered) return;
    answered = true;
    total++;
    const allBtns = document.querySelectorAll('.lang-choice');
    allBtns.forEach(b => {
      b.disabled = true;
      if (b.textContent === correct) b.classList.add('correct');
    });
    if (chosen === correct) {
      score++;
      btn.classList.add('correct');
      document.getElementById('lgFeedback').textContent = '✅ Correct! Miigwech / Pidamayaye!';
    } else {
      btn.classList.add('wrong');
      document.getElementById('lgFeedback').textContent = `Not quite — the answer is "${correct}"`;
    }
    document.getElementById('lgScore').innerHTML = `Score: <strong>${score}</strong> / <strong>${total}</strong>`;
    document.getElementById('lgNext').style.display = 'inline-block';
  }

  function showFinal() {
    const pct = Math.round((score / total) * 100);
    let msg = pct >= 80 ? '🌟 Excellent! You\'re a Language Keeper!' : pct >= 60 ? '👍 Great effort! Keep practicing with MIIN and Dakhota.org!' : '🌱 Keep going — every word learned is a step toward fluency!';
    document.getElementById('lgWord').textContent = `${score} / ${total}`;
    document.getElementById('lgType').textContent = `${pct}% — ${msg}`;
    document.getElementById('lgChoices').innerHTML = '';
    document.getElementById('lgFeedback').textContent = 'Practice more words with the Ojibwe Language Deck and Dakota Language Deck from your Nashke collection!';
    document.getElementById('lgNext').style.display = 'none';
  }

  const nextBtn = document.getElementById('lgNext');
  const restartBtn = document.getElementById('lgRestart');
  if (nextBtn) nextBtn.addEventListener('click', () => { currentIdx++; showQuestion(); });
  if (restartBtn) restartBtn.addEventListener('click', buildDeck);

  buildDeck();
})();
