import useCountUp from '../hooks/useCountUp';
import { t } from '../design';

// ─── Single animated stat cell ────────────────────────────────────────────────
function StatCell({ num, label, sub, delay, isLast }) {
  // Parse "70%" → prefix:"", val:70, suffix:"%"
  //       "500+" → val:500, suffix:"+"
  //       "3 min"→ val:3,   suffix:" min"
  const match  = num.match(/^(\D*?)(\d+)(\D*)$/);
  const prefix = match ? match[1] : '';
  const numVal = match ? parseInt(match[2], 10) : 0;
  const suffix = match ? match[3] : num;

  const { ref, value } = useCountUp(numVal, 1200, delay);

  return (
    <div
      ref={ref}
      className="stat-cell"
      style={{ borderRight: isLast ? 'none' : `1px solid ${t.border}` }}
    >
      <div style={{
        fontFamily:  t.serif,
        fontSize:    52,
        fontWeight:  400,
        color:       t.text,
        lineHeight:  1,
        marginBottom: 10,
        transition:  'opacity 0.4s ease',
      }}>
        {prefix}{value}{suffix}
      </div>
      <div style={{ fontSize: 14, color: t.text,  fontWeight: 500, marginBottom: 4 }}>{label}</div>
      <div style={{ fontSize: 12, color: t.faint, fontWeight: 300 }}>{sub}</div>
    </div>
  );
}

// ─── Landing Page ─────────────────────────────────────────────────────────────
export default function Landing({ onStart }) {
  const stats = [
    { num: '70%',   label: 'Average match accuracy',  sub: 'Across 10k+ resume analyses'    },
    { num: '60',    label: 'Day structured roadmap',   sub: 'Week-by-week skill building'     },
    { num: '500+',  label: 'Skills tracked & mapped',  sub: 'Across every major industry'     },
    { num: '<1 min', label: 'To your full analysis',    sub: 'Resume to roadmap, instantly'    },
  ];

  const features = [
    {
      icon:  '⬡',
      title: 'NLP Skill Extraction',
      desc:  'Our engine parses your resume using natural language processing to identify every hard and soft skill you possess — no manual input needed.',
    },
    {
      icon:  '◎',
      title: 'Gap Intelligence',
      desc:  'We compare your skills against the exact job description and surface what\'s missing, ranked by importance and market frequency.',
    },
    {
      icon:  '◈',
      title: '60-Day Learning Roadmap',
      desc:  'Missing skills become a structured week-by-week plan with curated resources and micro-projects to build real proof of work.',
    },
    {
      icon:  '◉',
      title: 'Live Score Tracking',
      desc:  'Mark skills as learned and watch your match score recalculate in real time. Know exactly where you stand at every stage.',
    },
  ];

  return (
    <div className="fade-in">

      {/* ── Hero ── */}
      <div style={{ textAlign: 'center', padding: '64px 0 80px', maxWidth: 680, margin: '0 auto' }}>
        <div className="section-tag">AI Career Intelligence</div>
        <h1 style={{
          fontFamily:    t.serif,
          fontSize:      'clamp(44px, 6.5vw, 72px)',
          fontWeight:    400,
          lineHeight:    1.04,
          color:         t.text,
          marginBottom:  22,
          letterSpacing: '-0.02em',
        }}>
          Know precisely<br />
          <em style={{ fontStyle: 'italic', color: '#555' }}>what to learn next.</em>
        </h1>
        <p style={{
          fontSize:     16,
          color:        t.muted,
          lineHeight:   1.75,
          fontWeight:   300,
          maxWidth:     520,
          margin:       '0 auto 36px',
        }}>
          SkillVector analyzes your resume against any job description, surfaces your
          exact skill gaps, and generates a personalized 60-day learning roadmap —
          in seconds.
        </p>

        <div style={{ display: 'flex', gap: 12, justifyContent: 'center', flexWrap: 'wrap' }}>
          <button className="btn-primary" style={{ padding: '14px 32px', fontSize: 15 }} onClick={onStart}>
            Analyze my resume →
          </button>
          <button
            className="btn-outline"
            style={{ padding: '14px 32px', fontSize: 15 }}
            onClick={() => document.getElementById('how-it-works')?.scrollIntoView({ behavior: 'smooth' })}
          >
            See how it works
          </button>
        </div>

        <div style={{ marginTop: 24, fontSize: 12, color: t.faint }}>
          No account needed · Free to use · Instant results
        </div>
      </div>

      {/* ── Animated Stats ── */}
      <div style={{ borderTop: `1px solid ${t.border}`, borderBottom: `1px solid ${t.border}`, marginBottom: 88 }}>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))' }}>
          {stats.map((s, i) => (
            <StatCell
              key={i}
              num={s.num}
              label={s.label}
              sub={s.sub}
              delay={i * 120}
              isLast={i === stats.length - 1}
            />
          ))}
        </div>
      </div>

      {/* ── What SkillVector Does ── */}
      <div id="how-it-works" style={{ marginBottom: 88, scrollMarginTop: 80 }}>
        <div style={{ marginBottom: 48, maxWidth: 560 }}>
          <div className="section-tag">What We Do</div>
          <h2 style={{
            fontFamily:    t.serif,
            fontSize:      'clamp(32px, 4vw, 48px)',
            fontWeight:    400,
            color:         t.text,
            lineHeight:    1.1,
            marginBottom:  16,
            letterSpacing: '-0.01em',
          }}>
            The career intelligence layer<br />you've been missing.
          </h2>
          <p style={{ fontSize: 15, color: t.muted, lineHeight: 1.75, fontWeight: 300 }}>
            Most job seekers apply blindly — not knowing which skills are costing them
            the offer. SkillVector makes your gaps visible, quantifies them with a
            real match score, and tells you exactly what to learn with a structured plan.
          </p>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: 16 }}>
          {features.map((f, i) => (
            <div key={i} className="feature-card fade-up">
              <div style={{ fontSize: 22, marginBottom: 16, color: t.text }}>{f.icon}</div>
              <div style={{ fontSize: 16, fontWeight: 600, color: t.text, marginBottom: 10 }}>{f.title}</div>
              <div style={{ fontSize: 13, color: '#777', lineHeight: 1.7, fontWeight: 300 }}>{f.desc}</div>
            </div>
          ))}
        </div>
      </div>

      {/* ── About Section ── */}
      <div id="about" style={{ marginBottom: 88, scrollMarginTop: 80 }}>
        <div style={{
          display:   'grid',
          gridTemplateColumns: '1fr 1fr',
          gap:       64,
          alignItems: 'center',
          flexWrap:  'wrap',
        }}>
          {/* Left */}
          <div>
            <div className="section-tag">About SkillVector</div>
            <h2 style={{
              fontFamily:    t.serif,
              fontSize:      'clamp(28px, 3.5vw, 42px)',
              fontWeight:    400,
              color:         t.text,
              lineHeight:    1.1,
              marginBottom:  20,
              letterSpacing: '-0.01em',
            }}>
              Built for serious<br />job seekers.
            </h2>
            <p style={{ fontSize: 15, color: t.muted, lineHeight: 1.8, fontWeight: 300, marginBottom: 16 }}>
              SkillVector was built to solve a real problem — most people don't know why
              they're not getting callbacks. The answer is almost always a skills mismatch
              that nobody told them about.
            </p>
            <p style={{ fontSize: 15, color: t.muted, lineHeight: 1.8, fontWeight: 300, marginBottom: 28 }}>
              We use NLP, TF-IDF vectorization, and cosine similarity scoring — the same
              techniques used in enterprise hiring tools — and put them in your hands for free.
              No fluff, no generic advice. Just your exact gaps and a plan to close them.
            </p>
            <button className="btn-primary" style={{ padding: '12px 28px' }} onClick={onStart}>
              Try it now →
            </button>
          </div>

          {/* Right — Stack cards */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            {[
              { icon: '◎', title: 'NLP-powered parsing',    desc: 'spaCy + regex extracts skills from any resume format' },
              { icon: '◈', title: 'TF-IDF match scoring',   desc: 'Cosine similarity gives you a real % fit — not a guess' },
              { icon: '⬡', title: 'Personalized roadmaps',  desc: 'Each plan is unique to your gaps, not a generic list' },
              { icon: '◉', title: 'Real-time recalculation',desc: 'Score updates live as you mark skills complete' },
            ].map((item, i) => (
              <div key={i} style={{
                display:      'flex',
                alignItems:   'flex-start',
                gap:          14,
                padding:      '16px 20px',
                border:       `1.5px solid ${t.border}`,
                borderRadius: 14,
                background:   '#fff',
                transition:   'border-color 0.2s',
              }}
                onMouseEnter={e => e.currentTarget.style.borderColor = t.text}
                onMouseLeave={e => e.currentTarget.style.borderColor = t.border}
              >
                <div style={{ fontSize: 18, flexShrink: 0, marginTop: 1, color: t.text }}>{item.icon}</div>
                <div>
                  <div style={{ fontSize: 14, fontWeight: 600, color: t.text, marginBottom: 3 }}>{item.title}</div>
                  <div style={{ fontSize: 13, color: t.muted, fontWeight: 300 }}>{item.desc}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* ── CTA Block ── */}
      <div style={{
        textAlign:    'center',
        padding:      '64px 40px',
        background:   t.text,
        borderRadius: 24,
        marginBottom: 40,
      }}>
        <div style={{
          fontFamily:    t.serif,
          fontSize:      'clamp(28px, 4vw, 46px)',
          fontWeight:    400,
          color:         '#f0ece3',
          marginBottom:  14,
          lineHeight:    1.1,
          letterSpacing: '-0.01em',
        }}>
          Ready to close the gap?
        </div>
        <p style={{ fontSize: 14, color: 'rgba(255,255,255,0.4)', marginBottom: 28, fontWeight: 300 }}>
          Upload your resume and get your full analysis in seconds.
        </p>
        <button
          onClick={onStart}
          style={{
            display:     'inline-flex',
            padding:     '13px 30px',
            background:  '#f0ece3',
            color:       t.text,
            border:      'none',
            borderRadius: 100,
            fontFamily:  t.sans,
            fontSize:    14,
            fontWeight:  600,
            cursor:      'pointer',
            transition:  'all 0.2s',
          }}
          onMouseEnter={e => e.currentTarget.style.background = '#fff'}
          onMouseLeave={e => e.currentTarget.style.background = '#f0ece3'}
        >
          Get started — it's free →
        </button>
      </div>
    </div>
  );
}
