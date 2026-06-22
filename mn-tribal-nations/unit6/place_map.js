// Minnesota Place Names Map — Unit 6
// Names sourced from Fond du Lac Band (via MDE IEFA), Grand Portage Band (via MDE IEFA), Dakhota.org
(function() {
  const canvas = document.getElementById('placeCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const W = 680, H = 460;
  canvas.width = W; canvas.height = H;

  // x/y as fractions of canvas, approximate MN geography
  const places = [
    {
      modern: 'Minneapolis / Bdote area',
      x: 0.62, y: 0.58,
      nation: 'dakota',
      original: 'Bdote',
      language: 'Dakota',
      meaning: 'Where two rivers meet — the sacred confluence of the Minnesota and Mississippi Rivers, the center of the Dakota world.',
      source: 'Dakhota.org & MDE IEFA Lower Sioux Caŋṡayapi curriculum',
    },
    {
      modern: 'Lake Minnetonka',
      x: 0.55, y: 0.56,
      nation: 'dakota',
      original: 'Mní Tháŋka',
      language: 'Dakota',
      meaning: 'Big Water. The Dakota name describes what is most notable about the lake — its size.',
      source: 'Dakhota.org Dakota language resources',
    },
    {
      modern: 'Minnehaha Falls',
      x: 0.63, y: 0.60,
      nation: 'dakota',
      original: 'Mni Haha',
      language: 'Dakota',
      meaning: 'Laughing / curling water — named for the sound and movement of the waterfall.',
      source: 'Dakhota.org & MDE IEFA resources',
    },
    {
      modern: 'Minnesota River',
      x: 0.40, y: 0.68,
      nation: 'dakota',
      original: 'Mní Sóta Wakpá',
      language: 'Dakota',
      meaning: 'Sky-tinted water river. This is where the state name "Minnesota" comes from.',
      source: 'Dakhota.org & MDE IEFA Lower Sioux Caŋṡayapi curriculum',
    },
    {
      modern: 'Shakopee',
      x: 0.60, y: 0.63,
      nation: 'dakota',
      original: 'Šakpe Otonwe',
      language: 'Dakota',
      meaning: "Six's Village — named after Chief Šakpe. Today the Shakopee Mdewakanton Sioux Community's homeland.",
      source: 'Dakhota.org & MDE IEFA',
    },
    {
      modern: 'Mankato',
      x: 0.45, y: 0.73,
      nation: 'dakota',
      original: 'Makhóčhe Mní Sóta',
      language: 'Dakota',
      meaning: 'Blue Earth — named for the bluish-green clay found along the river near here.',
      source: 'Dakhota.org Dakota language resources',
    },
    {
      modern: 'Leech Lake',
      x: 0.42, y: 0.32,
      nation: 'ojibwe',
      original: 'Miskwaaziibiing',
      language: 'Ojibwe',
      meaning: "Place of red pike. The Leech Lake Band's homeland — named for the fish present in the water.",
      source: 'Fond du Lac Ojibwemowin Roads & Buildings (via MDE IEFA)',
    },
    {
      modern: 'Red Lake',
      x: 0.35, y: 0.18,
      nation: 'ojibwe',
      original: 'Gaa-miskwaawaakokaag',
      language: 'Ojibwe',
      meaning: 'Place of red pines. Home of the Red Lake Band of Chippewa — one of the most sovereign tribal nations in the US.',
      source: 'Fond du Lac Ojibwemowin Roads & Buildings (via MDE IEFA)',
    },
    {
      modern: 'White Earth',
      x: 0.22, y: 0.28,
      nation: 'ojibwe',
      original: 'Gaa-waabizhiishing',
      language: 'Ojibwe',
      meaning: 'White Earth — the White Earth Nation homeland. Home of the Rights of Manoomin law (2021).',
      source: 'Fond du Lac Ojibwemowin Roads & Buildings (via MDE IEFA)',
    },
    {
      modern: 'Fond du Lac / Duluth area',
      x: 0.72, y: 0.30,
      nation: 'ojibwe',
      original: 'Gaa-wiindamaagozid',
      language: 'Ojibwe',
      meaning: "The one who is told (or 'where word is given'). Home of the Fond du Lac Band, who created many of the Ojibwe language resources linked through MDE IEFA.",
      source: 'Fond du Lac Ojibwemowin Roads & Buildings (via MDE IEFA)',
    },
    {
      modern: 'Grand Portage (NE tip of MN)',
      x: 0.86, y: 0.14,
      nation: 'ojibwe',
      original: 'Gichi-onigaming',
      language: 'Ojibwe',
      meaning: "Great carrying place — named for the famous 9-mile portage trail. Grand Portage Band's homeland. Their North Shore place names resource is linked through MDE IEFA.",
      source: 'Grand Portage Band — Rivers of the North Shore (via MDE IEFA)',
    },
    {
      modern: 'Mille Lacs Lake',
      x: 0.57, y: 0.40,
      nation: 'ojibwe',
      original: 'Misi-zaaga\'iganing',
      language: 'Ojibwe',
      meaning: "At the great lake. Home of the Mille Lacs Band of Ojibwe, known for landmark treaty rights court cases protecting hunting, fishing, and gathering rights.",
      source: 'Fond du Lac Ojibwemowin Roads & Buildings (via MDE IEFA)',
    },
  ];

  const colors = { dakota: '#B03A2E', ojibwe: '#2D6A2D' };
  let hovered = null, selected = null;

  function drawMN() {
    ctx.beginPath();
    ctx.moveTo(W*0.18, H*0.05);
    ctx.lineTo(W*0.82, H*0.05);
    ctx.lineTo(W*0.82, H*0.28);
    ctx.lineTo(W*0.91, H*0.28);
    ctx.lineTo(W*0.91, H*0.44);
    ctx.lineTo(W*0.82, H*0.44);
    ctx.lineTo(W*0.82, H*0.93);
    ctx.lineTo(W*0.48, H*0.93);
    ctx.lineTo(W*0.38, H*0.82);
    ctx.lineTo(W*0.18, H*0.82);
    ctx.closePath();
    ctx.fillStyle = '#E8F2E8';
    ctx.fill();
    ctx.strokeStyle = '#9BBB99';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Rivers
    ctx.strokeStyle = '#4A90C888';
    ctx.lineWidth = 2;
    ctx.setLineDash([4,3]);
    ctx.beginPath();
    ctx.moveTo(W*0.18, H*0.70); ctx.quadraticCurveTo(W*0.38, H*0.72, W*0.55, H*0.65); ctx.quadraticCurveTo(W*0.66, H*0.60, W*0.72, H*0.68); ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(W*0.76, H*0.08); ctx.quadraticCurveTo(W*0.82, H*0.42, W*0.78, H*0.72); ctx.quadraticCurveTo(W*0.76, H*0.82, W*0.72, H*0.92); ctx.stroke();
    ctx.setLineDash([]);

    // Labels
    ctx.fillStyle = '#666';
    ctx.font = 'italic 10px Arial';
    ctx.fillText('Minnesota River', W*0.28, H*0.77);
    ctx.fillText('Mississippi R.', W*0.77, H*0.52);
  }

  function drawPins() {
    places.forEach((p, i) => {
      const px = p.x * W, py = p.y * H;
      const isSel = selected === i, isHov = hovered === i;
      const col = colors[p.nation];

      if (isSel || isHov) {
        ctx.beginPath(); ctx.arc(px, py, 22, 0, Math.PI*2);
        ctx.fillStyle = col + '30'; ctx.fill();
      }
      // Pin body
      ctx.beginPath(); ctx.arc(px, py - 2, isSel ? 11 : 8, 0, Math.PI*2);
      ctx.fillStyle = col; ctx.fill();
      ctx.strokeStyle = '#fff'; ctx.lineWidth = 2; ctx.stroke();
      // Pin tip
      ctx.beginPath(); ctx.moveTo(px - 5, py + 6); ctx.lineTo(px, py + 14); ctx.lineTo(px + 5, py + 6);
      ctx.fillStyle = col; ctx.fill();

      // Name label
      if (isSel || isHov) {
        ctx.font = 'bold 10px Arial';
        ctx.fillStyle = '#1A1A1A';
        ctx.textAlign = 'center';
        ctx.fillText(p.modern.length > 20 ? p.modern.slice(0,20)+'…' : p.modern, px, py - 18);
      }
    });
    ctx.textAlign = 'left';

    // Legend
    ctx.fillStyle = 'rgba(255,255,255,0.88)';
    ctx.fillRect(12, 12, 190, 46);
    ctx.strokeStyle = '#ccc'; ctx.lineWidth = 1; ctx.strokeRect(12,12,190,46);
    ctx.font = 'bold 11px Arial';
    ctx.fillStyle = colors.ojibwe; ctx.fillText('● Ojibwe / Anishinaabe place', 20, 30);
    ctx.fillStyle = colors.dakota;  ctx.fillText('● Dakota place', 20, 48);
    ctx.strokeStyle = '';
  }

  function draw() {
    ctx.clearRect(0,0,W,H);
    drawMN(); drawPins();
    // Title
    ctx.fillStyle = '#1A1A1A'; ctx.font = 'bold 13px Arial'; ctx.textAlign = 'left';
    ctx.fillText('Original Names of Minnesota Places', 210, 24);
    ctx.fillStyle = '#555'; ctx.font = '11px Arial';
    ctx.fillText('Tap a pin to see the original name', 210, 40);
  }

  function getHit(px, py) {
    for (let i = 0; i < places.length; i++) {
      if (Math.hypot(px - places[i].x*W, py - places[i].y*H) < 18) return i;
    }
    return null;
  }

  function showInfo(i) {
    const p = places[i];
    const box = document.getElementById('placeInfo');
    const col = colors[p.nation];
    box.style.display = 'block';
    document.getElementById('placeTitle').textContent = p.modern + ' →';
    document.getElementById('placeOriginal').innerHTML =
      `<span class="${p.nation === 'dakota' ? 'pin-dakota' : 'pin-ojibwe'}">${p.original}</span>
       <span style="font-size:0.85rem;color:#888;font-family:Arial,sans-serif"> (${p.language})</span>`;
    document.getElementById('placeDesc').innerHTML =
      `${p.meaning}<br><span style="font-size:0.78rem;color:#888;font-family:Arial,sans-serif">📚 Source: ${p.source}</span>`;
  }

  function handleClick(e) {
    const rect = canvas.getBoundingClientRect();
    const scaleX = W/rect.width, scaleY = H/rect.height;
    let px, py;
    if (e.touches) { px=(e.touches[0].clientX-rect.left)*scaleX; py=(e.touches[0].clientY-rect.top)*scaleY; }
    else { px=(e.clientX-rect.left)*scaleX; py=(e.clientY-rect.top)*scaleY; }
    const hit = getHit(px,py);
    if (hit !== null) { selected = hit; showInfo(hit); draw(); }
  }

  canvas.addEventListener('click', handleClick);
  canvas.addEventListener('touchstart', e => { e.preventDefault(); handleClick(e); }, { passive:false });
  canvas.addEventListener('mousemove', e => {
    const rect = canvas.getBoundingClientRect();
    const px=(e.clientX-rect.left)*W/rect.width, py=(e.clientY-rect.top)*H/rect.height;
    const hit = getHit(px,py);
    if (hit !== hovered) { hovered=hit; draw(); }
    canvas.style.cursor = hit!==null ? 'pointer' : 'default';
  });

  draw();
})();
