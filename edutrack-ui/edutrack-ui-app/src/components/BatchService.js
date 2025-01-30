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

export const getBatches = async () => {
    try {
        const response = await axiosInstance.get('/users/batches');
        return response.data;
    } catch (error) {
        console.error('Error fetching batches:', error);
        throw error;
    }
};

export const createBatch = async (batchData) => {
    try {
        console.log(batchData);
        const response = await axiosInstance.post('/users/batches', batchData);
        return response.data;
    } catch (error) {
        console.error('Error creating batch:', error);
        throw error;
    }
};

export const updateBatch = async (id, batchData) => {
    try {
        const response = await axiosInstance.put(`/users/batches/${id}`, batchData);
        return response.data;
    } catch (error) {
        console.error('Error updating batch:', error);
        throw error;
    }
};

export const deleteBatch = async (id) => {
    try {
        await axiosInstance.delete(`/users/batches/${id}`);
    } catch (error) {
        console.error('Error deleting batch:', error);
        throw error;
    }
};

export const getBatch = async (batchId) => {
    try {
        const response = await axiosInstance.get(`/users/batches/${batchId}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching batch details:', error);
        throw error;
    }
};

export const getCourses = async () => {
    try {
        const response = await axiosInstance.get('/courses/courses');
        return response.data;
    } catch (error) {
        console.error('Error fetching courses:', error);
        throw error;
    }
};

export const getTrainers = async () => {
    try {
        const response = await axiosInstance.get('auth/users/trainers');
        return response.data;
    } catch (error) {
        console.error('Error fetching trainers:', error);
        throw error;
    }
};
