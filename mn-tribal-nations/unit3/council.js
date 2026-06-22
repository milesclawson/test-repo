// Tribal Council Simulation — Unit 3
(function() {
  const container = document.getElementById('councilSim');
  if (!container) return;

  const scenarios = [
    {
      situation: 'The community wants to plant a garden with traditional foods — like corn, beans, and squash — called the "Three Sisters." There are two possible locations. Where should the garden go?',
      character: 'Miigizi',
      choices: [
        { text: 'Next to the school, so students can help tend it and learn about it every day.', outcome: 'Great thinking! Putting the garden near the school means students can learn from it all year. The elders also said they could visit and teach the traditional names of the plants. The community agrees — and adds a sign with the Ojibwe names for each plant.', best: true },
        { text: 'Near the tribal center, so it\'s easy for everyone in the community to access it.', outcome: 'A thoughtful choice! Being near the tribal center means everyone can enjoy the harvest and elders can visit easily. The council notes that students would need to travel to tend it — maybe that\'s part of the learning too. The community discusses both options carefully.' },
        { text: 'Start with a small test plot in both locations and decide next year.', outcome: 'Wise and cautious! Starting small lets the community learn what works before committing. This is how many traditional decisions are made — carefully, with patience, watching how the land responds.' },
      ]
    },
    {
      situation: 'The tribal nation receives funding to support language learning. There are different ways to use it. Which approach should the council choose?',
      character: 'Winona',
      choices: [
        { text: 'Hire a full-time language teacher for the tribal school, so children learn every day.', outcome: 'Excellent! Daily language instruction builds fluency over time. The council also decides the teacher should document elder speakers\' stories so the knowledge is preserved — connecting teaching to community memory.', best: true },
        { text: 'Create a free app and website so everyone in the community can learn at home, like MIIN\'s Ojibwe app.', outcome: 'Smart use of technology! A free app reaches families who don\'t live close to the school. The council notes that MIIN already offers Ojibwe resources — maybe this funding could support a Dakota equivalent through Dakhota.org.' },
        { text: 'Pay elders who are fluent speakers to hold weekly community language circles.', outcome: 'A beautiful idea that honors the elders! Elder speakers carry knowledge that can\'t be found in any book. The council adds: can the recordings from these circles be archived and shared with the school?' },
      ]
    },
    {
      situation: 'A company wants to build a pipeline near the reservation that would cross a wild rice lake. The tribal council must decide what to do.',
      character: 'Miigizi & Winona',
      choices: [
        { text: 'Say no — the wild rice lake is too important to risk. The tribe has the right to protect it.', outcome: 'The council agrees that manoomin is a relative, not just a resource — and that tribal sovereignty gives the nation the right to say no to development on or near their land. They consult environmental scientists and pass a resolution protecting the lake. This is sovereignty in action.', best: true },
        { text: 'Ask for more information about the pipeline\'s safety, and hire tribal scientists to study the risk.', outcome: 'A careful, evidence-based approach. The council uses their sovereign right to demand an independent environmental study. They note: the White Earth Nation\'s Rights of Manoomin law means the rice itself has legal rights that must be considered.' },
        { text: 'Negotiate with the company — only allow the pipeline if they fund a 50-year environmental protection fund for the lake.', outcome: 'A negotiating approach that uses the tribe\'s sovereign power to protect future generations. The council weighs this carefully — some members say no amount of money replaces a healthy rice lake. The discussion continues in community.' },
      ]
    },
  ];

  let current = 0;
  let chosen = null;

  function render() {
    const s = scenarios[current];
    container.innerHTML = `
      <div class="council-scenario">
        <h4>🪑 Scenario ${current + 1} of ${scenarios.length} — Community Decision</h4>
        <p><strong>${s.character}</strong> brings this question to the tribal council. As a member of the community, you help decide:</p>
        <p style="margin-top:10px; font-style:italic; font-size:1rem; color:var(--text)">"${s.situation}"</p>
      </div>
      <div class="council-choices" id="choiceList">
        ${s.choices.map((c, i) => `
          <button class="choice-btn" data-idx="${i}">${String.fromCharCode(65+i)}. ${c.text}</button>
        `).join('')}
      </div>
      <div class="council-result" id="councilResult"></div>
      <div class="council-nav">
        <button id="cnPrev" ${current === 0 ? 'disabled' : ''}>← Previous</button>
        <span class="council-progress">Scenario ${current + 1} / ${scenarios.length}</span>
        <button id="cnNext" disabled>${current === scenarios.length - 1 ? '✅ Finished' : 'Next Scenario →'}</button>
      </div>
    `;

    container.querySelectorAll('.choice-btn').forEach(btn => {
      btn.addEventListener('click', function() {
        if (chosen !== null) return;
        chosen = parseInt(this.dataset.idx);
        const result = document.getElementById('councilResult');
        result.innerHTML = `<h4>${scenarios[current].choices[chosen].best ? '⭐ Strong Choice!' : '💬 Good Thinking!'}</h4><p>${scenarios[current].choices[chosen].outcome}</p>`;
        result.classList.add('show');
        this.classList.add('selected');
        document.getElementById('cnNext').disabled = false;
      });
    });

    document.getElementById('cnPrev').addEventListener('click', () => {
      current = Math.max(0, current - 1);
      chosen = null;
      render();
    });
    document.getElementById('cnNext').addEventListener('click', () => {
      if (current < scenarios.length - 1) {
        current++;
        chosen = null;
        render();
      } else {
        container.innerHTML = `
          <div class="council-scenario">
            <h4>🎉 Miigwech! You completed all three community decisions.</h4>
            <p>Real tribal councils consider many voices — elders, parents, youth, environmental experts — before making decisions. There are rarely simple right or wrong answers. The process of talking together, listening, and deciding as a community is itself the teaching.</p>
            <p style="margin-top:10px; font-size:0.88rem; color:var(--text-soft)">Source: Community decision-making practices from <a href="https://education.mn.gov/MDE/dse/indian/all/" target="_blank">MDE IEFA Tribal Relations Training</a>.</p>
          </div>
          <div style="text-align:center; margin-top:16px">
            <button class="sim-btn" onclick="location.reload()">🔄 Start Over</button>
          </div>
        `;
      }
    });
  }

  render();
})();
