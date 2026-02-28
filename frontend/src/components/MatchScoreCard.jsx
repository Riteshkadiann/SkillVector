import { t, eyebrow } from '../design';

function scoreColor(s)  { return s >= 75 ? t.green : s >= 50 ? t.amber : t.red; }
function scoreBg(s)     { return s >= 75 ? t.greenBg : s >= 50 ? t.amberBg : t.redBg; }
function scoreBorder(s) { return s >= 75 ? t.greenBorder : s >= 50 ? t.amberBorder : t.redBorder; }

export default function MatchScoreCard({ current, projected }) {
  const gain = Math.round(projected - current);
  const cc   = scoreColor(current);

  return (
    <div style={{
      background:   '#fff',
      border:       `1.5px solid ${t.border}`,
      borderRadius: 20,
      padding:      '36px 40px',
    }}>
      {/* ── Top bar ── */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 28 }}>
        <div>
          <div style={eyebrow}>Match Score</div>
          <div style={{ fontFamily: t.serif, fontSize: 28, fontWeight: 400, color: t.text, lineHeight: 1.2 }}>
            Your current alignment
          </div>
        </div>
        <div style={{
          padding: '8px 18px', background: t.greenBg, border: `1.5px solid ${t.greenBorder}`,
          borderRadius: 100, color: t.green, fontSize: 13, fontWeight: 600,
        }}>
          +{gain}% potential gain
        </div>
      </div>

      {/* ── Horizontal layout: score boxes + bars side by side ── */}
      <div style={{ display: 'grid', gridTemplateColumns: 'auto 40px auto 1fr', gap: '0 24px', alignItems: 'center' }}>

        {/* Current score box */}
        <div style={{
          padding: '28px 48px', background: scoreBg(current),
          border: `1.5px solid ${scoreBorder(current)}`, borderRadius: 16, textAlign: 'center', minWidth: 160,
        }}>
          <div style={{ fontFamily: t.serif, fontSize: 60, fontWeight: 400, lineHeight: 1, color: cc }}>
            {typeof current === 'number' ? current.toFixed ? current.toFixed(0) : current : current}%
          </div>
          <div style={{ fontSize: 11, color: t.faint, marginTop: 8, textTransform: 'uppercase', letterSpacing: '0.08em' }}>Current</div>
        </div>

        {/* Arrow */}
        <div style={{ textAlign: 'center', color: '#ccc', fontSize: 24 }}>→</div>

        {/* Projected score box */}
        <div style={{
          padding: '28px 48px', background: t.greenBg,
          border: `1.5px solid ${t.greenBorder}`, borderRadius: 16, textAlign: 'center', minWidth: 160,
        }}>
          <div style={{ fontFamily: t.serif, fontSize: 60, fontWeight: 400, lineHeight: 1, color: t.green }}>
            {typeof projected === 'number' ? projected.toFixed ? projected.toFixed(0) : projected : projected}%
          </div>
          <div style={{ fontSize: 11, color: t.faint, marginTop: 8, textTransform: 'uppercase', letterSpacing: '0.08em' }}>After Roadmap</div>
        </div>

        {/* Progress bars + tip — take remaining width */}
        <div style={{ paddingLeft: 8 }}>
          {[
            { label: 'Current match',            val: current,   color: cc      },
            { label: 'After completing roadmap', val: projected, color: t.green },
          ].map(({ label, val, color }) => (
            <div key={label} style={{ marginBottom: 12 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
                <span style={{ fontSize: 12, color: t.muted }}>{label}</span>
                <span style={{ fontSize: 12, fontWeight: 600, color: t.text }}>
                  {typeof val === 'number' && val % 1 !== 0 ? val.toFixed(1) : val}%
                </span>
              </div>
              <div style={{ height: 6, background: '#f0f0f0', borderRadius: 4, overflow: 'hidden' }}>
                <div style={{ width: `${Math.min(val, 100)}%`, height: '100%', background: color, borderRadius: 4, transition: 'width 0.8s ease' }} />
              </div>
            </div>
          ))}

          <div style={{
            marginTop: 16, padding: '12px 16px', background: t.surface,
            border: `1.5px solid ${t.border}`, borderRadius: 12,
            fontSize: 13, color: t.muted, lineHeight: 1.6,
          }}>
            Complete the roadmap below to close your skill gaps and reach{' '}
            <strong style={{ color: t.text }}>
              {typeof projected === 'number' && projected % 1 !== 0 ? projected.toFixed(1) : projected}%
            </strong> alignment with this role.
          </div>
        </div>

      </div>
    </div>
  );
}
