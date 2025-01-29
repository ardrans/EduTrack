import React, { useState, useEffect } from 'react';
import { Form, Button, Card } from 'react-bootstrap';

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
        <Card className="p-4" style={{ boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)', borderRadius: '10px' }}>
            <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3">
                    <Form.Label>Name</Form.Label>
                    <Form.Control
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        placeholder="Enter Name"
                        required
                    />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Label>Email</Form.Label>
                    <Form.Control
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        placeholder="Enter Email"
                        required
                    />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Label>Phone</Form.Label>
                    <Form.Control
                        type="text"
                        name="phone"
                        value={formData.phone}
                        onChange={handleChange}
                        placeholder="Enter Phone"
                        required
                    />
                </Form.Group>
                <Form.Group className="mb-3">
                    <Form.Label>Profile Picture (URL)</Form.Label>
                    <Form.Control
                        type="text"
                        name="profile_picture"
                        value={formData.profile_picture}
                        onChange={handleChange}
                        placeholder="Enter Profile Picture URL"
                    />
                </Form.Group>
                <Button variant="primary" type="submit" style={{ width: '100%' }}>
                    Submit
                </Button>
            </Form>
        </Card>
    );
};

export default StudentForm;
