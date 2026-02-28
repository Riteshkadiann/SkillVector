import { t, eyebrow } from '../design';

const WEEK_COLORS = [
  '#2563eb','#7c3aed','#0891b2','#059669',
  '#d97706','#dc2626','#64748b','#16a34a',
];

// Skills where uploading to GitHub makes sense
const GITHUB_SKILLS = new Set([
  'python','javascript','typescript','java','c#','c++','c','go','rust',
  'kotlin','swift','php','ruby','scala','r','bash','shell scripting',
  'react','angular','vue','nextjs','svelte','django','flask','fastapi',
  'express','express.js','node.js','nestjs','graphql','rest api','rest apis',
  'postgresql','mysql','mongodb','redis','sql','database design',
  'aws','gcp','azure','docker','kubernetes','terraform','ci/cd','github actions','linux',
  'machine learning','deep learning','nlp','computer vision','pytorch','tensorflow',
  'scikit-learn','pandas','numpy','langchain','openai api','data structures','algorithms',
  'oop','system design','microservices','distributed systems','operating systems',
  'pytest','jest','cypress','unit testing','typescript','rails','ruby on rails',
  'fastapi','django','flask','vba','asp.net','.net',
]);

// Skills where "Ask AI" tip is genuinely helpful (learning concepts, not doing tasks)
const ASK_AI_SKILLS = new Set([
  'concierge','hospitality','property services','building compliance','front-of-house',
  'interpersonal communication','organizational aptitude','multi-tasking','scheduling',
  'customer service','communication','leadership','collaboration','agile',
  'verbal de-escalation','de-escalation','conflict resolution','situational awareness',
  'incident reporting','emergency response','radio communication','security protocols',
  'amenities management','property management','digital signage','documentation',
  'whmis','aoda','ohsa','first aid','cpr','patrolling','surveillance',
]);

export default function RoadmapTimeline({ roadmap }) {
  if (!roadmap || roadmap.length === 0) return null;

  return (
    <div style={{ background: '#fff', border: `1.5px solid ${t.border}`, borderRadius: 20, padding: '36px 40px' }}>
      <div style={{ marginBottom: 32 }}>
        <div style={eyebrow}>60-Day Plan</div>
        <div style={{ fontFamily: t.serif, fontSize: 28, fontWeight: 400, color: t.text, lineHeight: 1.2 }}>
          Your personalized learning roadmap
        </div>
      </div>

      <div style={{ position: 'relative' }}>
        <div style={{ position: 'absolute', left: 72, top: 0, bottom: 0, width: 1, background: t.border }} />

        {roadmap.map((item, i) => {
          const c = WEEK_COLORS[i % WEEK_COLORS.length];
          const skillLower = item.skill.toLowerCase().trim();

          // GitHub pill: only for tech/coding skills
          const showGithub = GITHUB_SKILLS.has(skillLower);

          // Ask AI pill: only for concept/non-tech skills, and only every other one (not consecutive)
          const showAskAI = ASK_AI_SKILLS.has(skillLower) && i % 2 === 0;

          const aiLabels = [
            "Ask ChatGPT to quiz you on this",
            "Ask Claude for a study plan",
            "Ask Gemini for real examples",
            "Ask ChatGPT to explain edge cases",
          ];
          const aiLabel = aiLabels[i % aiLabels.length];

          return (
            <div key={i} style={{ display: 'flex', gap: 24, marginBottom: i < roadmap.length - 1 ? 20 : 0, alignItems: 'flex-start' }}>

              {/* Week badge */}
              <div style={{ width: 144, flexShrink: 0, display: 'flex', justifyContent: 'center', paddingTop: 16, position: 'relative', zIndex: 1 }}>
                <div style={{
                  padding: '6px 12px', borderRadius: 8,
                  background: `${c}12`, border: `1.5px solid ${c}30`,
                  color: c, fontSize: 10, fontWeight: 700,
                  letterSpacing: '0.07em', textTransform: 'uppercase', whiteSpace: 'nowrap',
                }}>
                  {item.week}
                </div>
              </div>

              {/* Content */}
              <div style={{
                flex: 1,
                background: `${c}06`,
                border: `1.5px solid ${c}20`,
                borderLeft: `4px solid ${c}60`,
                borderRadius: '0 14px 14px 0',
                padding: '16px 24px',
              }}>
                <div style={{ fontWeight: 600, fontSize: 16, color: t.text, marginBottom: 8 }}>
                  {item.skill.charAt(0).toUpperCase() + item.skill.slice(1)}
                </div>
                <div style={{ fontSize: 13, color: t.muted, marginBottom: 12, lineHeight: 1.6 }}>
                  <span style={{ color: t.faint, fontWeight: 500 }}>Project: </span>
                  {item.micro_project}
                </div>
                <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, alignItems: 'center' }}>
                  {item.resources.map(r => (
                    <span key={r} style={{
                      fontSize: 12, padding: '4px 12px', borderRadius: 6,
                      background: t.blueBg, border: `1px solid ${t.blueBorder}`,
                      color: t.blue, fontWeight: 500,
                    }}>
                      {r}
                    </span>
                  ))}

                  {/* Upload to GitHub — tech skills only */}
                  {showGithub && (
                    <span style={{
                      fontSize: 12, padding: '4px 12px', borderRadius: 6,
                      background: '#f0fdf4', border: '1px solid #bbf7d0',
                      color: '#15803d', fontWeight: 600,
                    }}>
                      ↗ Upload to GitHub
                    </span>
                  )}

                  {/* Ask AI — non-tech skills, alternating */}
                  {showAskAI && (
                    <span style={{
                      fontSize: 12, padding: '4px 12px', borderRadius: 6,
                      background: '#faf5ff', border: '1px solid #e9d5ff',
                      color: '#7c3aed', fontWeight: 500,
                    }}>
                      💬 {aiLabel}
                    </span>
                  )}
                </div>
              </div>

            </div>
          );
        })}
      </div>
    </div>
  );
}
