import { useState, useRef } from 'react';
import { uploadResumePDF, uploadResumeText } from '../utils/api';
import { t, card, inputBase, fieldLabel, eyebrow, sectionTitle } from '../design';

export default function UploadResume({ userId, onDone }) {
  const [file,      setFile]      = useState(null);
  const [text,      setText]      = useState('');
  const [dragging,  setDragging]  = useState(false);
  const [loading,   setLoading]   = useState(false);
  const [result,    setResult]    = useState(null);
  const fileRef = useRef();

  const handleDrop = (e) => {
    e.preventDefault();
    setDragging(false);
    const f = e.dataTransfer.files[0];
    if (f) setFile(f);
  };

  const handleFileSelect = (e) => {
    const f = e.target.files[0];
    if (f) setFile(f);
  };

  const handleSubmit = async () => {
    setLoading(true);
    try {
      let data;
      if (file) {
        data = await uploadResumePDF(userId, file);
      } else {
        data = await uploadResumeText(userId, text);
      }
      setResult(data.data);
      setTimeout(() => onDone(), 900);
    } catch (e) {
      alert('Error: ' + (e.response?.data?.detail || 'Something went wrong'));
    } finally {
      setLoading(false);
    }
  };

  const canSubmit = !loading && (file || text.trim().length > 50);

  return (
    <div style={card}>
      {/* Header */}
      <div style={{ marginBottom: 28 }}>
        <div style={eyebrow}>Step 01</div>
        <div style={sectionTitle}>Upload your resume</div>
        <div style={{ fontSize: 14, color: t.muted, fontWeight: 300, marginTop: 4 }}>
          We extract your skills and experience automatically using NLP.
        </div>
      </div>

      {/* Drop Zone */}
      <div
        onClick={() => fileRef.current?.click()}
        onDragOver={(e) => { e.preventDefault(); setDragging(true); }}
        onDragLeave={() => setDragging(false)}
        onDrop={handleDrop}
        style={{
          border:       `1.5px dashed ${dragging ? t.text : '#d8d8d8'}`,
          borderRadius: 14,
          padding:      '40px 32px',
          textAlign:    'center',
          cursor:       'pointer',
          transition:   'all 0.2s',
          background:   dragging ? t.surface : '#fdfdfd',
          marginBottom: 0,
        }}
      >
        <div style={{ fontSize: 26, marginBottom: 10 }}>{file ? '📄' : '↑'}</div>
        <div style={{ fontSize: 14, color: t.muted, marginBottom: 3 }}>
          {file ? file.name : 'Click or drag your resume here'}
        </div>
        <div style={{ fontSize: 12, color: t.faint }}>PDF · DOCX · TXT</div>
        <input
          ref={fileRef}
          type="file"
          accept=".pdf,.docx,.txt"
          style={{ display: 'none' }}
          onChange={handleFileSelect}
        />
      </div>

      {/* OR Divider */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 14, margin: '22px 0' }}>
        <div style={{ flex: 1, height: 1, background: t.border }} />
        <span style={{ fontSize: 11, color: t.faint, letterSpacing: '0.06em', textTransform: 'uppercase' }}>
          or paste text
        </span>
        <div style={{ flex: 1, height: 1, background: t.border }} />
      </div>

      {/* Textarea */}
      <div style={{ marginBottom: 22 }}>
        <label style={fieldLabel}>Resume Text</label>
        <textarea
          className="input-focus"
          placeholder="Paste your resume content here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          style={{ ...inputBase, minHeight: 160, resize: 'vertical' }}
        />
      </div>

      {/* Submit */}
      <button
        className="btn-primary btn-full"
        onClick={handleSubmit}
        disabled={!canSubmit}
      >
        {loading ? 'Processing…' : 'Continue →'}
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
          <span>{result.skill_count} skills found · {result.years_experience} years experience detected</span>
        </div>
      )}
    </div>
  );
}
