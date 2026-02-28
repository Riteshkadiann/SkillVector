import { useState } from 'react';
import { analyzeJob } from '../utils/api';
import { t, card, inputBase, fieldLabel, eyebrow, sectionTitle } from '../design';

export default function JobInput({ userId, onDone }) {
  const [jobTitle, setJobTitle] = useState('');
  const [jobDesc,  setJobDesc]  = useState('');
  const [loading,  setLoading]  = useState(false);
  const [result,   setResult]   = useState(null);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const data = await analyzeJob(userId, jobTitle, jobDesc);
      setResult(data.data);
      setTimeout(() => onDone(), 900);
    } catch (e) {
      alert('Error: ' + (e.response?.data?.detail || 'Something went wrong'));
    } finally {
      setLoading(false);
    }
  };

  const canSubmit = !loading && jobTitle.trim() && jobDesc.trim().length > 50;

  return (
    <div style={card}>
      {/* Header */}
      <div style={{ marginBottom: 28 }}>
        <div style={eyebrow}>Step 02</div>
        <div style={sectionTitle}>Paste a job description</div>
        <div style={{ fontSize: 14, color: t.muted, fontWeight: 300, marginTop: 4 }}>
          We'll extract required skills and instantly calculate your fit.
        </div>
      </div>

      {/* Job Title */}
      <div style={{ marginBottom: 18 }}>
        <label style={fieldLabel}>Job Title</label>
        <input
          type="text"
          className="input-focus"
          placeholder="e.g. Senior Backend Engineer"
          value={jobTitle}
          onChange={(e) => setJobTitle(e.target.value)}
          style={inputBase}
        />
      </div>

      {/* Job Description */}
      <div style={{ marginBottom: 24 }}>
        <label style={fieldLabel}>Job Description</label>
        <textarea
          className="input-focus"
          placeholder="Paste the full job description here…"
          value={jobDesc}
          onChange={(e) => setJobDesc(e.target.value)}
          style={{ ...inputBase, minHeight: 240, resize: 'vertical' }}
        />
        <div style={{ fontSize: 11, color: t.faint, marginTop: 6 }}>
          {jobDesc.trim().length} characters — minimum 50 required
        </div>
      </div>

      {/* Submit */}
      <button
        className="btn-primary btn-full"
        onClick={handleSubmit}
        disabled={!canSubmit}
      >
        {loading ? 'Analyzing…' : 'Generate Analysis →'}
      </button>

      {/* Success */}
      {result && (
        <div style={{
          marginTop:    16,
          padding:      '12px 16px',
          background:   t.greenBg,
          border:       `1px solid ${t.greenBorder}`,
          borderRadius: 8,
          color:        t.green,
          fontSize:     13,
          display:      'flex',
          gap:          8,
        }}>
          <span>✓</span>
          <span>Extracted {result.total_skill_count} skills from job description</span>
        </div>
      )}
    </div>
  );
}
