import MatchScoreCard  from './MatchScoreCard';
import SkillGapChart   from './SkillGapChart';
import RoadmapTimeline from './RoadmapTimeline';
import ProgressTracker from './ProgressTracker';

export default function Results({ gapData, roadmapData, userId, onReset }) {
  if (!gapData || !roadmapData) return null;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>

      <MatchScoreCard
        current={gapData.match_score}
        projected={gapData.projected_score_after_learning}
      />

      <SkillGapChart
        userSkills={gapData.user_skills}
        missingSkills={gapData.missing_skills}
        prioritySkills={gapData.priority_skills}
      />

      <RoadmapTimeline roadmap={roadmapData.roadmap} />

      <ProgressTracker userId={userId} skills={gapData.missing_skills} />

      <div style={{ textAlign: 'center', paddingTop: 4 }}>
        <button className="btn-outline" onClick={onReset}>← Start new analysis</button>
      </div>
    </div>
  );
}
