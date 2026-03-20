import { t } from '../design';

export default function CreatorSignature() {
  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: 32,
      padding: '72px 48px',
      marginBottom: 0,
      borderTop: `1px solid ${t.border}`,
      borderBottom: `1px solid ${t.border}`,
      textAlign: 'center',
      transition: 'border-color 0.3s cubic-bezier(0.22,1,0.36,1)',
    }}
      onMouseEnter={e => {
        e.currentTarget.style.borderTopColor = '#000';
        e.currentTarget.style.borderBottomColor = '#000';
      }}
      onMouseLeave={e => {
        e.currentTarget.style.borderTopColor = t.border;
        e.currentTarget.style.borderBottomColor = t.border;
      }}
    >
      {/* Quote at top */}
      <blockquote style={{
        fontFamily: t.serif,
        fontSize: 'clamp(18px, 3vw, 26px)',
        fontWeight: 400,
        fontStyle: 'italic',
        color: t.text,
        lineHeight: 1.6,
        margin: 0,
        maxWidth: 700,
      }}>
        "Don't build for the sake of building. Build something that matters."
      </blockquote>

      {/* Name & Title */}
      <div>
        <div style={{
          fontSize: 15,
          fontWeight: 600,
          color: t.text,
          letterSpacing: '0.02em',
          marginBottom: 4,
        }}>
          Ritesh Kadian
        </div>
        <div style={{
          fontSize: 13,
          color: t.muted,
          fontWeight: 400,
        }}>
          Founder, SkillVector
        </div>
      </div>
    </div>
  );
}
