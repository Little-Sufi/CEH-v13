![Study Guides Header](https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=800&h=200&fit=crop)

# 📚 CEH v13 MCQ-Focused Study Guides


<div class="xp-dashboard" style="background: var(--background-secondary); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; font-family: var(--font-interface, sans-serif); color: var(--text-normal); margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; border-bottom: 1px solid var(--border-color); padding-bottom: 10px;">
    <h2 style="margin: 0; color: var(--text-accent); font-size: 1.5rem; display: flex; align-items: center; gap: 8px;">🏆 CEH v13 Master's Dashboard</h2>
    <div style="text-align: right;">
      <span style="font-weight: bold; color: var(--text-success, #a6e3a1); font-size: 1.2rem;" id="total-xp-display">0</span> <span style="color: var(--text-muted); font-size: 0.9rem;">/ 26,250 XP</span>
    </div>
  </div>
  
  <div style="background: var(--background-primary); border-radius: 8px; height: 16px; width: 100%; overflow: hidden; margin-bottom: 20px; position: relative; border: 1px solid var(--border-color);">
    <div id="xp-progress-bar" style="background: linear-gradient(90deg, var(--interactive-accent) 0%, var(--text-accent) 100%); height: 100%; width: 0%; transition: width 0.4s ease;"></div>
  </div>

  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
    <span style="font-size: 0.9rem; color: var(--text-muted);" id="completion-percentage">Progress: 0.0% Complete</span>
    <button onclick="resetAllProgress()" style="background: var(--text-error, #f38ba8); color: var(--background-primary); border: none; padding: 6px 12px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85rem; transition: opacity 0.2s ease;" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">🔄 Reset Progress</button>
  </div>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 15px;" id="modules-grid">
    <!-- Dynamically injected modules -->
  </div>
</div>

<script>
const MODULES = [
  { id: "01", name: "Introduction to Ethical Hacking" },
  { id: "02", name: "Footprinting & Reconnaissance" },
  { id: "03", name: "Scanning Networks" },
  { id: "04", name: "Enumeration" },
  { id: "05", name: "Vulnerability Analysis" },
  { id: "06", name: "System Hacking" },
  { id: "07", name: "Malware Threats" },
  { id: "08", name: "Sniffing" },
  { id: "09", name: "Social Engineering" },
  { id: "10", name: "Denial-of-Service" },
  { id: "11", name: "Session Hijacking" },
  { id: "12", name: "Evading IDS, Firewalls & Honeypots" },
  { id: "13", name: "Hacking Web Servers" },
  { id: "14", name: "Hacking Web Applications" },
  { id: "15", name: "SQL Injection" },
  { id: "16", name: "Hacking Wireless Networks" },
  { id: "17", name: "Hacking Mobile Platforms" },
  { id: "18", name: "IoT & OT Hacking" },
  { id: "19", name: "Cloud Computing" },
  { id: "20", name: "Cryptography" },
  { id: "21", name: "AI-Powered Hacking" }
];

const TASKS = [
  { key: "overview", label: "Overview", xp: 100 },
  { key: "techniques", label: "Techniques", xp: 150 },
  { key: "tools", label: "Tools", xp: 200 },
  { key: "countermeasures", label: "Mitigations", xp: 150 },
  { key: "course", label: "Course Notes", xp: 200 },
  { key: "mcq", label: "MCQ Practice", xp: 200 },
  { key: "lab", label: "Practical Lab", xp: 250 }
];

const totalPossibleXP = MODULES.length * TASKS.reduce((acc, t) => acc + t.xp, 0);

function loadProgress() {
  const saved = localStorage.getItem('ceh_v13_progress');
  return saved ? JSON.parse(saved) : {};
}

function saveProgress(progress) {
  localStorage.setItem('ceh_v13_progress', JSON.stringify(progress));
}

function updateUI() {
  const progress = loadProgress();
  const grid = document.getElementById('modules-grid');
  grid.innerHTML = '';
  
  let currentXP = 0;
  
  MODULES.forEach(mod => {
    const modProgress = progress[mod.id] || {};
    let modXP = 0;
    
    TASKS.forEach(task => {
      if (modProgress[task.key]) {
        modXP += task.xp;
        currentXP += task.xp;
      }
    });
    
    const card = document.createElement('div');
    card.style.background = 'var(--background-primary)';
    card.style.border = '1px solid var(--border-color)';
    card.style.borderRadius = '8px';
    card.style.padding = '12px';
    card.style.display = 'flex';
    card.style.flexDirection = 'column';
    card.style.gap = '8px';
    
    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 5px;">
        <span style="font-weight: bold; color: var(--text-accent); font-size: 0.95rem;">M${mod.id}: ${mod.name}</span>
        <span style="font-size: 0.8rem; color: var(--text-success, #a6e3a1); font-weight: bold;">${modXP} / 1050 XP</span>
      </div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px;">
        ${TASKS.map(task => {
          const isChecked = modProgress[task.key] ? 'checked' : '';
          return `
            <label style="display: flex; align-items: center; gap: 6px; font-size: 0.75rem; color: var(--text-muted); cursor: pointer;">
              <input type="checkbox" data-mod="${mod.id}" data-task="${task.key}" onclick="toggleTask(this)" ${isChecked} style="accent-color: var(--interactive-accent); cursor: pointer;">
              <span>${task.label} <span style="color: var(--text-faint, #585b70);">(${task.xp}xp)</span></span>
            </label>
          `;
        }).join('')}
      </div>
    `;
    grid.appendChild(card);
  });
  
  document.getElementById('total-xp-display').innerText = currentXP.toLocaleString();
  const percentage = ((currentXP / totalPossibleXP) * 100).toFixed(1);
  document.getElementById('xp-progress-bar').style.width = `${percentage}%`;
  document.getElementById('completion-percentage').innerText = `Progress: ${percentage}% Complete (${currentXP.toLocaleString()} / ${totalPossibleXP.toLocaleString()} XP)`;
}

function toggleTask(checkbox) {
  const modId = checkbox.getAttribute('data-mod');
  const taskKey = checkbox.getAttribute('data-task');
  const progress = loadProgress();
  
  if (!progress[modId]) {
    progress[modId] = {};
  }
  
  progress[modId][taskKey] = checkbox.checked;
  saveProgress(progress);
  updateUI();
}

function resetAllProgress() {
  if (confirm("⚠️ Are you sure you want to reset all your learning progress and XP? This action cannot be undone.")) {
    localStorage.removeItem('ceh_v13_progress');
    updateUI();
  }
}

// Initial render
document.addEventListener('DOMContentLoaded', () => {
  updateUI();
});
// Fallback if DOMContentLoaded already fired
if (document.readyState === 'complete' || document.readyState === 'interactive') {
  updateUI();
}
</script>


[⬅️ CEH v13 Home](../Home.md)

---

## 📋 Module Index

| Module | Status |
|---|---|
| [Module 01: Introduction to Ethical Hacking](Module-01-Introduction-to-Ethical-Hacking/Home.md) | ✅ Complete! |
| [Module 02: Footprinting & Reconnaissance](Module-02-Footprinting-and-Reconnaissance/Home.md) | ✅ Complete! |
| [Module 03: Scanning Networks](Module-03-Scanning-Networks/Home.md) | ✅ Complete! |
| [Module 04: Enumeration](Module-04-Enumeration/Home.md) | ✅ Complete! |
| [Module 05: Vulnerability Analysis](Module-05-Vulnerability-Analysis/Home.md) | ✅ Complete! |
| [Module 06: System Hacking](Module-06-System-Hacking/Home.md) | ✅ Complete! |
| [Module 07: Malware Threats](Module-07-Malware-Threats/Home.md) | ✅ Complete! |
| [Module 08: Sniffing](Module-08-Sniffing/Home.md) | ✅ Complete! |
| [Module 09: Social Engineering](Module-09-Social-Engineering/Home.md) | ✅ Complete! |
| [Module 10: Denial-of-Service](Module-10-Denial-of-Service/Home.md) | ✅ Complete! |
| [Module 11: Session Hijacking](Module-11-Session-Hijacking/Home.md) | ✅ Complete! |
| [Module 12: Evading IDS, Firewalls & Honeypots](Module-12-Evading-IDS-Firewalls-and-Honeypots/Home.md) | ✅ Complete! |
| [Module 13: Hacking Web Servers](Module-13-Hacking-Web-Servers/Home.md) | ✅ Complete! |
| [Module 14: Hacking Web Applications](Module-14-Hacking-Web-Applications/Home.md) | ✅ Complete! |
| [Module 15: SQL Injection](Module-15-SQL-Injection/Home.md) | ✅ Complete! |
| [Module 16: Hacking Wireless Networks](Module-16-Hacking-Wireless-Networks/Home.md) | ✅ Complete! |
| [Module 17: Hacking Mobile Platforms](Module-17-Hacking-Mobile-Platforms/Home.md) | ✅ Complete! |
| [Module 18: IoT & OT Hacking](Module-18-IoT-and-OT-Hacking/Home.md) | ✅ Complete! |
| [Module 19: Cloud Computing](Module-19-Cloud-Computing/Home.md) | ✅ Complete! |
| [Module 20: Cryptography](Module-20-Cryptography/Home.md) | ✅ Complete! |
| [Module 21: AI-Powered Hacking](Module-21-AI-Powered-Ethical-Hacking/Home.md) | ✅ Complete! |

---

[⬅️ CEH v13 Home](../Home.md) | [🏠 Vault Home](../Home.md)
