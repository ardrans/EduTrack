import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const loginUser = async (email, password) => {
    try {
        const response = await axios.post(`${API_URL}/auth/login`, { email, password });
        localStorage.setItem('token', response.data.token);
        return response.data;
    } catch (error) {
        console.error('Login failed:', error);
        throw error;
    }
};


export const registerUser = async (data) => {
    try {
        const response = await axios.post(`${API_URL}/auth/users`, data);
        return response.data;
    } catch (error) {
        console.error('Registration failed:', error);
        throw error;
    }
};

export const createUserWithRole = async (data) => {
    const token = localStorage.getItem('token');
    try {
        const response = await axios.post(
            `${API_URL}/auth/users`,
            data,
            { headers: { Authorization: `Bearer ${token}` } }
        );
        return response.data;
    } catch (error) {
        console.error('Error creating user:', error);
        throw error;
    }
};

export const addRole = async (roleName) => {
    try {
        const response = await axios.post(`${API_URL}/auth/roles`, { name: roleName });
        return response.data;
    } catch (error) {
        console.error('Error adding role:', error);
        throw error;
    }
};

export const getStudents = async () => {
    const token = localStorage.getItem('token');
    console.log(token);
    const response = await axios.get(`${API_URL}/students/students`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
};

export const getStudent = async (id) => {
    const token = localStorage.getItem('token');
    const response = await axios.get(`${API_URL}/students/students${id}`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
};

export const createStudent = async (data) => {
    const token = localStorage.getItem('token');
    const response = await axios.post(`${API_URL}/students/students`, data, {
        headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
};

export const updateStudent = async (id, data) => {
    const token = localStorage.getItem('token');
    const response = await axios.put(`${API_URL}/students/students${id}`, data, {
        headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
};

export const deleteStudent = async (id) => {
    const token = localStorage.getItem('token');
    const response = await axios.delete(`${API_URL}/students/students${id}`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
};
