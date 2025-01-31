import React, { useState, useEffect } from 'react';
import { Form, Button } from 'react-bootstrap';

const TopicForm = ({ onSubmit, topic }) => {
    const [formData, setFormData] = useState({
        name: '',
        description: '',
        course_id: ''
    });

    useEffect(() => {
        if (topic) {
            setFormData({
                name: topic.name,
                description: topic.description,
                course_id: topic.course_id
            });
        }
    }, [topic]);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(formData);
    };

    return (
        <Form onSubmit={handleSubmit}>
            <Form.Group controlId="name">
                <Form.Label>Topic Name</Form.Label>
                <Form.Control 
                    type="text" 
                    name="name" 
                    value={formData.name} 
                    onChange={handleChange} 
                    required 
                />
            </Form.Group>
            <Form.Group controlId="description">
                <Form.Label>Description</Form.Label>
                <Form.Control 
                    as="textarea" 
                    name="description" 
                    value={formData.description} 
                    onChange={handleChange} 
                />
            </Form.Group>
            <Form.Group controlId="course_id">
                <Form.Label>Course ID</Form.Label>
                <Form.Control 
                    type="text" 
                    name="course_id" 
                    value={formData.course_id} 
                    onChange={handleChange} 
                    required 
                />
            </Form.Group>
            <Button variant="primary" type="submit" className="mt-3">
                {topic ? 'Update Topic' : 'Create Topic'}
            </Button>
        </Form>
    );
};

export default TopicForm;