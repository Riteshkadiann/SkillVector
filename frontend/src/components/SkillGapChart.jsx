import { t, eyebrow } from '../design';

const RANK_COLORS = [
  { bg: '#fff7ed', border: '#fed7aa', color: '#c2410c' },
  { bg: '#fefce8', border: '#fde68a', color: '#a16207' },
  { bg: '#f5f5f5', border: '#e5e5e5', color: '#555'    },
  { bg: '#fafafa', border: '#ebebeb', color: '#888'    },
];

function deduplicateSkills(skills) {
  const lower = skills.map(s => s.toLowerCase().trim());
  // Remove any skill that is a prefix of a longer skill in the same list
  const keep = skills.filter((_, i) =>
    !lower.some((other, j) => i !== j && other.startsWith(lower[i]) && other !== lower[i])
  );
  // Final exact-match dedup
  const seen = new Set();
  return keep.filter(s => {
    const k = s.toLowerCase().trim();
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });
}

const cardStyle = {
  background:   '#fff',
  border:       `1.5px solid ${t.border}`,
  borderRadius: 20,
  padding:      '32px 36px',
};

export default function SkillGapChart({ userSkills, missingSkills, prioritySkills }) {
  const cleanUser    = deduplicateSkills(userSkills);
  const cleanMissing = deduplicateSkills(missingSkills);

  return (
    <div>
      {/* Section header */}
      <div style={{ marginBottom: 20 }}>
        <div style={eyebrow}>Gap Analysis</div>
        <div style={{ fontFamily: t.serif, fontSize: 28, fontWeight: 400, color: t.text, lineHeight: 1.2 }}>
          What you have vs. what's needed
        </div>
      </div>

      {/* ── ROW 1: You Have (left) | Missing (right) ── */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20, marginBottom: 20 }}>

        {/* You Have */}
        <div style={cardStyle}>
          <div style={{ fontSize: 11, fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.06em', color: t.green, marginBottom: 14 }}>
            ✓ You have ({cleanUser.length})
          </div>
          <div>
            {cleanUser.map(s => <span key={s} className="pill pill-green">{s}</span>)}
          </div>
        </div>

        {/* Missing */}
        <div style={cardStyle}>
          <div style={{ fontSize: 11, fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.06em', color: t.red, marginBottom: 14 }}>
            ✗ Missing ({cleanMissing.length})
          </div>
          <div>
            {cleanMissing.map(s => <span key={s} className="pill pill-red">{s}</span>)}
          </div>
        </div>

      </div>

      {/* ── ROW 2: Top Priority Skills — full width below ── */}
      <div style={cardStyle}>
        <div style={{ fontSize: 11, fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.06em', color: t.faint, marginBottom: 20 }}>
          Top Priority Skills to Learn
        </div>

        {/* Priority skills in a 2-column grid for space efficiency */}
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0 32px' }}>
          {prioritySkills.map((item, i) => {
            const rs = RANK_COLORS[Math.min(i, RANK_COLORS.length - 1)];
            return (
              <div key={item.skill} className="priority-row">
                <div style={{
                  width: 28, height: 28, borderRadius: '50%', flexShrink: 0,
                  background: rs.bg, border: `1.5px solid ${rs.border}`,
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontSize: 11, fontWeight: 700, color: rs.color,
                }}>
                  {i + 1}
                </div>
                <div style={{ flex: 1 }}>
                  <div style={{ fontWeight: 500, fontSize: 14, color: t.text }}>
                    {item.skill.charAt(0).toUpperCase() + item.skill.slice(1)}
                  </div>
                  <div style={{ fontSize: 12, color: t.faint, marginTop: 2 }}>
                    Importance: {(item.importance_score * 100).toFixed(0)}% · Appears in {item.frequency} posting{item.frequency !== 1 ? 's' : ''}
                  </div>
                </div>
                <div style={{ fontSize: 11, fontWeight: 600, color: rs.color }}>#{i + 1}</div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
