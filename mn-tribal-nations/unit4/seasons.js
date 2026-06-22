// Ojibwe Seasons Wheel — Unit 4
(function() {
  const canvas = document.getElementById('seasonCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const W = 500, H = 500;
  canvas.width = W; canvas.height = H;
  const cx = W / 2, cy = H / 2, R = 190, innerR = 80;

  const seasons = [
    {
      name: 'Ziigwan',
      english: 'Spring',
      icon: '🌱',
      color: '#5A9E5A',
      moonName: 'Iskigamizige-giizis',
      moonEnglish: 'Maple Sugar Moon (March/April)',
      activities: [
        'Maple sugaring — collecting and boiling sap',
        'Preparing gardens and planting seeds',
        'Fishing returns to open water',
        'Gathering medicines and early plants',
        'Geese return from the south (Anishinaabe sign of spring)',
      ],
      foods: ['Maple syrup & maple sugar', 'Early greens and fiddleheads', 'Walleye and other fish'],
      source: 'Moon names from MIIN 3rd Grade resources (miinojibwe.org)',
    },
    {
      name: 'Niibin',
      english: 'Summer',
      icon: '☀️',
      color: '#D4820A',
      moonName: 'Ode\'imini-giizis / Miinikaa-giizis',
      moonEnglish: 'Strawberry Moon / Blueberry Moon (June–August)',
      activities: [
        'Berry picking — strawberries, blueberries, raspberries',
        'Tending gardens (Three Sisters: corn, beans, squash)',
        'Fishing and gathering near water',
        'Visiting family at summer encampments',
        'Language camps and cultural gatherings',
      ],
      foods: ['Wild berries', 'Garden vegetables (Three Sisters)', 'Fish and waterfowl', 'Wild plants and medicines'],
      source: 'Seasonal practices from MIIN 3rd Grade Bdote & Niigaane science curricula',
    },
    {
      name: 'Dagwaagin',
      english: 'Fall / Autumn',
      icon: '🍂',
      color: '#B03A2E',
      moonName: 'Manoominike-giizis',
      moonEnglish: 'Wild Rice Harvesting Moon (August/September)',
      activities: [
        'Wild rice (manoomin) harvest — canoes and knocking sticks',
        'Parching and storing the rice for winter',
        'Hunting deer and other game',
        'Gathering nuts and late berries',
        'Preparing and storing food for winter',
      ],
      foods: ['Wild rice / Manoomin', 'Venison (deer)', 'Nuts and dried berries', 'Dried fish'],
      source: 'Wild rice practices from MIIN 3rd Grade resources. Fond du Lac Band See & Say videos via MDE IEFA.',
    },
    {
      name: 'Biboon',
      english: 'Winter',
      icon: '❄️',
      color: '#1B5FA8',
      moonName: 'Manidoo-giizisoons',
      moonEnglish: 'Little Spirit Moon (December)',
      activities: [
        'Storytelling — many stories are traditionally shared only in winter',
        'Traditional games: Moccasin Game (Makizinataagewin), Bagese Bowl Game',
        'Ice fishing',
        'Making and repairing tools, clothing, and beadwork',
        'Community gatherings and ceremonies (community review for specifics)',
      ],
      foods: ['Stored wild rice and dried foods', 'Venison and other stored meats', 'Maple sugar saved from spring'],
      source: 'Winter games from Nashke.com (Makizinataagewin, Bagese Bowl Game). Storytelling traditions from MIIN resources.',
    },
  ];

  let selected = null;
  let hovered = null;

  function angleForIndex(i) {
    return (i / seasons.length) * Math.PI * 2 - Math.PI / 2;
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);

    // Background circle
    ctx.beginPath();
    ctx.arc(cx, cy, R + 20, 0, Math.PI * 2);
    ctx.fillStyle = '#F5F0E8';
    ctx.fill();
    ctx.strokeStyle = '#D9C8A8';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Draw wedges
    seasons.forEach((s, i) => {
      const startAngle = angleForIndex(i);
      const endAngle = angleForIndex(i + 1);
      const isHov = hovered === i;
      const isSel = selected === i;

      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.arc(cx, cy, R, startAngle, endAngle);
      ctx.closePath();

      ctx.fillStyle = isSel ? s.color : isHov ? s.color + 'CC' : s.color + '88';
      ctx.fill();
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 3;
      ctx.stroke();

      // Icon & label in wedge
      const midAngle = (startAngle + endAngle) / 2;
      const labelR = R * 0.64;
      const lx = cx + Math.cos(midAngle) * labelR;
      const ly = cy + Math.sin(midAngle) * labelR;

      ctx.font = '28px serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(s.icon, lx, ly - 14);

      ctx.font = `bold ${isSel || isHov ? 14 : 12}px Arial`;
      ctx.fillStyle = isSel ? '#fff' : '#1A1A1A';
      ctx.fillText(s.name, lx, ly + 12);
      ctx.font = `${isSel || isHov ? 12 : 10}px Arial`;
      ctx.fillStyle = isSel ? 'rgba(255,255,255,0.85)' : '#444';
      ctx.fillText(s.english, lx, ly + 26);
    });

    // Inner circle
    ctx.beginPath();
    ctx.arc(cx, cy, innerR, 0, Math.PI * 2);
    ctx.fillStyle = '#fff';
    ctx.fill();
    ctx.strokeStyle = '#D9C8A8';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Center text
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    if (selected !== null) {
      ctx.font = 'bold 14px Arial';
      ctx.fillStyle = seasons[selected].color;
      ctx.fillText(seasons[selected].name, cx, cy - 10);
      ctx.font = '11px Arial';
      ctx.fillStyle = '#555';
      ctx.fillText(seasons[selected].english, cx, cy + 8);
      ctx.font = '20px serif';
      ctx.fillText(seasons[selected].icon, cx, cy + 26);
    } else {
      ctx.font = '13px Arial';
      ctx.fillStyle = '#888';
      ctx.fillText('Tap a', cx, cy - 8);
      ctx.fillText('season', cx, cy + 8);
    }
  }

  function getWedge(px, py) {
    const dx = px - cx, dy = py - cy;
    const dist = Math.hypot(dx, dy);
    if (dist < innerR || dist > R) return null;
    let angle = Math.atan2(dy, dx) + Math.PI / 2;
    if (angle < 0) angle += Math.PI * 2;
    const idx = Math.floor((angle / (Math.PI * 2)) * seasons.length);
    return idx % seasons.length;
  }

  function showInfo(i) {
    const s = seasons[i];
    const infoBox = document.getElementById('seasonInfo');
    infoBox.style.display = 'block';
    infoBox.style.borderColor = s.color;
    infoBox.innerHTML = `
      <h4 style="color:${s.color}">${s.icon} ${s.name} — ${s.english}</h4>
      <div class="moon-name" style="color:${s.color}">🌕 ${s.moonName} <span style="color:#888;font-weight:normal">(${s.moonEnglish})</span></div>
      <p style="font-size:0.88rem; color:#555; margin-bottom:10px; font-family:Arial,sans-serif"><strong>Traditional Activities:</strong></p>
      <ul>${s.activities.map(a => `<li>${a}</li>`).join('')}</ul>
      <p style="font-size:0.88rem; color:#555; margin-top:10px; margin-bottom:6px; font-family:Arial,sans-serif"><strong>Traditional Foods:</strong> ${s.foods.join(' · ')}</p>
      <p style="font-size:0.78rem; color:#888; margin-top:10px; font-family:Arial,sans-serif">📚 ${s.source}</p>
    `;
  }

  canvas.addEventListener('click', e => {
    const rect = canvas.getBoundingClientRect();
    const px = (e.clientX - rect.left) * W / rect.width;
    const py = (e.clientY - rect.top) * H / rect.height;
    const hit = getWedge(px, py);
    if (hit !== null) { selected = hit; showInfo(hit); draw(); }
  });
  canvas.addEventListener('touchstart', e => {
    e.preventDefault();
    const rect = canvas.getBoundingClientRect();
    const px = (e.touches[0].clientX - rect.left) * W / rect.width;
    const py = (e.touches[0].clientY - rect.top) * H / rect.height;
    const hit = getWedge(px, py);
    if (hit !== null) { selected = hit; showInfo(hit); draw(); }
  }, { passive: false });
  canvas.addEventListener('mousemove', e => {
    const rect = canvas.getBoundingClientRect();
    const px = (e.clientX - rect.left) * W / rect.width;
    const py = (e.clientY - rect.top) * H / rect.height;
    const hit = getWedge(px, py);
    if (hit !== hovered) { hovered = hit; draw(); }
    canvas.style.cursor = hit !== null ? 'pointer' : 'default';
  });

  draw();
})();
