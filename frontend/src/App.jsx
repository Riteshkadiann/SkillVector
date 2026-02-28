import { useState } from 'react';
import Landing        from './components/Landing';
import UploadResume   from './components/UploadResume';
import JobInput       from './components/JobInput';
import Results        from './components/Results';
import { getSkillGap, getRoadmap } from './utils/api';
import { t, GLOBAL_CSS } from './design';

const USER_ID = 'user_001';

// ─── Stepper ──────────────────────────────────────────────────────────────────
function Stepper({ step }) {
  const steps = ['Resume', 'Job Description', 'Results'];
  return (
    <div style={{
      display:       'flex',
      alignItems:    'flex-start',
      maxWidth:      480,
      margin:        '0 auto 52px',
    }}>
      {steps.map((label, i) => {
        const num   = i + 1;
        const state = step === num ? 'active' : step > num ? 'done' : 'idle';
        const isLast = i === steps.length - 1;
        return (
          <div key={label} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', flex: 1 }}>
            <div style={{ display: 'flex', alignItems: 'center', width: '100%' }}>
              {i > 0 && (
                <div style={{
                  flex:       1,
                  height:     1.5,
                  marginTop:  17,
                  background: step > i ? t.text : t.border,
                  transition: 'background 0.4s',
                }} />
              )}
              <div style={{
                width:        34,
                height:       34,
                borderRadius: '50%',
                flexShrink:   0,
                display:      'flex',
                alignItems:   'center',
                justifyContent: 'center',
                fontSize:     12,
                fontWeight:   600,
                transition:   'all 0.35s',
                ...(state === 'active'
                  ? { background: t.text,    color: '#fff'  }
                  : state === 'done'
                  ? { background: '#f5f5f5', color: t.text, border: `1.5px solid ${t.text}` }
                  : { background: '#f5f5f5', color: '#bbb', border: `1.5px solid ${t.border}` }),
              }}>
                {state === 'done' ? '✓' : num}
              </div>
              {!isLast && (
                <div style={{
                  flex:       1,
                  height:     1.5,
                  marginTop:  17,
                  background: step > num ? t.text : t.border,
                  transition: 'background 0.4s',
                }} />
              )}
            </div>
            <div style={{
              fontSize:      11,
              letterSpacing: '0.05em',
              marginTop:     9,
              fontWeight:    500,
              textTransform: 'uppercase',
              whiteSpace:    'nowrap',
              color:         state === 'idle' ? '#bbb' : t.text,
            }}>
              {label}
            </div>
          </div>
        );
      })}
    </div>
  );
}

// ─── Loading Spinner ──────────────────────────────────────────────────────────
function Spinner() {
  return (
    <div style={{ textAlign: 'center', padding: '80px 0' }}>
      <div style={{
        width:        32,
        height:       32,
        borderRadius: '50%',
        border:       `2px solid ${t.border}`,
        borderTopColor: t.text,
        animation:    'spin 0.7s linear infinite',
        margin:       '0 auto 16px',
      }} />
      <div style={{ fontSize: 14, color: t.faint }}>Analyzing skill gaps…</div>
    </div>
  );
}

// ─── App Root ─────────────────────────────────────────────────────────────────
export default function App() {
  const [view,        setView]        = useState('landing'); // 'landing' | 'app'
  const [step,        setStep]        = useState(1);
  const [loading,     setLoading]     = useState(false);
  const [gapData,     setGapData]     = useState(null);
  const [roadmapData, setRoadmapData] = useState(null);

  const startApp = () => {
    setView('app');
    setStep(1);
    setGapData(null);
    setRoadmapData(null);
  };

  const handleResumeUploaded = () => setStep(2);

  const handleJobAnalyzed = async () => {
    setStep(3);
    setLoading(true);
    try {
      const [gap, roadmap] = await Promise.all([
        getSkillGap(USER_ID),
        getRoadmap(USER_ID),
      ]);
      setGapData(gap);
      setRoadmapData(roadmap);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ background: t.bg, minHeight: '100vh', fontFamily: t.sans, color: t.text }}>
      <style>{GLOBAL_CSS}</style>

      {/* ── Sticky Nav ── */}
      <nav style={{
        position:       'sticky',
        top:            0,
        zIndex:         100,
        background:     'rgba(255,255,255,0.92)',
        backdropFilter: 'blur(12px)',
        borderBottom:   `1px solid ${t.border}`,
      }}>
        <div style={{
          maxWidth:      1100,
          margin:        '0 auto',
          padding:       '0 32px',
          display:       'flex',
          alignItems:    'center',
          justifyContent: 'space-between',
          height:        60,
        }}>
          {/* Logo */}
          <div
            style={{ fontFamily: t.serif, fontSize: 20, fontWeight: 400, cursor: 'pointer', letterSpacing: '-0.01em' }}
            onClick={() => {
              setView('landing');
              setStep(1);
              window.scrollTo({ top: 0, behavior: 'smooth' });
            }}
          >
            SkillVector
          </div>

          {/* Nav right */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 28 }}>
            <span
              className="nav-link"
              onClick={() => {
                if (view !== 'landing') { setView('landing'); setStep(1); setTimeout(() => document.getElementById('how-it-works')?.scrollIntoView({ behavior: 'smooth' }), 100); }
                else document.getElementById('how-it-works')?.scrollIntoView({ behavior: 'smooth' });
              }}
            >
              How it works
            </span>
            <span
              className="nav-link"
              onClick={() => {
                if (view !== 'landing') { setView('landing'); setStep(1); setTimeout(() => document.getElementById('about')?.scrollIntoView({ behavior: 'smooth' }), 100); }
                else document.getElementById('about')?.scrollIntoView({ behavior: 'smooth' });
              }}
            >
              About
            </span>
            <button className="btn-primary" style={{ padding: '9px 20px', fontSize: 13 }} onClick={startApp}>
              Get started
            </button>
          </div>
        </div>
      </nav>

      {/* ── Main Content ── */}
      <main style={{
        maxWidth: view === 'landing' ? 1100 : 1200,
        margin:   '0 auto',
        padding:  view === 'landing' ? '0 32px 80px' : '48px 40px 100px',
      }}>

        {/* Landing view */}
        {view === 'landing' && <Landing onStart={startApp} />}

        {/* App view */}
        {view === 'app' && (
          <>
            <div style={{ textAlign: 'center', marginBottom: 48 }}>
              <h2 style={{
                fontFamily:    t.serif,
                fontSize:      34,
                fontWeight:    400,
                color:         t.text,
                marginBottom:  8,
                letterSpacing: '-0.01em',
              }}>
                Career Analysis
              </h2>
              <p style={{ fontSize: 14, color: t.faint, fontWeight: 300 }}>
                Simple, instant, data-driven
              </p>
            </div>

            <Stepper step={step} />

            <div key={step} className="fade-up">
              {step === 1 && (
                <UploadResume userId={USER_ID} onDone={handleResumeUploaded} />
              )}
              {step === 2 && (
                <JobInput userId={USER_ID} onDone={handleJobAnalyzed} />
              )}
              {step === 3 && loading && <Spinner />}
              {step === 3 && !loading && (
                <Results
                  gapData={gapData}
                  roadmapData={roadmapData}
                  userId={USER_ID}
                  onReset={startApp}
                />
              )}
            </div>
          </>
        )}
      </main>

      {/* ── Footer ── */}
      <footer style={{ borderTop: `1px solid ${t.border}`, padding: '28px 32px' }}>
        <div style={{
          maxWidth:      1100,
          margin:        '0 auto',
          display:       'flex',
          alignItems:    'center',
          justifyContent: 'space-between',
          flexWrap:      'wrap',
          gap:           12,
        }}>
          <div style={{ fontFamily: t.serif, fontSize: 16 }}>SkillVector</div>
          <div style={{ fontSize: 12, color: t.faint }}>AI-powered career intelligence</div>
        </div>
      </footer>
    </div>
  );
}
