export const t = {
  bg:           '#ffffff',
  surface:      '#fafafa',
  surfaceHover: '#f5f5f5',
  border:       '#ebebeb',
  borderDark:   '#0a0a0a',
  text:         '#0a0a0a',
  muted:        '#666666',
  faint:        '#aaaaaa',
  placeholder:  '#bbbbbb',

  green:        '#1a7a3f',
  greenBg:      '#f0faf4',
  greenBorder:  '#b6e8c7',

  red:          '#b92b2b',
  redBg:        '#fff2f2',
  redBorder:    '#f5c0c0',

  amber:        '#b45309',
  amberBg:      '#fffbeb',
  amberBorder:  '#fde68a',

  blue:         '#1d4ed8',
  blueBg:       '#eff6ff',
  blueBorder:   '#bfdbfe',

  serif: "'Instrument Serif', Georgia, serif",
  sans:  "'Outfit', -apple-system, sans-serif",
};

export const card = {
  background:   '#fff',
  border:       `1.5px solid ${t.border}`,
  borderRadius: 20,
  padding:      '36px 40px',
};

export const inputBase = {
  width:        '100%',
  padding:      '13px 16px',
  background:   t.surface,
  border:       `1.5px solid ${t.border}`,
  borderRadius: 12,
  fontFamily:   t.sans,
  fontSize:     14,
  color:        t.text,
  outline:      'none',
  transition:   'border-color 0.2s, background 0.2s',
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
  fontSize:      11,
  fontWeight:    600,
  letterSpacing: '0.1em',
  textTransform: 'uppercase',
  color:         '#999',
  marginBottom:  6,
};

export const sectionTitle = {
  fontFamily:    t.serif,
  fontSize:      26,
  fontWeight:    400,
  color:         t.text,
  lineHeight:    1.2,
  marginBottom:  6,
};

export const GLOBAL_CSS = `
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
  }
  @keyframes spin {
    to { transform: rotate(360deg); }
  }

  .fade-up { animation: fadeUp 0.5s cubic-bezier(0.22,1,0.36,1) both; }
  .fade-in { animation: fadeIn 0.4s ease both; }

  .btn-primary {
    display: inline-flex; align-items: center; justify-content: center;
    padding: 13px 28px; background: #0a0a0a; color: #fff;
    border: none; border-radius: 100px; font-family: 'Outfit', sans-serif;
    font-size: 14px; font-weight: 500; cursor: pointer;
    transition: all 0.2s; letter-spacing: 0.01em;
  }
  .btn-primary:hover:not(:disabled) {
    background: #222; transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.14);
  }
  .btn-primary:disabled {
    background: #c8c8c8; cursor: not-allowed; transform: none; box-shadow: none;
  }

  .btn-outline {
    display: inline-flex; align-items: center; justify-content: center;
    padding: 12px 26px; background: transparent; color: #0a0a0a;
    border: 1.5px solid #e0e0e0; border-radius: 100px;
    font-family: 'Outfit', sans-serif; font-size: 14px; font-weight: 500;
    cursor: pointer; transition: all 0.2s;
  }
  .btn-outline:hover { border-color: #0a0a0a; background: #fafafa; }

  .btn-full { width: 100%; }

  .input-focus:focus { border-color: #0a0a0a !important; background: #fff !important; }

  .nav-link {
    font-size: 13px; color: #666; font-weight: 400;
    cursor: pointer; transition: color 0.15s;
  }
  .nav-link:hover { color: #0a0a0a; }

  .feature-card {
    padding: 32px; border: 1.5px solid #ebebeb; border-radius: 20px;
    background: #fff; transition: all 0.2s;
  }
  .feature-card:hover {
    border-color: #0a0a0a; transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.06);
  }

  .section-tag {
    display: inline-block; padding: 6px 14px; background: #f5f5f5;
    border-radius: 100px; font-size: 12px; font-weight: 500;
    color: #666; letter-spacing: 0.04em; text-transform: uppercase;
    margin-bottom: 20px;
  }

  .priority-row {
    display: flex; align-items: center; gap: 14px;
    padding: 13px 16px; border-radius: 12px; margin-bottom: 8px;
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
