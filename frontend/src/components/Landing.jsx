import useCountUp from '../hooks/useCountUp';
import CreatorSignature from './CreatorSignature';
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
    { num: '60 Days',    label: 'Structured Learning Roadmap',   sub: 'Week-by-week execution'     },
    { num: '500+ Skills',  label: 'Tracked across industries',  sub: 'From tech to marketing'     },
    { num: '<1 min', label: 'To your full analysis',    sub: 'Resume to roadmap, instantly'    },
  ];

  const features = [
    {
      icon:  '⬡',
      title: 'NLP Skill Extraction',
      desc:  'We parse your resume using NLP to identify your real skill set — no manual input.',
    },
    {
      icon:  '◎',
      title: 'Gap Intelligence',
      desc:  'We compare your profile to job requirements and rank missing skills by impact.',
    },
    {
      icon:  '◈',
      title: '60-Day Learning Roadmap',
      desc:  'Get a structured, week-by-week plan with curated resources and real projects.',
    },
    {
      icon:  '◉',
      title: 'Live Score Tracking',
      desc:  'Track progress in real time as your match score updates instantly.',
    },
  ];

  return (
    <div className="fade-in">

      {/* ── Hero ── */}
      <div style={{ textAlign: 'center', padding: '80px 0 100px', maxWidth: 720, margin: '0 auto' }}>
        <div className="section-tag">AI Career Intelligence</div>
        <h1 style={{
          fontFamily:    t.serif,
          fontSize:      'clamp(48px, 7vw, 76px)',
          fontWeight:    400,
          lineHeight:    1.08,
          color:         t.text,
          marginBottom:  24,
          letterSpacing: '-0.025em',
        }}>
          Know precisely<br />
          <em style={{ fontStyle: 'italic', color: '#6b7280', fontWeight: 400 }}>what to learn next.</em>
        </h1>
        <p style={{
          fontSize:     'clamp(15px, 2.2vw, 18px)',
          color:        t.muted,
          lineHeight:   1.8,
          fontWeight:   400,
          maxWidth:     560,
          margin:       '0 auto 44px',
        }}>
          SkillVector analyzes your resume against real job descriptions, identifies your exact skill gaps, and generates a personalized roadmap to close them — in seconds.
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
      <div style={{ borderTop: `1px solid ${t.border}`, borderBottom: `1px solid ${t.border}`, marginBottom: 100 }}>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))' }}>
          {stats.map((s, i) => (
            <StatCell
              key={i}
              num={s.num}
              label={s.label}
              sub={s.sub}
              delay={i * 100}
              isLast={i === stats.length - 1}
            />
          ))}
        </div>
      </div>

      {/* ── What SkillVector Does ── */}
      <div id="how-it-works" style={{ marginBottom: 100, scrollMarginTop: 80 }}>
        <div style={{ marginBottom: 56, maxWidth: 600 }}>
          <div className="section-tag">What We Do</div>
          <h2 style={{
            fontFamily:    t.serif,
            fontSize:      'clamp(36px, 4.5vw, 52px)',
            fontWeight:    400,
            color:         t.text,
            lineHeight:    1.1,
            marginBottom:  20,
            letterSpacing: '-0.015em',
          }}>
            The career intelligence<br />layer you've been missing.
          </h2>
          <p style={{ fontSize: 15, color: t.muted, lineHeight: 1.8, fontWeight: 300 }}>
            Most job seekers apply blindly — not knowing which skills are costing them the offer. SkillVector makes your gaps visible, quantifies them with a real match score, and tells you exactly what to learn with a structured plan.
          </p>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 20 }}>
          {features.map((f, i) => (
            <div key={i} className="feature-card fade-up" style={{ animationDelay: `${i * 70}ms` }}>
              <div style={{ fontSize: 28, marginBottom: 18, color: t.primary }}>{f.icon}</div>
              <div style={{ fontSize: 17, fontWeight: 600, color: t.text, marginBottom: 12 }}>{f.title}</div>
              <div style={{ fontSize: 14, color: '#666', lineHeight: 1.7, fontWeight: 300 }}>{f.desc}</div>
            </div>
          ))}
        </div>
      </div>

      {/* ── About Section ── */}
      <div id="about" style={{ marginBottom: 100, scrollMarginTop: 80 }}>
        <div style={{
          display:   'grid',
          gridTemplateColumns: '1fr 1fr',
          gap:       72,
          alignItems: 'center',
          flexWrap:  'wrap',
        }}>
          {/* Left */}
          <div>
            <div className="section-tag">About SkillVector</div>
            <h2 style={{
              fontFamily:    t.serif,
              fontSize:      'clamp(32px, 4vw, 48px)',
              fontWeight:    400,
              color:         t.text,
              lineHeight:    1.1,
              marginBottom:  24,
              letterSpacing: '-0.015em',
            }}>
              Built for serious<br />job seekers.
            </h2>
            <p style={{ fontSize: 15, color: t.muted, lineHeight: 1.8, fontWeight: 300, marginBottom: 18 }}>
              SkillVector was built to solve a real problem — most people don't know why
              they're not getting callbacks. The answer is almost always a skills mismatch
              that nobody told them about.
            </p>
            <p style={{ fontSize: 15, color: t.muted, lineHeight: 1.8, fontWeight: 300, marginBottom: 32 }}>
              We use NLP, TF-IDF vectorization, and cosine similarity scoring — the same
              techniques used in enterprise hiring tools — and put them in your hands for free.
              No fluff, no generic advice. Just your exact gaps and a plan to close them.
            </p>
            <button className="btn-primary" style={{ padding: '14px 32px', fontSize: 14 }} onClick={onStart}>
              Try it now →
            </button>
          </div>

          {/* Right — Stack cards */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
            {[
              { icon: '◎', title: 'NLP-powered parsing',    desc: 'spaCy + regex extracts skills from any resume format' },
              { icon: '◈', title: 'TF-IDF match scoring',   desc: 'Cosine similarity gives you a real % fit — not a guess' },
              { icon: '⬡', title: 'Personalized roadmaps',  desc: 'Each plan is unique to your gaps, not a generic list' },
              { icon: '◉', title: 'Real-time recalculation',desc: 'Score updates live as you mark skills complete' },
            ].map((item, i) => (
              <div key={i} style={{
                display:      'flex',
                alignItems:   'flex-start',
                gap:          16,
                padding:      '18px 22px',
                border:       `1px solid ${t.border}`,
                borderRadius: 14,
                background:   '#fff',
                transition:   'all 0.3s cubic-bezier(0.22,1,0.36,1)',
              }}
                onMouseEnter={e => {
                  e.currentTarget.style.borderColor = t.primary;
                  e.currentTarget.style.background = '#f0f9ff';
                  e.currentTarget.style.transform = 'translateX(4px)';
                }}
                onMouseLeave={e => {
                  e.currentTarget.style.borderColor = t.border;
                  e.currentTarget.style.background = '#fff';
                  e.currentTarget.style.transform = 'translateX(0)';
                }}
              >
                <div style={{ fontSize: 20, flexShrink: 0, marginTop: 2, color: t.primary }}>{item.icon}</div>
                <div>
                  <div style={{ fontSize: 15, fontWeight: 600, color: t.text, marginBottom: 4 }}>{item.title}</div>
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
        padding:      '80px 60px',
        background:   `linear-gradient(135deg, ${t.darkBg} 0%, #1e293b 100%)`,
        borderRadius: 24,
        marginBottom: 40,
        boxShadow:    '0 20px 40px rgba(0, 0, 0, 0.12)',
      }}>
        <div style={{
          fontFamily:    t.serif,
          fontSize:      'clamp(32px, 5vw, 48px)',
          fontWeight:    400,
          color:         '#f8fafc',
          marginBottom:  16,
          lineHeight:    1.1,
          letterSpacing: '-0.015em',
        }}>
          Ready to close the gap?
        </div>
        <p style={{ fontSize: 16, color: 'rgba(255,255,255,0.6)', marginBottom: 32, fontWeight: 300, maxWidth: 600, margin: '0 auto 32px' }}>
          Upload your resume and get your full analysis in seconds. Start your transformation today.
        </p>
        <button
          onClick={onStart}
          style={{
            display:     'inline-flex',
            padding:     '14px 36px',
            background:  '#fff',
            color:       t.darkBg,
            border:      'none',
            borderRadius: 12,
            fontFamily:  t.sans,
            fontSize:    14,
            fontWeight:  600,
            cursor:      'pointer',
            transition:  'all 0.3s cubic-bezier(0.22,1,0.36,1)',
            boxShadow:   '0 8px 24px rgba(0,0,0,0.12)',
          }}
          onMouseEnter={e => {
            e.currentTarget.style.background = '#f0f9ff';
            e.currentTarget.style.transform = 'translateY(-2px)';
            e.currentTarget.style.boxShadow = '0 12px 32px rgba(0,0,0,0.16)';
          }}
          onMouseLeave={e => {
            e.currentTarget.style.background = '#fff';
            e.currentTarget.style.transform = 'translateY(0)';
            e.currentTarget.style.boxShadow = '0 8px 24px rgba(0,0,0,0.12)';
          }}
        >
          Get started — it's free →
        </button>
      </div>

      <CreatorSignature />
    </div>
  );
}
