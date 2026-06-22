// Dakota Communities Map — Unit 2
(function() {
  const canvas = document.getElementById('dakotaMapCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const W = 680, H = 440;
  canvas.width = W; canvas.height = H;

  const communities = [
    {
      name: 'Lower Sioux Indian Community',
      dakota: 'Čhaŋšáyapi Oyáte',
      x: 0.28, y: 0.72,
      color: '#B03A2E',
      desc: 'Located near Morton, MN on the Minnesota River. The Lower Sioux Community runs its own government, school, health clinic, and cultural programs. The MDE has partnered with Lower Sioux to create the Caŋṡayapi: Past and Present curriculum — a history of this community told by its own people.',
    },
    {
      name: 'Upper Sioux Community',
      dakota: 'Pejúhutazizi Oyáte',
      x: 0.22, y: 0.60,
      color: '#C0392B',
      desc: 'Located near Granite Falls, MN — also on the Minnesota River. "Pejúhutazizi" means Yellow Medicine, named for the Yellow Medicine River. The Upper Sioux Community maintains its own government and cultural programs, including language revitalization efforts.',
    },
    {
      name: 'Prairie Island Indian Community',
      dakota: 'Thaŋktóŋwaŋ Oyáte',
      x: 0.72, y: 0.68,
      color: '#922B21',
      desc: 'Located near Red Wing, MN on an island in the Mississippi River. Prairie Island is the homeland of the Mdewakanton Dakota. The community runs its own government, environmental programs, and cultural initiatives, and has been a strong advocate for tribal sovereignty and treaty rights.',
    },
    {
      name: 'Shakopee Mdewakanton Sioux Community',
      dakota: 'Šakpe Mdewakantunwan Oyáte',
      x: 0.60, y: 0.52,
      color: '#7B241C',
      desc: 'Located near Prior Lake, MN — south of the Twin Cities. The Shakopee Mdewakanton Sioux Community is one of the most economically successful tribal nations in the US. They fund language revitalization, education programs for all students, environmental protection, and community support across Minnesota.',
    },
  ];

  let hovered = null;

  function drawMNOutline() {
    // Simplified Minnesota state outline
    ctx.beginPath();
    ctx.moveTo(W*0.18, H*0.05);
    ctx.lineTo(W*0.82, H*0.05);
    ctx.lineTo(W*0.82, H*0.28);
    ctx.lineTo(W*0.90, H*0.28);
    ctx.lineTo(W*0.90, H*0.45);
    ctx.lineTo(W*0.82, H*0.45);
    ctx.lineTo(W*0.82, H*0.92);
    ctx.lineTo(W*0.48, H*0.92);
    ctx.lineTo(W*0.38, H*0.80);
    ctx.lineTo(W*0.18, H*0.80);
    ctx.closePath();
    ctx.fillStyle = '#E8F4E8';
    ctx.fill();
    ctx.strokeStyle = '#9BBB99';
    ctx.lineWidth = 2;
    ctx.stroke();
  }

  function drawRivers() {
    ctx.strokeStyle = '#4A90C8';
    ctx.lineWidth = 2;
    ctx.setLineDash([4, 3]);
    // Minnesota River (rough path)
    ctx.beginPath();
    ctx.moveTo(W*0.18, H*0.68);
    ctx.quadraticCurveTo(W*0.35, H*0.72, W*0.55, H*0.62);
    ctx.quadraticCurveTo(W*0.65, H*0.56, W*0.72, H*0.65);
    ctx.stroke();
    // Mississippi (right side)
    ctx.beginPath();
    ctx.moveTo(W*0.75, H*0.08);
    ctx.quadraticCurveTo(W*0.82, H*0.40, W*0.78, H*0.70);
    ctx.quadraticCurveTo(W*0.76, H*0.80, W*0.72, H*0.90);
    ctx.stroke();
    ctx.setLineDash([]);

    // River labels
    ctx.fillStyle = '#2563a8';
    ctx.font = 'italic 10px Arial';
    ctx.fillText('Minnesota River', W*0.30, H*0.78);
    ctx.fillText('Mississippi R.', W*0.75, H*0.50);
  }

  function drawDots() {
    communities.forEach((c, i) => {
      const cx = c.x * W, cy = c.y * H;
      const isHov = hovered === i;
      // Pulse ring
      ctx.beginPath();
      ctx.arc(cx, cy, isHov ? 22 : 16, 0, Math.PI*2);
      ctx.fillStyle = isHov ? c.color + '44' : c.color + '22';
      ctx.fill();
      // Dot
      ctx.beginPath();
      ctx.arc(cx, cy, isHov ? 12 : 9, 0, Math.PI*2);
      ctx.fillStyle = c.color;
      ctx.fill();
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 2;
      ctx.stroke();
      // Label
      ctx.fillStyle = '#1A1A1A';
      ctx.font = `bold ${isHov ? 12 : 11}px Arial`;
      ctx.textAlign = 'center';
      const lines = c.name.split(' ');
      // Short label
      const short = c.name.replace('Indian Community','').replace('Sioux Community','').trim();
      ctx.fillText(short, cx, cy + 22);
    });
    ctx.textAlign = 'left';
  }

  function drawTitle() {
    ctx.fillStyle = '#1A1A1A';
    ctx.font = 'bold 14px Arial';
    ctx.fillText('Dakota Communities in Minnesota Today', 18, 24);
    ctx.fillStyle = '#555';
    ctx.font = '11px Arial';
    ctx.fillText('Tap a dot to learn about each community', 18, 40);
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    drawMNOutline();
    drawRivers();
    drawDots();
    drawTitle();
  }

  function getHit(px, py) {
    for (let i = 0; i < communities.length; i++) {
      const c = communities[i];
      if (Math.hypot(px - c.x*W, py - c.y*H) < 22) return i;
    }
    return null;
  }

  function handleClick(e) {
    const rect = canvas.getBoundingClientRect();
    const scaleX = W / rect.width, scaleY = H / rect.height;
    let px, py;
    if (e.touches) {
      px = (e.touches[0].clientX - rect.left) * scaleX;
      py = (e.touches[0].clientY - rect.top) * scaleY;
    } else {
      px = (e.clientX - rect.left) * scaleX;
      py = (e.clientY - rect.top) * scaleY;
    }
    const hit = getHit(px, py);
    if (hit !== null) {
      hovered = hit;
      const c = communities[hit];
      const box = document.getElementById('mapInfo');
      document.getElementById('mapTitle').textContent = c.name + ' — ' + c.dakota;
      document.getElementById('mapDesc').textContent = c.desc;
      box.style.display = 'block';
      draw();
    }
  }

  canvas.addEventListener('click', handleClick);
  canvas.addEventListener('touchstart', e => { e.preventDefault(); handleClick(e); }, { passive: false });
  canvas.addEventListener('mousemove', e => {
    const rect = canvas.getBoundingClientRect();
    const px = (e.clientX - rect.left) * W / rect.width;
    const py = (e.clientY - rect.top) * H / rect.height;
    const hit = getHit(px, py);
    if (hit !== hovered) { hovered = hit; draw(); }
    canvas.style.cursor = hit !== null ? 'pointer' : 'default';
  });

  draw();
})();
