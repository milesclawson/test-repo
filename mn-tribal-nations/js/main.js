// Shared utilities across the site

// Tooltip for Ojibwe/Dakota words
(function() {
  const tip = document.createElement('div');
  tip.className = 'tooltip';
  document.body.appendChild(tip);

  document.addEventListener('mouseover', e => {
    const el = e.target.closest('[data-tip]');
    if (!el) { tip.style.display = 'none'; return; }
    tip.textContent = el.dataset.tip;
    tip.style.display = 'block';
  });
  document.addEventListener('mousemove', e => {
    tip.style.left = (e.clientX + 14) + 'px';
    tip.style.top  = (e.clientY - 10) + 'px';
  });
  document.addEventListener('mouseout', e => {
    if (!e.target.closest('[data-tip]')) tip.style.display = 'none';
  });
  // Touch support
  document.addEventListener('touchstart', e => {
    const el = e.target.closest('[data-tip]');
    if (!el) { tip.style.display = 'none'; return; }
    tip.textContent = el.dataset.tip;
    const r = el.getBoundingClientRect();
    tip.style.left = r.left + 'px';
    tip.style.top  = (r.bottom + 8) + 'px';
    tip.style.display = 'block';
    setTimeout(() => { tip.style.display = 'none'; }, 2500);
  }, { passive: true });
})();

// Story reader
function initStoryReader(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  const pages = container.querySelectorAll('.story-page');
  const prevBtn = container.querySelector('.prev-btn');
  const nextBtn = container.querySelector('.next-btn');
  const progress = container.querySelector('.story-progress');
  let current = 0;

  function show(n) {
    pages.forEach((p, i) => p.classList.toggle('active', i === n));
    prevBtn.disabled = n === 0;
    nextBtn.disabled = n === pages.length - 1;
    progress.textContent = `Page ${n + 1} of ${pages.length}`;
  }
  prevBtn.addEventListener('click', () => { if (current > 0) show(--current); });
  nextBtn.addEventListener('click', () => { if (current < pages.length - 1) show(++current); });
  show(0);
}

// Memory matching game
function initMemoryGame(containerId, pairs) {
  const container = document.getElementById(containerId);
  if (!container) return;
  const grid = container.querySelector('.game-grid');
  const status = container.querySelector('.game-status');
  const restartBtn = container.querySelector('.restart-btn');

  let flipped = [], matched = 0, moves = 0, locked = false;

  function shuffle(arr) {
    return [...arr].sort(() => Math.random() - 0.5);
  }

  function build() {
    grid.innerHTML = '';
    flipped = []; matched = 0; moves = 0; locked = false;
    status.innerHTML = `Matches: <strong>0 / ${pairs.length}</strong> &nbsp;|&nbsp; Moves: <strong>0</strong>`;
    const cards = shuffle([...pairs, ...pairs].map((p, i) => ({ ...p, id: i })));
    cards.forEach(card => {
      const btn = document.createElement('button');
      btn.className = 'memory-card';
      btn.dataset.value = card.value;
      btn.setAttribute('aria-label', 'Hidden card');
      btn.innerHTML = `<span style="display:none">${card.display}</span>`;
      btn.addEventListener('click', () => flip(btn));
      grid.appendChild(btn);
    });
  }

  function flip(btn) {
    if (locked || btn.classList.contains('flipped') || btn.classList.contains('matched')) return;
    btn.classList.add('flipped');
    btn.querySelector('span').style.display = '';
    btn.setAttribute('aria-label', btn.dataset.value);
    flipped.push(btn);
    if (flipped.length === 2) {
      moves++;
      locked = true;
      setTimeout(check, 900);
    }
  }

  function check() {
    const [a, b] = flipped;
    if (a.dataset.value === b.dataset.value) {
      a.classList.add('matched'); b.classList.add('matched');
      matched++;
      if (matched === pairs.length) {
        status.innerHTML = `🎉 You matched all <strong>${pairs.length}</strong> pairs in <strong>${moves}</strong> moves! Miigwech!`;
      } else {
        status.innerHTML = `Matches: <strong>${matched} / ${pairs.length}</strong> &nbsp;|&nbsp; Moves: <strong>${moves}</strong>`;
      }
    } else {
      a.classList.remove('flipped'); b.classList.remove('flipped');
      a.querySelector('span').style.display = 'none';
      b.querySelector('span').style.display = 'none';
      a.setAttribute('aria-label', 'Hidden card');
      b.setAttribute('aria-label', 'Hidden card');
      status.innerHTML = `Matches: <strong>${matched} / ${pairs.length}</strong> &nbsp;|&nbsp; Moves: <strong>${moves}</strong>`;
    }
    flipped = [];
    locked = false;
  }

  restartBtn.addEventListener('click', build);
  build();
}
