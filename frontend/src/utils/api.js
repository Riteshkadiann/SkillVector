import axios from 'axios';

const BASE_URL = 'http://localhost:8010/api';

export const uploadResumePDF = async (userId, file) => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('user_id', userId);
  const res = await axios.post(`${BASE_URL}/resume/upload`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return res.data;
};

export const uploadResumeText = async (userId, rawText) => {
  const res = await axios.post(`${BASE_URL}/resume/text`, {
    user_id: userId,
    raw_text: rawText,
  });
  return res.data;
};

export const analyzeJob = async (userId, jobTitle, jobDescription) => {
  const res = await axios.post(`${BASE_URL}/jobs/analyze`, {
    user_id: userId,
    job_title: jobTitle,
    job_description: jobDescription,
  });
  return res.data;
};

export const getSkillGap = async (userId) => {
  const res = await axios.get(`${BASE_URL}/gap/${userId}`);
  return res.data;
};

export const getRoadmap = async (userId) => {
  const res = await axios.get(`${BASE_URL}/roadmap/${userId}`);
  return res.data;
};

export const updateProgress = async (userId, completedSkills) => {
  const res = await axios.put(`${BASE_URL}/roadmap/progress/${userId}`, {
    user_id: userId,
    completed_skills: completedSkills,
  });
  return res.data;
};
