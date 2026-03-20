export const t = {
  bg:           '#ffffff',
  surface:      '#fafafa',
  surfaceHover: '#f5f5f5',
  border:       '#e5e5e5',
  borderDark:   '#0a0a0a',
  text:         '#0f0f0f',
  muted:        '#5a5a5a',
  faint:        '#888888',
  placeholder:  '#aaaaaa',

  // Premium accent colors
  primary:      '#1d4ed8',
  primaryLight: '#3b82f6',
  accent:       '#06b6d4',
  accentAlt:    '#8b5cf6',
  success:      '#10b981',

  // Backgrounds
  darkBg:       '#0f172a',
  gradientStart: '#1e3a8a',
  gradientEnd:   '#312e81',

  green:        '#10b981',
  greenBg:      '#ecfdf5',
  greenBorder:  '#a7f3d0',

  red:          '#ef4444',
  redBg:        '#fef2f2',
  redBorder:    '#fecaca',

  amber:        '#f59e0b',
  amberBg:      '#fffbeb',
  amberBorder:  '#fde68a',

  blue:         '#3b82f6',
  blueBg:       '#eff6ff',
  blueBorder:   '#bfdbfe',

  serif: "'Instrument Serif', Georgia, serif",
  sans:  "'Outfit', -apple-system, sans-serif",
};

export const card = {
  background:   '#fff',
  border:       `1px solid ${t.border}`,
  borderRadius: 24,
  padding:      '40px 44px',
  boxShadow:    '0 2px 8px rgba(0, 0, 0, 0.04), 0 1px 3px rgba(0, 0, 0, 0.02)',
  transition:   'all 0.3s cubic-bezier(0.22, 1, 0.36, 1)',
};

export const inputBase = {
  width:        '100%',
  padding:      '14px 18px',
  background:   '#f9fafb',
  border:       `1px solid ${t.border}`,
  borderRadius: 14,
  fontFamily:   t.sans,
  fontSize:     14,
  color:        t.text,
  outline:      'none',
  transition:   'all 0.2s cubic-bezier(0.22, 1, 0.36, 1)',
  lineHeight:   1.5,
};

export const fieldLabel = {
  display:       'block',
  fontSize:      12,
  fontWeight:    500,
  letterSpacing: '0.04em',
  textTransform: 'uppercase',
  color:         t.faint,
  marginBottom:  8,
};

export const eyebrow = {
  fontSize:      10,
  fontWeight:    700,
  letterSpacing: '0.15em',
  textTransform: 'uppercase',
  color:         '#666',
  marginBottom:  10,
};

export const sectionTitle = {
  fontFamily:    t.serif,
  fontSize:      32,
  fontWeight:    400,
  color:         t.text,
  lineHeight:    1.2,
  marginBottom:  8,
  letterSpacing: '-0.01em',
};

export const GLOBAL_CSS = `
  @keyframes fadeUp {20px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
  }
  @keyframes slideInRight {
    from { opacity: 0; transform: translateX(-20px); }
    to   { opacity: 1; transform: translateX(0); }
  }
  @keyframes glow {
    0%, 100% { box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04); }
    50% { box-shadow: 0 4px 16px rgba(59, 130, 246, 0.08); }
  }
  @keyframes spin {
    to { transform: rotate(360deg); }
  }

  .fade-up { animation: fadeUp 0.6s cubic-bezier(0.22,1,0.36,1) both; }
  .fade-in { animation: fadeIn 0.5s ease both; }
  .slide-in { animation: slideInRight 0.6s cubic-bezier(0.22,1,0.36,1) both; }

  .btn-primary {
    display: inline-flex; align-items: center; justify-content: center;
    padding: 14px 32px; background: linear-gradient(135deg, #1f2937 0%, #111827 100%); color: #fff;
    border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; font-family: 'Outfit', sans-serif;
    font-size: 14px; font-weight: 600; cursor: pointer;
    transition: all 0.3s cubic-bezier(0.22,1,0.36,1); letter-spacing: 0.01em;
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
  }
  .btn-primary:hover:not(:disabled) {
    background: linear-gradient(135deg, #374151 0%, #1f2937 100%);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.16);
  }
  .btn-primary:disabled {
    background: #d1d5db; cursor: not-allowed; transform: none; box-shadow: none;
  }

  .btn-outline {
    display: inline-flex; align-items: center; justify-content: center;
    padding: 13px 28px; background: transparent; color: #0f0f0f;
    border: 1.5px solid #e5e5e5; border-radius: 12px;
    font-family: 'Outfit', sans-serif; font-size: 14px; font-weight: 600;
    cursor: pointer; transition: all 0.3s cubic-bezier(0.22,1,0.36,1);
  }
  .btn-outline:hover { 
    border-color: #0f0f0f; 
    background: #f9fafb;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
  }

  .btn-full { width: 100%; }

  .input-focus:focus { 
    border-color: #3b82f6 !important; 
    background: #f0f9ff !important; 
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
  }

  .nav-link {
    font-size: 13px; color: #5a5a5a; font-weight: 500;
    cursor: pointer; transition: color 0.2s;
  }
  .nav-link:hover { color: #0f0f0f; }

  .feature-card {
    padding: 36px; border: 1px solid #e5e5e5; border-radius: 18px;
    background: #fff; transition: all 0.3s cubic-bezier(0.22,1,0.36,1);
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  }
  .feature-card:hover {
    border-color: #d1d5db;
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.08);
  }

  .section-tag {
    display: inline-block; padding: 8px 16px; background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%);
    border-radius: 12px; font-size: 11px; font-weight: 700;
    color: #5a5a5a; letter-spacing: 0.08em; text-transform: uppercase;
    margin-bottom: 20px; border: 1px solid #e5e5e5;
  }

  .priority-row {
    display: flex; align-items: center; gap: 14px;
    padding: 14px 18px; border-radius: 12px; margin-bottom: 10px;
    border: 1px solid #e5e5e5; background: #f9fafb;
    transition: all 0.2s;
  }
  .priority-row:hover {
    border-color: #d1d5db;
    background: #fff;
  }ottom: 8px;
    border: 1.5px solid #ebebeb; background: #fafafa;
    transition: border-color 0.2s, transform 0.15s; cursor: default;
  }
  .priority-row:hover { border-color: #0a0a0a; transform: translateX(3px); }

  .roadmap-content {
    flex: 1; background: #fafafa; border: 1.5px solid #ebebeb;
    border-radius: 12px; padding: 14px 18px; transition: border-color 0.2s;
  }
  .roadmap-content:hover { border-color: #0a0a0a; }

  .tracker-item {
    display: flex; align-items: center; gap: 10px;
    padding: 10px 13px; border-radius: 10px;
    border: 1.5px solid #ebebeb; background: #fafafa;
    cursor: pointer; transition: all 0.18s; user-select: none;
  }
  .tracker-item:hover { border-color: #0a0a0a; }
  .tracker-item.checked { border-color: #1a7a3f; background: #f0faf4; }

  .pill {
    display: inline-block; padding: 4px 11px; border-radius: 20px;
    font-size: 12px; margin: 3px; font-weight: 400;
  }
  .pill-green { background: #f0faf4; border: 1px solid #b6e8c7; color: #1a7a3f; }
  .pill-red   { background: #fff2f2; border: 1px solid #f5c0c0; color: #b92b2b; }

  .stat-cell {
    padding: 40px 28px; border-top: 1px solid #ebebeb;
  }
`;
