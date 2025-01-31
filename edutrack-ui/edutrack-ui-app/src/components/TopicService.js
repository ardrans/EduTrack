import axios from 'axios';

const API_URL = 'http://localhost:5000';

// Create an Axios instance with a default Authorization header
const axiosInstance = axios.create({
    baseURL: API_URL,
});

// Add Authorization token to requests dynamically
axiosInstance.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

export const getTopics = async () => {
    try {
        const response = await axiosInstance.get('/topics/topics');
        return response.data;
    } catch (error) {
        console.error('Error fetching topics:', error);
        throw error;
    }
};

export const createTopic = async (topicData) => {
    try {
        const response = await axiosInstance.post('/topics/topics', topicData);
        return response.data;
    } catch (error) {
        console.error('Error creating topic:', error);
        throw error;
    }
};

export const updateTopic = async (id, topicData) => {
    try {
        const response = await axiosInstance.put(`/topics/topics/${id}`, topicData);
        return response.data;
    } catch (error) {
        console.error('Error updating topic:', error);
        throw error;
    }
};

export const deleteTopic = async (id) => {
    try {
        await axiosInstance.delete(`/topics/${id}`);
    } catch (error) {
        console.error('Error deleting topic:', error);
        throw error;
    }
};

export const getTopic = async (topicId) => {
    try {
        const response = await axiosInstance.get(`/topics/topics/${topicId}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching topic details:', error);
        throw error;
    }
};
