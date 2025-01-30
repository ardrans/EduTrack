import React, { useState, useEffect } from 'react';
import { Form, Button } from 'react-bootstrap';

const CourseForm = ({ onSubmit, course }) => {
    const [formData, setFormData] = useState({ name: '', description: '' });

    useEffect(() => {
        if (course) {
            setFormData({ name: course.name, description: course.description });
        } else {
            setFormData({ name: '', description: '' });
        }
    }, [course]);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(formData);
    };

    return (
        <Form onSubmit={handleSubmit}>
            <Form.Group controlId="courseName">
                <Form.Label>Course Name</Form.Label>
                <Form.Control
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    required
                />
            </Form.Group>
            <Form.Group controlId="courseDescription" className="mt-3">
                <Form.Label>Description</Form.Label>
                <Form.Control
                    as="textarea"
                    name="description"
                    value={formData.description}
                    onChange={handleChange}
                    required
                />
            </Form.Group>
            <Button variant="primary" type="submit" className="mt-3">
                {course ? 'Update Course' : 'Add Course'}
            </Button>
        </Form>
    );
};

export default CourseForm;
