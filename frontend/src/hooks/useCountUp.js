import { useState, useEffect, useRef } from 'react';

/**
 * Animates a number from 0 to `target` over `duration` ms
 * using an ease-out cubic curve.
 * Fires only once the element (returned ref) enters the viewport.
 *
 * Usage:
 *   const { ref, value } = useCountUp(70, 1200);
 *   <div ref={ref}>{value}%</div>
 */
export default function useCountUp(target, duration = 1200, delay = 0) {
  const [value, setValue]     = useState(0);
  const [started, setStarted] = useState(false);
  const ref                   = useRef(null);

  // IntersectionObserver — trigger when element scrolls into view
  useEffect(() => {
    const el = ref.current;
    if (!el) return;

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setTimeout(() => setStarted(true), delay);
          observer.disconnect();
        }
      },
      { threshold: 0.3 }
    );

    observer.observe(el);
    return () => observer.disconnect();
  }, [delay]);

  // Count-up animation
  useEffect(() => {
    if (!started) return;

    let startTime = null;
    let rafId;

    const step = (timestamp) => {
      if (!startTime) startTime = timestamp;
      const elapsed  = timestamp - startTime;
      const progress = Math.min(elapsed / duration, 1);
      // ease-out cubic: starts fast, decelerates to a snap
      const eased    = 1 - Math.pow(1 - progress, 3);

      setValue(Math.floor(eased * target));

      if (progress < 1) {
        rafId = requestAnimationFrame(step);
      } else {
        setValue(target); // guarantee exact final value
      }
    };

    rafId = requestAnimationFrame(step);
    return () => cancelAnimationFrame(rafId);
  }, [started, target, duration]);

  return { ref, value };
}
