import axios from 'axios';

const API_URL = 'http://localhost:5000';

// Create an Axios instance with a default Authorization header
const axiosInstance = axios.create({
    baseURL: API_URL,
});

// Add Authorization token to requests dynamically
axiosInstance.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
}, (error) => Promise.reject(error));

export const getCourses = async () => {
    try {
        const response = await axiosInstance.get('/courses/courses');
        return response.data;
    } catch (error) {
        console.error('Error fetching courses:', error);
        throw error;
    }
};

export const createCourse = async (courseData) => {
    try {
        const response = await axiosInstance.post('/courses/courses', courseData);
        return response.data;
    } catch (error) {
        console.error('Error creating course:', error);
        throw error;
    }
};

export const updateCourse = async (id, courseData) => {
    try {
        const response = await axiosInstance.put(`/courses/courses/${id}`, courseData);
        return response.data;
    } catch (error) {
        console.error('Error updating course:', error);
        throw error;
    }
};

export const deleteCourse = async (id) => {
    try {
        await axiosInstance.delete(`/courses/courses/${id}`);
    } catch (error) {
        console.error('Error deleting course:', error);
        throw error;
    }
};

export const getCourse = async (courseId) => {
    try {
        const response = await axiosInstance.get(`/courses/courses/${courseId}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching course details:', error);
        throw error;
    }
};
