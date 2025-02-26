import axios from 'axios';

const API_URL = 'http://localhost:5000';

// Create an Axios instance
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

// Fetch all batch-student associations
export const getAllAssociations = async () => {
    try {
        const response = await axiosInstance.get('associations/associations/all');
        return response.data;
    } catch (error) {
        console.error('Error fetching all associations:', error);
        throw error;
    }
};

// Fetch students by batch ID
export const getStudentsByBatch = async (batchId) => {
    try {
        const response = await axiosInstance.get(`associations/associations/batch/${batchId}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching students by batch:', error);
        throw error;
    }
};

// Fetch batches by student ID
export const getBatchesByStudent = async (studentId) => {
    try {
        const response = await axiosInstance.get(`associations/associations/student/${studentId}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching batches by student:', error);
        throw error;
    }
};

// Create a new batch-student association
export const createAssociation = async (associationData) => {
    try {
        const response = await axiosInstance.post('associations/associations', associationData);
        return response.data;
    } catch (error) {
        console.error('Error creating association:', error);
        throw error;
    }
};

// Delete an association by ID
export const deleteAssociation = async (associationId) => {
    try {
        await axiosInstance.delete(`associations/associations/${associationId}`);
    } catch (error) {
        console.error('Error deleting association:', error);
        throw error;
    }
};