import React, { useState, useEffect } from 'react';

const StudentForm = ({ onSubmit, student }) => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        phone: '',
        profile_picture: '',
    });

    useEffect(() => {
        if (student) {
            setFormData(student);
        }
    }, [student]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prev) => ({ ...prev, [name]: value }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(formData);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                placeholder="Name"
                required
            />
            <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="Email"
                required
            />
            <input
                type="text"
                name="phone"
                value={formData.phone}
                onChange={handleChange}
                placeholder="Phone"
                required
            />
            <input
                type="text"
                name="profile_picture"
                value={formData.profile_picture}
                onChange={handleChange}
                placeholder="Profile Picture (URL)"
            />
            <button type="submit">Submit</button>
        </form>
    );
};

export default StudentForm;
