// Wild Rice Harvest Simulation
// Students tap ripe (golden) stalks to harvest them
// Teaching: leave some behind so the rice can grow again

(function() {
  const canvas = document.getElementById('harvestCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let stalks = [];
  let totalRipe = 0;

  const W = 680, H = 360;
  canvas.width = W;
  canvas.height = H;

  function rand(min, max) { return Math.random() * (max - min) + min; }

  function buildStalks() {
    stalks = [];
    const count = 32;
    for (let i = 0; i < count; i++) {
      const x = rand(30, W - 30);
      const ripeness = Math.random(); // 0=green, >0.55=ripe
      stalks.push({
        x,
        baseY: rand(H * 0.55, H * 0.85),
        height: rand(80, 140),
        ripe: ripeness > 0.55,
        harvested: false,
        sway: rand(0, Math.PI * 2),
        swaySpeed: rand(0.008, 0.018),
        thickness: rand(3, 6),
      });
    }
    totalRipe = stalks.filter(s => s.ripe).length;
    updateScore();
  }

  function updateScore() {
    const harvested = stalks.filter(s => s.ripe && s.harvested).length;
    const left = stalks.filter(s => s.ripe && !s.harvested).length;
    document.getElementById('harvestCount').textContent = harvested;
    document.getElementById('leftCount').textContent = left;
  }

  let frame = 0;

  function draw() {
    frame++;
    ctx.clearRect(0, 0, W, H);

    // Sky gradient
    const sky = ctx.createLinearGradient(0, 0, 0, H * 0.45);
    sky.addColorStop(0, '#87CEEB');
    sky.addColorStop(1, '#C8E8F5');
    ctx.fillStyle = sky;
    ctx.fillRect(0, 0, W, H * 0.45);

    // Water
    const water = ctx.createLinearGradient(0, H * 0.45, 0, H);
    water.addColorStop(0, '#1B5FA8');
    water.addColorStop(1, '#0D3A6E');
    ctx.fillStyle = water;
    ctx.fillRect(0, H * 0.45, W, H * 0.55);

    // Water ripple lines
    ctx.strokeStyle = 'rgba(255,255,255,0.12)';
    ctx.lineWidth = 1;
    for (let y = H * 0.5; y < H; y += 18) {
      ctx.beginPath();
      ctx.moveTo(0, y + Math.sin(frame * 0.02 + y) * 3);
      ctx.lineTo(W, y + Math.sin(frame * 0.02 + y + 2) * 3);
      ctx.stroke();
    }

    // Canoe silhouette
    ctx.fillStyle = '#6B4226';
    ctx.beginPath();
    ctx.ellipse(W * 0.5, H * 0.48, 90, 14, 0, 0, Math.PI);
    ctx.fill();
    // Paddler dots
    ctx.fillStyle = '#3A1800';
    ctx.beginPath(); ctx.arc(W * 0.44, H * 0.465, 8, 0, Math.PI * 2); ctx.fill();
    ctx.beginPath(); ctx.arc(W * 0.56, H * 0.465, 8, 0, Math.PI * 2); ctx.fill();

    // Stalks
    stalks.forEach(s => {
      s.sway += s.swaySpeed;
      const swayX = Math.sin(s.sway) * 5;
      const topX = s.x + swayX;
      const topY = s.baseY - s.height;

      if (s.harvested) {
        // Show cut stub
        ctx.strokeStyle = '#555';
        ctx.lineWidth = s.thickness;
        ctx.beginPath();
        ctx.moveTo(s.x, s.baseY);
        ctx.lineTo(s.x, s.baseY - 20);
        ctx.stroke();
        return;
      }

      // Stem
      ctx.strokeStyle = s.ripe ? '#8B6914' : '#2D6A2D';
      ctx.lineWidth = s.thickness;
      ctx.beginPath();
      ctx.moveTo(s.x, s.baseY);
      ctx.quadraticCurveTo(s.x + swayX * 0.5, s.baseY - s.height * 0.6, topX, topY);
      ctx.stroke();

      // Seed head
      if (s.ripe) {
        // Golden drooping seed head
        ctx.fillStyle = '#D4820A';
        for (let j = 0; j < 6; j++) {
          const angle = (j / 6) * Math.PI * 2;
          const dx = Math.cos(angle) * 9;
          const dy = Math.abs(Math.sin(angle)) * 14;
          ctx.beginPath();
          ctx.ellipse(topX + dx * 0.6, topY + dy * 0.5, 3, 7, angle, 0, Math.PI * 2);
          ctx.fill();
        }
        // Glow hint
        ctx.strokeStyle = 'rgba(244,200,50,0.4)';
        ctx.lineWidth = 8;
        ctx.beginPath();
        ctx.arc(topX, topY + 4, 12, 0, Math.PI * 2);
        ctx.stroke();
      } else {
        // Green feathery top
        ctx.fillStyle = '#4A8A4A';
        for (let j = 0; j < 5; j++) {
          ctx.beginPath();
          ctx.ellipse(topX + (j - 2) * 5, topY - j * 3, 3, 10, (j - 2) * 0.3, 0, Math.PI * 2);
          ctx.fill();
        }
      }
    });

    // Legend overlay
    ctx.fillStyle = 'rgba(0,0,0,0.45)';
    ctx.fillRect(10, 10, 220, 36);
    ctx.fillStyle = '#fff';
    ctx.font = '13px Arial';
    ctx.fillText('🟡 Tap golden stalks to harvest', 18, 32);

    requestAnimationFrame(draw);
  }

  function getHitStalk(px, py) {
    // Find the closest ripe, unharvested stalk near the tap point
    let best = null, bestDist = 36;
    stalks.forEach(s => {
      if (!s.ripe || s.harvested) return;
      const topX = s.x + Math.sin(s.sway) * 5;
      const topY = s.baseY - s.height;
      const dist = Math.hypot(px - topX, py - topY);
      if (dist < bestDist) { bestDist = dist; best = s; }
      // Also check mid-stalk
      const midDist = Math.hypot(px - s.x, py - (s.baseY - s.height * 0.5));
      if (midDist < bestDist) { bestDist = midDist; best = s; }
    });
    return best;
  }

  function handleTap(e) {
    e.preventDefault();
    const rect = canvas.getBoundingClientRect();
    const scaleX = W / rect.width;
    const scaleY = H / rect.height;
    let cx, cy;
    if (e.touches) {
      cx = (e.touches[0].clientX - rect.left) * scaleX;
      cy = (e.touches[0].clientY - rect.top) * scaleY;
    } else {
      cx = (e.clientX - rect.left) * scaleX;
      cy = (e.clientY - rect.top) * scaleY;
    }
    const hit = getHitStalk(cx, cy);
    if (hit) {
      hit.harvested = true;
      updateScore();
      // Particle burst (simple)
      showBurst(cx, cy);
    }
  }

  function showBurst(x, y) {
    // Quick overlay flash
    ctx.save();
    ctx.fillStyle = 'rgba(212,130,10,0.35)';
    ctx.beginPath();
    ctx.arc(x, y, 28, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }

  canvas.addEventListener('click', handleTap);
  canvas.addEventListener('touchstart', handleTap, { passive: false });

  // Exposed globals for buttons
  window.resetHarvest = function() {
    buildStalks();
    document.getElementById('harvestScore').innerHTML =
      'Tap golden stalks to begin harvesting &nbsp;·&nbsp; <strong id="harvestCount">0</strong> harvested &nbsp;·&nbsp; <strong id="leftCount">0</strong> left behind';
  };

  window.showHarvestResult = function() {
    const harvested = stalks.filter(s => s.ripe && s.harvested).length;
    const left = stalks.filter(s => s.ripe && !s.harvested).length;
    const pctHarvested = totalRipe > 0 ? Math.round((harvested / totalRipe) * 100) : 0;
    const pctLeft = 100 - pctHarvested;
    let msg = '';
    if (pctLeft < 20) {
      msg = `⚠️ You took too much! You harvested ${pctHarvested}% and left only ${pctLeft}% — the lake may not recover next year. Remember Nokomis's teaching: leave some for the future.`;
    } else if (pctHarvested < 40) {
      msg = `You harvested ${pctHarvested}% and left ${pctLeft}% behind — very gentle! The rice will definitely grow back. Can you harvest a bit more while still being respectful?`;
    } else {
      msg = `✅ Miigwech! You harvested ${pctHarvested}% and left ${pctLeft}% for next year. That's good harvesting — like Miigizi's Nokomis taught: take enough, leave enough.`;
    }
    document.getElementById('harvestScore').textContent = msg;
  };

  buildStalks();
  draw();
})();
