import { useState } from 'react';
import { updateProgress } from '../utils/api';
import { t, eyebrow } from '../design';

export default function ProgressTracker({ userId, skills }) {
  const [checked, setChecked] = useState([]);
  const [loading, setLoading] = useState(false);
  const [result,  setResult]  = useState(null);

  const toggle = (skill) =>
    setChecked(prev =>
      prev.includes(skill) ? prev.filter(s => s !== skill) : [...prev, skill]
    );

  const handleSubmit = async () => {
    if (checked.length === 0) return;
    setLoading(true);
    try {
      const data = await updateProgress(userId, checked);
      setResult(data);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  if (!skills || skills.length === 0) return null;

  const pct = Math.round((checked.length / skills.length) * 100);

  return (
    <div style={{ background: '#fff', border: `1.5px solid ${t.border}`, borderRadius: 20, padding: '36px 40px' }}>
      <div style={{ marginBottom: 28 }}>
        <div style={eyebrow}>Progress Tracker</div>
        <div style={{ fontFamily: t.serif, fontSize: 28, fontWeight: 400, color: t.text, lineHeight: 1.2 }}>
          Mark skills as learned
        </div>
        <div style={{ fontSize: 13, color: t.muted, marginTop: 8 }}>
          Check off acquired skills to recalculate your match score in real time.
        </div>
      </div>

      <div style={{ marginBottom: 28 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8 }}>
          <span style={{ fontSize: 13, color: t.muted }}>{checked.length} of {skills.length} completed</span>
          <span style={{ fontSize: 13, fontWeight: 600, color: pct > 0 ? t.green : t.faint }}>{pct}%</span>
        </div>
        <div style={{ height: 6, background: '#f0f0f0', borderRadius: 4, overflow: 'hidden' }}>
          <div style={{ width: `${pct}%`, height: '100%', background: t.green, borderRadius: 4, transition: 'width 0.5s ease' }} />
        </div>
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))',
        gap: 10,
        marginBottom: 28,
      }}>
        {skills.map(skill => {
          const on = checked.includes(skill);
          return (
            <div
              key={skill}
              className={`tracker-item${on ? ' checked' : ''}`}
              onClick={() => toggle(skill)}
            >
              <div style={{
                width: 17, height: 17, borderRadius: 4, flexShrink: 0,
                border: `1.5px solid ${on ? t.green : '#d0d0d0'}`,
                background: on ? t.green : '#fff',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                fontSize: 10, color: '#fff', fontWeight: 700, transition: 'all 0.18s',
              }}>
                {on ? '✓' : ''}
              </div>
              <span style={{ fontSize: 13, color: on ? t.green : '#555', fontWeight: on ? 500 : 400, transition: 'color 0.18s' }}>
                {skill}
              </span>
            </div>
          );
        })}
      </div>

      {/* Submit */}
      <button
        className="btn-primary btn-full"
        onClick={handleSubmit}
        disabled={loading || checked.length === 0}
      >
        {loading ? 'Recalculating…' : 'Recalculate My Score →'}
      </button>

      {/* Result */}
      {result && (
        <div style={{
          marginTop: 20, padding: '20px 24px',
          background: t.greenBg, border: `1.5px solid ${t.greenBorder}`,
          borderRadius: 14, display: 'flex', alignItems: 'center', gap: 20,
        }}>
          <div style={{ fontFamily: t.serif, fontSize: 48, color: t.green, fontWeight: 400, lineHeight: 1 }}>
            {result.updated_match_score}%
          </div>
          <div>
            <div style={{ fontSize: 15, color: t.green, fontWeight: 600 }}>Updated match score</div>
            <div style={{ fontSize: 13, color: t.muted, marginTop: 4 }}>{result.message}</div>
          </div>
        </div>
      )}
    </div>
  );
}
